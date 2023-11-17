from fastapi import APIRouter, HTTPException
from app.utils.assistant_utils import get_openai_assistant_id_by_name_util
from app.utils.project_utils import get_project_folder_path_util, get_project_idea_initial_util
from app.models.pydantic_models import CreateChatRequest
from app.utils.chat_utils import create_chat_thread_util, get_assistant_messages_util, insert_chat_data_util, associate_chat_with_project_util, chat_thread_exists_util, poll_for_completion_util, send_initial_message_util
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
        
        # Check if the chat threads already exist
        if await chat_thread_exists_util(
            primary_to_secondary_name=primary_to_secondary_name,
            secondary_to_primary_name=secondary_to_primary_name
        ):
            return {"message": f"Chat threads related to '{request_body.chat_name}' already exist"}
        
        # Assitant Primary to Assistant Secondary Chat
        
        # Create an assistant
        primary_secondary_chat_thread_data = await create_chat_thread_util()
        secondary_primary_chat_thread_data = await create_chat_thread_util()
        
        # Insert the assistant data into the assistants table
        primary_secondary_chat_id = await insert_chat_data_util(
            chat_thread_id=primary_secondary_chat_thread_data.id,
            chat_name=primary_to_secondary_name,
            chat_assistant_primary=request_body.chat_assistant_primary,
            chat_assistant_secondary=request_body.chat_assistant_secondary,
            chat_goal=request_body.chat_goal
            )
        
        # Insert the assistant data into the assistants table
        secondary_primary_chat_id = await insert_chat_data_util(
            chat_thread_id=secondary_primary_chat_thread_data.id,
            chat_name=secondary_to_primary_name,
            chat_assistant_primary=request_body.chat_assistant_secondary,
            chat_assistant_secondary=request_body.chat_assistant_primary,
            chat_goal=request_body.chat_goal
            )
        
        # Associate the assistant with the project
        await associate_chat_with_project_util(id, primary_secondary_chat_id)
        await associate_chat_with_project_util(id, secondary_primary_chat_id)
        
        # Initating the Chat process!

        # Step 1: Prepare the initial message for the first thread
        idea_initial = await get_project_idea_initial_util(id)
        
        initial_message = (
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
            assistant_id=primary_assistant_id,
            initial_message=initial_message
        )

        # Wait for the response
        if not await poll_for_completion_util(primary_secondary_chat_thread_data.id, primary_to_secondary_run.id):
            return {"message": "Error in completing the first chat"}

        # Step 3: Relay the Response to the Second Thread
        primary_to_secondary_messages = await get_assistant_messages_util(primary_secondary_chat_thread_data.id)
        response_from_first_assistant = primary_to_secondary_messages[-1]

        # Start the conversation in the second thread with the response from the first
        secondary_to_primary_run = await send_initial_message_util(
            thread_id=secondary_primary_chat_thread_data.id,
            assistant_id=secondary_assistant_id,
            initial_message=response_from_first_assistant
        )

        # Define maximum number of exchanges to prevent infinite loops
        max_exchanges = 3
        current_exchanges = 0

        while current_exchanges < max_exchanges:
            # Step 4: Conversation Loop
            
            # Wait for the second assistant's response
            if not await poll_for_completion_util(secondary_primary_chat_thread_data.id, secondary_to_primary_run.id):
                break  # Exit loop if there's an issue with the response

            # Get the last message from the second thread
            secondary_to_primary_messages = await get_assistant_messages_util(secondary_primary_chat_thread_data.id)
            response_from_second_assistant = secondary_to_primary_messages[-1]

            # Send this message as input to the first thread
            primary_to_secondary_run = await send_initial_message_util(
                thread_id=primary_secondary_chat_thread_data.id,
                assistant_id=secondary_assistant_id,
                initial_message=response_from_second_assistant
            )

            # Continue the loop with the roles reversed
            if not await poll_for_completion_util(primary_secondary_chat_thread_data.id, primary_to_secondary_run.id):
                break  # Exit loop if there's an issue with the response

            # Get the last message from the first thread
            primary_to_secondary_messages = await get_assistant_messages_util(primary_secondary_chat_thread_data.id)
            response_from_first_assistant = primary_to_secondary_messages[-1]

            print(f"Latest message from primary to secondary: {response_from_second_assistant}")
            print(f"Latest message from secondary to primary: {response_from_first_assistant}")

            # Send this message as input to the second thread
            secondary_to_primary_run = await send_initial_message_util(
                thread_id=secondary_primary_chat_thread_data.id,
                assistant_id=primary_assistant_id,
                initial_message=response_from_first_assistant
            )

            # Increment the exchange count
            current_exchanges += 1

            # Step 5: Check for End Condition
            if "<END>" in response_from_second_assistant:
                break  # End the conversation if the end condition is met

        # Step 6: Store and Process the Final Conversation
        final_primary_to_secondary_messages = await get_assistant_messages_util(primary_secondary_chat_thread_data.id)
        final_secondary_to_primary_messages = await get_assistant_messages_util(secondary_primary_chat_thread_data.id)
        
        # Assuming you have the folder_path from get_project_folder_path_util
        folder_path = await get_project_folder_path_util(id)

        # Define file paths using folder_path
        primary_to_secondary_file_path = os.path.join(folder_path, 'primary_to_secondary_chat_messages.json')
        secondary_to_primary_file_path = os.path.join(folder_path, 'secondary_to_primary_chat_messages.json')

        # Save the primary to secondary messages to a JSON file
        with open(primary_to_secondary_file_path, 'w') as file:
            json.dump(final_primary_to_secondary_messages, file, indent=4)

        # Save the secondary to primary messages to a JSON file
        with open(secondary_to_primary_file_path, 'w') as file:
            json.dump(final_secondary_to_primary_messages, file, indent=4)
        
        return {"message": f"Chat '{request_body.chat_name}' created successfully for project {id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating chat: {str(e)}")
