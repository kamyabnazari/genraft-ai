from fastapi import APIRouter, HTTPException
from app.models.pydantic_models import CreateChatRequest
from app.utils.chat_utils import create_chat_thread_util, insert_chat_data_util, associate_chat_with_project_util, chat_exists_util
from app.dependencies import get_database

router = APIRouter()
database = get_database()

@router.post("/chat-stakeholder-consultant")
async def chat_stakeholder_consultant(id: int, request_body: CreateChatRequest):
    try:
        # Check if the assistant already exists
        if await chat_exists_util(request_body.chat_name):
            return {"message": f"{request_body.chat_name} Chat already exists for this name"}
        
        # Create an assistant
        chat_thread_data = await create_chat_thread_util()
        
        # Insert the assistant data into the assistants table
        chat_id = await insert_chat_data_util(
            chat_thread_id=chat_thread_data.id,
            chat_name=request_body.chat_name,
            chat_assistant_primary=request_body.chat_assistant_primary,
            chat_assistant_secondary=request_body.chat_assistant_secondary,
            chat_goal=request_body.chat_goal
            )

        # Associate the assistant with the project
        await associate_chat_with_project_util(id, chat_id)

        return {"message": f"{request_body.chat_name} Chat Created Successfully for project {id}", "chat_id": chat_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating stakeholder assistant: {str(e)}")
