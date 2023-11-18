from fastapi import APIRouter, HTTPException
from app.utils.assistant_utils import get_openai_assistant_id_by_name_util
from app.utils.project_utils import get_project_folder_path_util, get_project_idea_initial_util
from app.models.pydantic_models import CreateChatRequest
from app.utils.chat_utils import associate_thread_with_chat_util, create_chat_thread_util, fetch_conversation_util, get_assistant_messages_util, insert_chat_data_util, associate_chat_with_project_util, chat_thread_exists_util, insert_thread_data_util, poll_for_completion_util, save_conversation_util, send_initial_message_util
from app.dependencies import get_database
import json
import os

router = APIRouter()
database = get_database()

@router.post("/chat-stakeholder-consultant")
async def chat_stakeholder_consultant(id: int, request_body: CreateChatRequest):
    try:
        primary_to_secondary_name = request_body.chat_name + "-primary-to-secondary"
        secondary_to_primary_name = request_body.chat_name + "-secondary-to-primary"
        
        # Check if the chat or its threads already exist
        exists, chat_id = await chat_thread_exists_util(
            chat_name=request_body.chat_name,
            primary_to_secondary_name=primary_to_secondary_name,
            secondary_to_primary_name=secondary_to_primary_name
        )
        if exists:
            return {"message": f"Chat or threads related to '{request_body.chat_name}' already exist", "chat_id": chat_id}

        # Assitant Primary to Assistant Secondary Chat
        
        # Create an assistant
        primary_secondary_chat_thread_data = await create_chat_thread_util()
        secondary_primary_chat_thread_data = await create_chat_thread_util()
        
        # Insert the assistant data into the assistants table
        chat_id = await insert_chat_data_util(
            chat_name=request_body.chat_name,
            chat_assistant_primary=request_body.chat_assistant_primary,
            chat_assistant_secondary=request_body.chat_assistant_secondary,
            chat_goal=request_body.chat_goal,
            chat_messages=""
            )
        
        # Insert the assistant data into the assistants table
        primary_secondary_thread_id = await insert_thread_data_util(
            thread_id=primary_secondary_chat_thread_data.id,
            thread_name=primary_to_secondary_name,
            thread_assistant_primary=request_body.chat_assistant_primary,
            thread_assistant_secondary=request_body.chat_assistant_secondary,
            thread_goal=request_body.chat_goal
            )
        
        # Insert the assistant data into the assistants table
        secondary_primary_thread_id = await insert_thread_data_util(
            thread_id=secondary_primary_chat_thread_data.id,
            thread_name=secondary_to_primary_name,
            thread_assistant_primary=request_body.chat_assistant_secondary,
            thread_assistant_secondary=request_body.chat_assistant_primary,
            thread_goal=request_body.chat_goal
            )
        
        # Associate the chat with the project
        await associate_chat_with_project_util(id, chat_id)

        # Associate the thread with the chat
        await associate_thread_with_chat_util(chat_id, primary_secondary_thread_id)
        await associate_thread_with_chat_util(chat_id, secondary_primary_thread_id)
                
        # Initating the Chat process!

        conversation = []

        # Step 1: Prepare the initial message for the first thread
        idea_initial = await get_project_idea_initial_util(id)
        
        initial_message_chat_1 = (
            "The goal of this conversation is: " + request_body.chat_goal + 
            ". Here is my initial project idea: " + idea_initial +
            ". Important: When you have reached the final result, mark the final sentence with <END>"
        )
        
        # Retrieve OpenAI Assistant IDs for primary and secondary assistants
        primary_assistant_id = await get_openai_assistant_id_by_name_util(request_body.chat_assistant_primary)
        secondary_assistant_id = await get_openai_assistant_id_by_name_util(request_body.chat_assistant_secondary)

        if not primary_assistant_id or not secondary_assistant_id:
            return {"message": "Error: Assistant not found"}
        
        # Step 2: Start the Conversation in the First Thread
        primary_to_secondary_run = await send_initial_message_util(
            thread_id=primary_secondary_chat_thread_data.id,
            assistant_id=secondary_assistant_id,
            initial_message=initial_message_chat_1
        )

        # Wait for the response
        if not await poll_for_completion_util(primary_secondary_chat_thread_data.id, primary_to_secondary_run.id):
            return {"message": "Error in completing the first chat"}
        
        # Get the last message from the first thread
        primary_to_secondary_messages = await get_assistant_messages_util(primary_secondary_chat_thread_data.id)
        response_from_secondary_assistant = primary_to_secondary_messages[0]
                
        initial_message_chat_2 = (
            "This was your initial idea: " + idea_initial + 
            ". Here was my firs response to your initial idea: " + response_from_secondary_assistant +
            ". I want you to responsed to my response please."
        )

        # Start the conversation in the second thread with the response from the first
        secondary_to_primary_run = await send_initial_message_util(
            thread_id=secondary_primary_chat_thread_data.id,
            assistant_id=primary_assistant_id,
            initial_message=initial_message_chat_2
        )
        
        # Wait for the response
        if not await poll_for_completion_util(secondary_primary_chat_thread_data.id, secondary_to_primary_run.id):
            return {"message": "Error in completing the second chat"}
        
        # Get the last message from the first thread
        secondary_to_primary_messages = await get_assistant_messages_util(secondary_primary_chat_thread_data.id)
        response_from_primary_assistant = secondary_to_primary_messages[0]
                
        # Add initial messages to the conversation list

        # Append messages with identifiers to the conversation list
        conversation.append({"sender": "stakeholder", "message": initial_message_chat_1})
        conversation.append({"sender": "consultant", "message": response_from_secondary_assistant})
        conversation.append({"sender": "consultant", "message": initial_message_chat_2})
        conversation.append({"sender": "stakeholder", "message": response_from_primary_assistant})
        
        # Initial setup for the loop with the first set of responses
        latest_response_from_stakeholder = response_from_primary_assistant
        latest_response_from_consultant = response_from_secondary_assistant
        
        # Define maximum number of exchanges to prevent infinite loops
        max_exchanges = 1
        current_exchanges = 0
        
        while current_exchanges < max_exchanges:                  
            # Consultant (secondary assistant) responding to the latest message from Stakeholder
            primary_to_secondary_run = await send_initial_message_util(
                thread_id=primary_secondary_chat_thread_data.id,
                assistant_id=secondary_assistant_id,
                initial_message=latest_response_from_stakeholder
            )
            
            
            # Wait for the response
            if not await poll_for_completion_util(primary_secondary_chat_thread_data.id, primary_to_secondary_run.id):
                return {"message": "Error in completing the first chat"}
            
            primary_to_secondary_messages = await get_assistant_messages_util(primary_secondary_chat_thread_data.id)

            latest_response_from_consultant = primary_to_secondary_messages[0]

            # Append consultant's response to the conversation
            conversation.append({"sender": "consultant", "message": latest_response_from_consultant})

            # Stakeholder (primary assistant) responding to the latest message from Consultant
            secondary_to_primary_run = await send_initial_message_util(
                thread_id=secondary_primary_chat_thread_data.id,
                assistant_id=primary_assistant_id,
                initial_message=latest_response_from_consultant
            )

            # Wait for the response
            if not await poll_for_completion_util(secondary_primary_chat_thread_data.id, secondary_to_primary_run.id):
                return {"message": "Error in completing the second chat"}
            
            secondary_to_primary_messages = await get_assistant_messages_util(secondary_primary_chat_thread_data.id)            
            latest_response_from_stakeholder = secondary_to_primary_messages[0]
            
            # Append stakeholder's response to the conversation
            conversation.append({"sender": "stakeholder", "message": latest_response_from_stakeholder})

            # Increment the exchange count
            current_exchanges += 1

            # Check for End Condition in both threads
            if "<END>" in latest_response_from_consultant or "<END>" in latest_response_from_stakeholder:
                break
        
        # Save the conversation in the database
        await save_conversation_util(primary_secondary_thread_id, conversation)
        await save_conversation_util(secondary_primary_thread_id, conversation)

        # Assuming you have the folder_path from get_project_folder_path_util
        folder_path = await get_project_folder_path_util(id)
        
        json_name = request_body.chat_name.replace('-', '_').lower()
        file_name = f"logs_chat_messages_{json_name}.json"
        
        # Define file path using folder_path
        conversation_file_path = os.path.join(folder_path, file_name)

        # Save the conversation to a JSON file
        with open(conversation_file_path, 'w') as file:
            json.dump(conversation, file, indent=4)
        
        return {
            "message": f"Chat '{request_body.chat_name}' created successfully for project {id}",
            "chat_id": chat_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating chat: {str(e)}")

@router.get("/{chat_id}")
async def get_chat_conversation(chat_id: int):
    try:
        conversation = await fetch_conversation_util(chat_id)
        return {"conversation": conversation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching conversation: {str(e)}")