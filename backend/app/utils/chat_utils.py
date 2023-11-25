import json
from syslog import LOG_PERROR
from fastapi import HTTPException
from openai import OpenAI, OpenAIError
from app.utils.project_utils import get_project_idea_final_util
from app.utils.project_utils import get_project_idea_initial_util
from app.core.config import settings
from app.models.database import chats, threads, project_chat_association, chat_thread_association
from app.dependencies import get_database
from sqlalchemy import select
import time
import datetime
from app.utils.file_utils import save_python_to_file_util
from app.utils.project_utils import (
    get_project_company_goal_util,
    get_project_design_strategy_util,
    get_project_technical_plan_util,
    save_project_company_goal_util,
    save_project_design_strategy_util,
    save_project_idea_final_util,
    save_project_technical_plan_util
    )

client = OpenAI(api_key=settings.openai_api_key)
database = get_database()

async def create_chat_thread_util():
    try:
        return client.beta.threads.create()
    except OpenAIError as e:
        raise e

async def send_initial_message_util(thread_id, assistant_id, initial_message):
    try:
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=initial_message
        )
        return client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
    except OpenAIError as e:
        raise e

async def poll_for_completion_util(thread_id, run_id, timeout=300):
    start_time = time.time()
    while time.time() - start_time < timeout:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run_status.status == "completed":
            return True
        elif run_status.status in ["failed", "cancelled", "expired"]:
            return False
        time.sleep(1)
    return False

async def get_assistant_messages_util(thread_id):
    try:
        messages_response = client.beta.threads.messages.list(thread_id=thread_id)
        assistant_messages = []
        
        for msg in messages_response.data:
            if msg.role == "assistant":
                for cp in msg.content:
                    if cp.type == 'text' and hasattr(cp, 'text'):
                        assistant_messages.append(cp.text.value)

        return assistant_messages
    except OpenAIError as e:
        raise e

async def delete_project_chats_util(project_id: int):
    try:
        # Retrieve chat IDs associated with the project
        chat_ids_query = project_chat_association.select().where(
            project_chat_association.c.project_id == project_id
        )
        chat_ids = await database.fetch_all(chat_ids_query)

        # Retrieve thread associations associated with each chat
        for chat in chat_ids:
            thread_associations_query = chat_thread_association.select().where(
                chat_thread_association.c.chat_id == chat['chat_id']
            )
            thread_associations = await database.fetch_all(thread_associations_query)

            # Delete each thread from OpenAI and database using the OpenAI thread_id
            for association in thread_associations:
                # Retrieve the actual OpenAI thread_id from the threads table
                thread_query = threads.select().where(
                    threads.c.id == association['thread_id']
                )
                thread = await database.fetch_one(thread_query)

                if thread:
                    # Use the OpenAI API to delete the thread
                    client.beta.threads.delete(thread_id=thread['thread_id'])

                    # Delete thread from database
                    delete_thread_query = threads.delete().where(
                        threads.c.id == association['thread_id']
                    )
                    await database.execute(delete_thread_query)

            # Delete the associations from database
            delete_thread_association_query = chat_thread_association.delete().where(
                chat_thread_association.c.chat_id == chat['chat_id']
            )
            await database.execute(delete_thread_association_query)

        # Delete chat associations from the database
        delete_chat_association_query = project_chat_association.delete().where(
            project_chat_association.c.project_id == project_id
        )
        await database.execute(delete_chat_association_query)

        # Delete chats from the database
        delete_chats_query = chats.delete().where(
            chats.c.id.in_([chat['chat_id'] for chat in chat_ids])
        )
        await database.execute(delete_chats_query)

        return {"message": f"All chats and associated threads for project {project_id} have been deleted"}
    except Exception as e:
        raise e

async def delete_specific_chat_and_threads(chat_id: int):
    try:
        # Retrieve thread associations with the specific chat
        thread_associations_query = chat_thread_association.select().where(
            chat_thread_association.c.chat_id == chat_id
        )
        thread_associations = await database.fetch_all(thread_associations_query)

        # Delete each thread from OpenAI and database using the OpenAI thread_id
        for association in thread_associations:
            # Retrieve the OpenAI thread_id from the threads table
            thread_query = threads.select().where(
                threads.c.id == association['thread_id']
            )
            thread = await database.fetch_one(thread_query)

            if thread:
                # Use the OpenAI API to delete the thread
                client.beta.threads.delete(thread_id=thread['thread_id'])

                # Delete thread from database
                delete_thread_query = threads.delete().where(
                    threads.c.id == association['thread_id']
                )
                await database.execute(delete_thread_query)

        # Delete the chat threads associations from database
        delete_association_query = chat_thread_association.delete().where(
            chat_thread_association.c.chat_id == chat_id
        )
        await database.execute(delete_association_query)

        # Delete project chat associations from the database
        delete_chat_association_query = project_chat_association.delete().where(
            project_chat_association.c.chat_id == chat_id
        )
        await database.execute(delete_chat_association_query)

        # Delete the specific chat from the database
        delete_chat_query = chats.delete().where(
            chats.c.id == chat_id
        )
        await database.execute(delete_chat_query)

        return {"message": f"Chat with ID {chat_id} and associated threads have been deleted"}
    except Exception as e:
        raise e

async def save_conversation_util(chat_id, conversation):
    try:
        update_query = chats.update().where(
            chats.c.id == chat_id
        ).values(
            chat_messages=json.dumps(conversation)
        )
        await database.execute(update_query)
    except Exception as e:
        raise e

async def fetch_conversation_util(chat_id: int):
    try:
        query = select([chats.c.chat_messages]).where(chats.c.id == chat_id)
        result = await database.fetch_one(query)
        if result:
            return json.loads(result['chat_messages'])
        else:
            return None
    except Exception as e:
        raise e

async def get_project_openai_chat_thread_ids_util(project_id: int):
    # Define a SQL query to join project_chat_association with chats
    # to fetch the OpenAI chat IDs (chat_id from chats table)
    join_query = select([
        chats.c.chat_thread_id
    ]).select_from(
        project_chat_association.join(chats, project_chat_association.c.chat_id == chats.c.id)
    ).where(
        project_chat_association.c.project_id == project_id
    )

    # Execute the query and fetch results
    result = await database.fetch_all(join_query)
    return [row['chat_thread_id'] for row in result]

async def chat_thread_exists_util(chat_name: str, primary_to_secondary_name: str, secondary_to_primary_name: str):
    # Check if the chat exists
    chat_query = chats.select().where(
        chats.c.chat_name == chat_name
    )
    chat_result = await database.fetch_one(chat_query)

    if chat_result:
        return True, chat_result['id']  # Return True and the found chat_id

    # Check if the threads exist
    thread_query = threads.select().where(
        (threads.c.thread_name == primary_to_secondary_name) | 
        (threads.c.thread_name == secondary_to_primary_name)
    )
    thread_exists = await database.fetch_one(thread_query) is not None

    return thread_exists, None  # Return False and None if no chat_id is found

async def insert_chat_data_util(chat_name, chat_assistant_primary, chat_assistant_secondary, chat_messages):
    chat_query = chats.insert().values(
        chat_name=chat_name,
        chat_assistant_primary=chat_assistant_primary,
        chat_assistant_secondary=chat_assistant_secondary,
        chat_messages=json.dumps(chat_messages),
        created_at=datetime.datetime.now()
    )
    chat_id = await database.execute(chat_query)
    return chat_id

async def insert_thread_data_util(thread_id, thread_name):
    thread_query = threads.insert().values(
        thread_id=thread_id,
        thread_name=thread_name,
        created_at=datetime.datetime.now()
    )
    thread_db_id = await database.execute(thread_query)
    return thread_db_id

async def associate_chat_with_project_util(project_id, chat_id):
    association_query = project_chat_association.insert().values(
        project_id=project_id,
        chat_id=chat_id
    )
    await database.execute(association_query)

async def associate_thread_with_chat_util(chat_id, thread_id):
    association_query = chat_thread_association.insert().values(
        chat_id=chat_id,
        thread_id=thread_id
    )
    await database.execute(association_query)

async def list_thread_messages(thread_id):
    try:
        return client.beta.threads.messages.list(thread_id=thread_id)
    except OpenAIError as e:
        raise e

async def retrieve_message_file(thread_id, message_id, file_id):
    try:
        return client.beta.threads.messages.files.retrieve(thread_id=thread_id, message_id=message_id, file_id=file_id)
    except OpenAIError as e:
        raise e

async def format_initial_message(chat_type, template, id, tech_scope, chat_goal, max_exchanges, chat_end, response_from_secondary_assistant):
    try:
        idea_initial, idea_final, company_goal, design_strategy, technical_plan  = None, None, None, None, None

        if chat_type in ["stakeholder_consultant", "stakeholder_ceo"]:
            idea_initial = await get_project_idea_initial_util(id)
        if chat_type in ["stakeholder_ceo", "ceo_cpo"]:
            idea_final = await get_project_idea_final_util(id)
        if chat_type in ["ceo_cpo"]:
            company_goal = await get_project_company_goal_util(id)
        if chat_type in ["ceo_cto"]:
            design_strategy = await get_project_design_strategy_util(id)
        if chat_type in ["cto_programmer"]:
            technical_plan = await get_project_technical_plan_util(id)

        return template.format(
            tech_scope=tech_scope,
            chat_goal=chat_goal,
            idea_initial=idea_initial,
            idea_final=idea_final,
            company_goal=company_goal,
            design_strategy=design_strategy,
            technical_plan=technical_plan,
            max_exchanges=max_exchanges,
            chat_end=chat_end,
            response_from_secondary=response_from_secondary_assistant
        )
    except Exception as e:
        # Log the error for debugging
        LOG_PERROR("Error in formatting message: " + str(e))
        return None

async def request_and_process_final_output(project_id,
                                           chat_type,
                                           request_body,
                                           primary_secondary_chat_thread_data,
                                           secondary_assistant_id,
                                           output_format_instructions,
                                           output_request,
                                           conversation,
                                           sender_name_primary,
                                           sender_name_secondary
                                           ):
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
        raise HTTPException(status_code=500, detail="Error: In requesting final output")

    final_output_messages = await get_assistant_messages_util(primary_secondary_chat_thread_data.id)
    final_output_from_secondary = final_output_messages[0]

    # Append Secondary Assistant response to the conversation
    conversation.append({"sender": sender_name_secondary, "message": final_output_from_secondary})
    
    # Directly use the response as the final output
    output_content = final_output_from_secondary.strip()

    # Save the output based on the chat type
    if chat_type == "stakeholder_consultant":
        await save_project_idea_final_util(project_id=project_id, final_idea=output_content)
    elif chat_type == "stakeholder_ceo":
        await save_project_company_goal_util(project_id=project_id, company_goal=output_content)
    elif chat_type == "ceo_cpo":
        await save_project_design_strategy_util(project_id=project_id, design_strategy=output_content)
    elif chat_type == "ceo_cto":
        await save_project_technical_plan_util(project_id=project_id, technical_plan=output_content)
    elif chat_type == "cto_programmer":
        await save_python_to_file_util(project_id=project_id, chat_name=request_body.chat_name, output_content=output_content)
    elif chat_type == "programmer_designer":
        print(output_content)

    return True
