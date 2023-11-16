from fastapi import APIRouter, HTTPException
from app.models.pydantic_models import CreateAssistantRequest
from app.utils.assistant_utils import create_new_assistant, insert_assistant_data, associate_assistant_with_project, assistant_exists
from app.dependencies import get_database

router = APIRouter()
database = get_database()

@router.post("/start")
async def start_preparation(id: int):
    return {"message": "Start Preparation Phase for project!"}

@router.get("/idea")
async def get_idea(id: int):
    return {"id": id, "idea_initial": "This is the initial idea!"}

@router.post("/assistant-stakeholder")
async def create_stakeholder_assistant(id: int, request_body: CreateAssistantRequest):
    try:
        # Check if the assistant already exists
        if await assistant_exists(request_body.assistant_name, "stakeholder"):
            return {"message": "Stakeholder Assistant already exists for this name"}
        
        # Create an assistant
        assistant_data = await create_new_assistant(name=request_body.assistant_name, instructions=request_body.assistant_instructions, model=request_body.assistant_model)
        
        # Insert the assistant data into the assistants table
        assistant_id = await insert_assistant_data(assistant_id=assistant_data.id, assistant_name=request_body.assistant_name, assistant_type="stakeholder", assistant_instructions=request_body.assistant_instructions, assistant_model=request_body.assistant_model)

        # Associate the assistant with the project
        await associate_assistant_with_project(id, assistant_id)

        return {"message": f"Stakeholder Assistant Created Successfully for project {id}", "assistant_id": assistant_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating stakeholder assistant: {str(e)}")

@router.post("/assistant-consultant")
async def create_consultant_assistant(id: int, request_body: CreateAssistantRequest):
    try:
        # Check if the assistant already exists
        if await assistant_exists(request_body.assistant_name, "consultant"):
            return {"message": "Consultant Assistant already exists for this name"}
        
        # Create an assistant
        assistant_data = await create_new_assistant(name=request_body.assistant_name, instructions=request_body.assistant_instructions, model=request_body.assistant_model)
        
        # Insert the assistant data into the assistants table
        assistant_id = await insert_assistant_data(assistant_id=assistant_data.id, assistant_name=request_body.assistant_name, assistant_type="consultant", assistant_instructions=request_body.assistant_instructions, assistant_model=request_body.assistant_model)

        # Associate the assistant with the project
        await associate_assistant_with_project(id, assistant_id)

        return {"message": f"Consultant Assistant Created Successfully for project {id}", "assistant_id": assistant_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating stakeholder assistant: {str(e)}")

@router.get("/done")
async def finish_preparation(id: int):
    return {"message": "Preparation Phase Done for project!"}
