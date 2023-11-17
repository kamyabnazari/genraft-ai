from fastapi import APIRouter, HTTPException
from app.models.pydantic_models import CreateChatRequest
from app.utils.chat_utils import create_chat_thread_util, insert_chat_data_util, associate_chat_with_project_util, chat_thread_exists_util
from app.dependencies import get_database

router = APIRouter()
database = get_database()

@router.post("/chat-stakeholder-consultant")
async def chat_stakeholder_consultant(id: int, request_body: CreateChatRequest):
    try:
        primary_to_secondary_name = request_body.chat_name + "-primary-to-secondary"
        secondary_to_primary_name = request_body.chat_name + "-secondary-to-primary"
        
        # Check if the chat threads already exist
        if await chat_thread_exists_util(
            primary_to_secondary_name=primary_to_secondary_name,
            secondary_to_primary_name=secondary_to_primary_name
        ):
            return {"message": f"Chat threads related to '{request_body.chat_name}' already exist"}
        
        # Assitant Primary to Assistant Secondary Chat
        
        # Create an assistant
        primary_secondary_chat_thread_data = await create_chat_thread_util()
        
        # Insert the assistant data into the assistants table
        primary_secondary_chat_id = await insert_chat_data_util(
            chat_thread_id=primary_secondary_chat_thread_data.id,
            chat_name=primary_to_secondary_name,
            chat_assistant_primary=request_body.chat_assistant_primary,
            chat_assistant_secondary=request_body.chat_assistant_secondary,
            chat_goal=request_body.chat_goal
            )

        # Associate the assistant with the project
        await associate_chat_with_project_util(id, primary_secondary_chat_id)

        # Assitant Secondary to Assistant Primary Chat
        
        # Create an assistant
        secondary_primary_chat_thread_data = await create_chat_thread_util()
        
        # Insert the assistant data into the assistants table
        secondary_primary_chat_id = await insert_chat_data_util(
            chat_thread_id=secondary_primary_chat_thread_data.id,
            chat_name=secondary_to_primary_name,
            chat_assistant_primary=request_body.chat_assistant_secondary,
            chat_assistant_secondary=request_body.chat_assistant_primary,
            chat_goal=request_body.chat_goal
            )

        # Associate the assistant with the project
        await associate_chat_with_project_util(id, secondary_primary_chat_id)

        return {"message": f"Chat '{request_body.chat_name}' created successfully for project {id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating chat: {str(e)}")
