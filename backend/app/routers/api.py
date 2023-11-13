from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import FileResponse
from app.models.pydantic_models import Project, ProjectStats, StepIdeaSubmitRequest, GenerateAssistantRequest
from app.models.database import projects
from app.dependencies import get_database
from app.core.config import settings
from openai import OpenAI, OpenAIError
from sqlalchemy import desc
from typing import List
import zipfile
import datetime
import shutil
import time
import os

router = APIRouter()
client = OpenAI(api_key=settings.openai_api_key)
database = get_database()

@router.get("/")
async def read_api_root():
    return {"message": "Welcome to the Genraft AI API!"}

@router.post("/project")
async def initialize_project(request_body: StepIdeaSubmitRequest):
    try:
        # Generate the current timestamp without microseconds
        timestamp = datetime.datetime.now()

        # Modify timestamp and name string for filesystem-friendly folder naming
        folder_timestamp = timestamp.strftime('%Y_%m_%d_at_%H_%M_%S')
        folder_name = request_body.name.replace(' ', '_').lower()
        project_folder = f"genraft_ai_data/projects/{folder_name}_{folder_timestamp}"
        os.makedirs(project_folder, exist_ok=True)

        # Write the initial idea into a text file
        with open(f"{project_folder}/prompt.txt", 'w') as file:
            file.write(request_body.idea)

        # Insert the project with the folder path and datetime object
        query = projects.insert().values(
            name=request_body.name,
            idea_initial=request_body.idea,
            idea_final="",
            folder_path=project_folder,
            created_at=timestamp
        )

        # Perform the database operation within a transaction
        async with database.transaction():
            new_project_id = await database.execute(query)

        return {"id": new_project_id}
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/project/{id}", response_model=Project)
async def get_project_by_id(id: int = Path(..., description="The ID of the project to retrieve")):
    try:
        # Start by checking if the project exists
        select_query = projects.select().where(projects.c.id == id)
        project = await database.fetch_one(select_query)

        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")

        # Convert the database model to the Pydantic model
        return Project(**project)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/project/{id}")
async def delete_project_by_id(id: int = Path(..., description="The ID of the project to delete")):
    try:
        # Start by checking if the project exists
        select_query = projects.select().where(projects.c.id == id)
        existing_project = await database.fetch_one(select_query)

        if existing_project is None:
            raise HTTPException(status_code=404, detail="Project not found")

        # Get the folder path
        folder_path = existing_project['folder_path']

        # If the project exists, proceed to delete it
        delete_query = projects.delete().where(projects.c.id == id)
        await database.execute(delete_query)

        # Delete the associated folder
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

        # Also delete the associated ZIP file if it exists
        zip_path = f"{folder_path}.zip"
        if os.path.exists(zip_path):
            os.remove(zip_path)

        return {"message": "Project successfully deleted"}
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/projects", response_model=List[Project])
async def get_all_projects():
    try:
        # Query to select all projects ordered by creation date in descending order
        query = projects.select().order_by(desc(projects.c.created_at))
        results = await database.fetch_all(query)
        
        # Transform the database results into a list of Project instances
        projects_list = [Project(**result) for result in results]

        return projects_list
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/project/{id}/download")
async def download_project_by_id(id: int = Path(..., description="The ID of the project to download")):
    try:
        # Check if the project exists and get its folder path
        select_query = projects.select().where(projects.c.id == id)
        existing_project = await database.fetch_one(select_query)

        if existing_project is None:
            raise HTTPException(status_code=404, detail="Project not found")

        folder_path = existing_project['folder_path']

        # Create a ZIP file from the folder
        zip_path = f"{folder_path}.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    zipf.write(os.path.join(root, file), 
                               os.path.relpath(os.path.join(root, file), 
                               os.path.join(folder_path, '..')))

        # Return the ZIP file as a response
        return FileResponse(zip_path, media_type='application/octet-stream', filename=os.path.basename(zip_path))
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats/projects", response_model=ProjectStats)
async def get_project_statistics():
    try:
        # Get all projects
        query = projects.select()
        all_projects = await database.fetch_all(query)
        total_projects = len(all_projects)

        total_files = 0
        total_assets = 0

        # File extensions considered as assets
        asset_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']

        # Count files and assets in each project folder
        for project in all_projects:
            folder_path = project['folder_path']
            for root, dirs, files in os.walk(folder_path):
                total_files += len(files)
                total_assets += sum(1 for file in files if os.path.splitext(file)[1].lower() in asset_extensions)

        # Combine the statistics into a single response object
        statistics = {
            "total_projects": total_projects,
            "total_files": total_files,
            "total_assets": total_assets
        }

        return statistics
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate_assistant")
async def generate_assistant(request_body: GenerateAssistantRequest):
    try:
        assistant = client.beta.assistants.create(
            name=request_body.name,
            instructions=request_body.instructions,
            tools=[{"type": "code_interpreter"}],
            model="gpt-3.5-turbo"
        )
        thread = client.beta.threads.create()
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=request_body.initial_message
        )
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )
        if not await poll_for_completion(thread.id, run.id):
            raise HTTPException(status_code=500, detail="Assistant run did not complete in time.")

        messages_response = client.beta.threads.messages.list(thread_id=thread.id)
        assistant_messages = [
            cp.text.value for msg in messages_response.data if msg.role == "assistant"
            for cp in msg.content if cp.type == 'text' and hasattr(cp, 'text')
        ]
        return {"messages": assistant_messages}
    except OpenAIError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

async def poll_for_completion(thread_id, run_id, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run_status.status == "completed":
            return True
        elif run_status.status in ["failed", "cancelled", "expired"]:
            return False
        time.sleep(1)
    return False