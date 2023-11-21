from fastapi import APIRouter, HTTPException
from app.models.pydantic_models import CreateAssistantRequest
from app.utils.assistant_utils import create_assistant_util, insert_assistant_data_util, associate_assistant_with_project_util, assistant_exists_util, generate_assistant_instructions
from app.dependencies import get_database

router = APIRouter()
database = get_database()

@router.post("/create-assistant")
async def create_assistant_endpoint(id: int, request_body: CreateAssistantRequest):
    try:
        # Check if the assistant already exists
        if await assistant_exists_util(request_body.assistant_name, request_body.assistant_type):
            return {"message": f"{request_body.assistant_type} Assistant already exists for this name"}
        
        # Generate assistant instructions
        assistant_instructions = generate_assistant_instructions(request_body.assistant_type)

        # Create an assistant
        assistant_data = await create_assistant_util(
            name=request_body.assistant_name,
            instructions=assistant_instructions,
            model=request_body.assistant_model
            )
        
        # Insert the assistant data into the assistants table
        assistant_id = await insert_assistant_data_util(
            assistant_id=assistant_data.id,
            assistant_name=request_body.assistant_name,
            assistant_type=request_body.assistant_type,
            assistant_instructions=assistant_instructions,
            assistant_model=request_body.assistant_model
        )

        # Associate the assistant with the project
        await associate_assistant_with_project_util(id, assistant_id)

        return {"message": f"{request_body.assistant_type} Assistant Created Successfully for project {id}", "assistant_id": assistant_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating stakeholder assistant: {str(e)}")
