from fastapi import APIRouter, HTTPException
from app.utils.file_utils import save_conversation_to_file_util, save_markdown_to_file_util
from app.utils.assistant_utils import get_openai_assistant_id_by_name_util
from app.utils.project_utils import get_project_company_goal_util, get_project_folder_path_util, get_project_idea_final_util, get_project_idea_initial_util, save_project_company_goal_util, save_project_idea_final_util
from app.config.project_config import project_config
from app.models.pydantic_models import CreateChatRequest
from app.utils.chat_utils import associate_thread_with_chat_util, create_chat_thread_util, fetch_conversation_util, format_initial_message, get_assistant_messages_util, insert_chat_data_util, associate_chat_with_project_util, chat_thread_exists_util, insert_thread_data_util, list_thread_messages, poll_for_completion_util, retrieve_message_file, save_conversation_util, send_initial_message_util
from app.dependencies import get_database

router = APIRouter()
database = get_database()

@router.post("/create-chat")
async def create_chat(id: int, request_body: CreateChatRequest):
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
            chat_messages=""
            )
        
        # Insert the assistant data into the assistants table
        primary_secondary_thread_id = await insert_thread_data_util(
            thread_id=primary_secondary_chat_thread_data.id,
            thread_name=primary_to_secondary_name
            )
        
        # Insert the assistant data into the assistants table
        secondary_primary_thread_id = await insert_thread_data_util(
            thread_id=secondary_primary_chat_thread_data.id,
            thread_name=secondary_to_primary_name
            )
        
        # Associate the chat with the project
        await associate_chat_with_project_util(id, chat_id)

        # Associate the thread with the chat
        await associate_thread_with_chat_util(chat_id, primary_secondary_thread_id)
        await associate_thread_with_chat_util(chat_id, secondary_primary_thread_id)
        
        sender_name_primary = request_body.chat_assistant_primary.split(f"project-{id}-assistant-")[-1]
        sender_name_secondary = request_body.chat_assistant_secondary.split(f"project-{id}-assistant-")[-1]
        
        # Initating the Chat process!

        conversation = []

        # Determine the chat type, e.g., "stakeholder_consultant"
        chat_type = sender_name_primary + "_" + sender_name_secondary
        
        # Access the configuration for the determined chat type
        global_properties = project_config["global_properties"]
        chat_specific_config = project_config["chats"][chat_type]
        
        max_exchanges=global_properties["max_exchanges"]
        chat_end = global_properties["chat_end"]
        tech_scope=global_properties["tech_scope"]
        output_format_instructions=global_properties["output_format_instructions"]
        
        initial_message_chat_1_template = chat_specific_config["initial_message_chat_1"]
        initial_message_chat_2_template = chat_specific_config["initial_message_chat_2"]
        output_request = chat_specific_config["output_request"]
        chat_goal = chat_specific_config["chat_goal"]
        
        # Step 1: Prepare the initial input for the first thread
        initial_message_chat_1 = await format_initial_message(
            chat_type, 
            initial_message_chat_1_template, 
            id, 
            tech_scope, 
            chat_goal, 
            max_exchanges, 
            chat_end, 
            None
        )
        
        if not initial_message_chat_1:
            return {"message": "Error: Failed to format initial message for chat 1"}
        
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
        
        # Step 2: Prepare the initial message for the second thread
        initial_message_chat_2 = await format_initial_message(
            chat_type, 
            initial_message_chat_2_template, 
            id, 
            tech_scope, 
            chat_goal, 
            max_exchanges, 
            chat_end, 
            response_from_secondary_assistant
        )

        if not initial_message_chat_2:
            return {"message": "Error: Failed to format initial message for chat 2"}

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
        conversation.append({"sender": sender_name_primary, "message": initial_message_chat_1})
        conversation.append({"sender": sender_name_secondary, "message": response_from_secondary_assistant})
        conversation.append({"sender": sender_name_secondary, "message": initial_message_chat_2})
        conversation.append({"sender": sender_name_primary, "message": response_from_primary_assistant})
        
        # Initial setup for the loop with the first set of responses
        latest_response_from_primary_assistant = response_from_primary_assistant
        latest_response_from_secondary_assistant = response_from_secondary_assistant
        
        if chat_end in latest_response_from_primary_assistant:
            # Send a new message to the secondary assistant asking for the final output
            final_output_request = output_format_instructions + " - " + output_request
            
            # Append Primary Assistant response to the conversation
            conversation.append({"sender": sender_name_primary, "message": final_output_request})
            
            request_to_secondary_for_output = await send_initial_message_util(
                thread_id=primary_secondary_chat_thread_data.id,
                assistant_id=secondary_assistant_id,
                initial_message=final_output_request
            )

            # Wait for the response
            if not await poll_for_completion_util(primary_secondary_chat_thread_data.id, request_to_secondary_for_output.id):
                return {"message": "Error in requesting final output"}

            final_output_messages = await get_assistant_messages_util(primary_secondary_chat_thread_data.id)
            final_output_from_secondary = final_output_messages[0]

            # Append Primary Assistant response to the conversation
            conversation.append({"sender": sender_name_secondary, "message": final_output_from_secondary})
        
            # Directly use the response as the final output
            output_content = final_output_from_secondary.strip()
            if(chat_type == "stakeholder_consultant"):
                await save_project_idea_final_util(project_id=id, final_idea=output_content)
            elif(chat_type == "stakeholder_ceo"):
                await save_project_company_goal_util(project_id=id, company_goal=output_content)
            if chat_type in ["ceo_cpo", "ceo_cto"]:
                await save_markdown_to_file_util(project_id=id, chat_name=request_body.chat_name, markdown_content=output_content) 
            
            # Save the conversation in the database
            await save_conversation_util(chat_id=chat_id, conversation=conversation)
            
            # Save the conversation to a JSON file
            success = await save_conversation_to_file_util(id, request_body.chat_name, conversation)
            if not success:
                # Handle the error case as needed
                raise HTTPException(status_code=500, detail="Error saving conversation to file")
            
            return {
                "message": f"Chat '{request_body.chat_name}' created successfully for project {id}",
                "chat_id": chat_id
            }
                
        current_exchanges = 0
        
        while current_exchanges < max_exchanges:                  
            # Secondary assistant responding to the latest message from Primary assistant
            primary_to_secondary_run = await send_initial_message_util(
                thread_id=primary_secondary_chat_thread_data.id,
                assistant_id=secondary_assistant_id,
                initial_message=latest_response_from_primary_assistant
            )
            
            # Wait for the response
            if not await poll_for_completion_util(primary_secondary_chat_thread_data.id, primary_to_secondary_run.id):
                return {"message": "Error in completing the first chat"}
            
            primary_to_secondary_messages = await get_assistant_messages_util(primary_secondary_chat_thread_data.id)

            latest_response_from_secondary_assistant = primary_to_secondary_messages[0]            

            # Reminder message for the Secondary Assistant
            reminder_message_secondary = " Please evaluate the output. If acceptable, end the conversation with '{}'.".format(chat_end)
            latest_response_from_secondary_assistant += reminder_message_secondary

            # Append Secondary Assistant response to the conversation
            conversation.append({"sender": sender_name_secondary, "message": latest_response_from_secondary_assistant})

            # Primary Assistant responding to the latest message from Secondary assistant
            secondary_to_primary_run = await send_initial_message_util(
                thread_id=secondary_primary_chat_thread_data.id,
                assistant_id=primary_assistant_id,
                initial_message=latest_response_from_secondary_assistant
            )

            # Wait for the response
            if not await poll_for_completion_util(secondary_primary_chat_thread_data.id, secondary_to_primary_run.id):
                return {"message": "Error in completing the second chat"}
            
            secondary_to_primary_messages = await get_assistant_messages_util(secondary_primary_chat_thread_data.id)            
            latest_response_from_primary_assistant = secondary_to_primary_messages[0]
            
            # Append primary's response to the conversation
            conversation.append({"sender": sender_name_primary, "message": latest_response_from_primary_assistant})

            if chat_end in latest_response_from_primary_assistant:
                # Send a new message to the secondary assistant asking for the final output
                final_output_request = output_format_instructions + " - " + output_request
                
                # Append Primary Assistant response to the conversation
                conversation.append({"sender": sender_name_primary, "message": final_output_request})
                
                request_to_secondary_for_output = await send_initial_message_util(
                    thread_id=primary_secondary_chat_thread_data.id,
                    assistant_id=secondary_assistant_id,
                    initial_message=final_output_request
                )

                # Wait for the response
                if not await poll_for_completion_util(primary_secondary_chat_thread_data.id, request_to_secondary_for_output.id):
                    return {"message": "Error in requesting final output"}

                final_output_messages = await get_assistant_messages_util(primary_secondary_chat_thread_data.id)
                final_output_from_secondary = final_output_messages[0]

                # Append Primary Assistant response to the conversation
                conversation.append({"sender": sender_name_secondary, "message": final_output_from_secondary})
                
                # Directly use the response as the final output
                output_content = final_output_from_secondary.strip()
                if(chat_type == "stakeholder_consultant"):
                    await save_project_idea_final_util(project_id=id, final_idea=output_content)
                elif(chat_type == "stakeholder_ceo"):
                    await save_project_company_goal_util(project_id=id, company_goal=output_content)
                if chat_type in ["ceo_cpo", "ceo_cto"]:
                    await save_markdown_to_file_util(project_id=id, chat_name=request_body.chat_name, markdown_content=output_content) 
            
                break
            
            # Increment the exchange count
            current_exchanges += 1
        
        # Save the conversation in the database
        await save_conversation_util(chat_id=chat_id, conversation=conversation)
        
        # Save the conversation to a JSON file
        success = await save_conversation_to_file_util(project_id=id, chat_name=request_body.chat_name, conversation=conversation)
        if not success:
            # Handle the error case as needed
            raise HTTPException(status_code=500, detail="Error saving conversation to file")
        
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