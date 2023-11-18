import json
from openai import OpenAI, OpenAIError
from app.core.config import settings
from app.models.database import chats, project_chat_association
from app.dependencies import get_database
from sqlalchemy import select
import time
import datetime

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

async def poll_for_completion_util(thread_id, run_id, timeout=60):
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

async def delete_project_chats_util(project_id: int):
    try:
        # Retrieve chat thread IDs associated with the project
        chat_thread_ids = await get_project_openai_chat_thread_ids_util(project_id)

        # Delete each chat thread from OpenAI
        for chat_thread_id in chat_thread_ids:
            client.beta.threads.delete(thread_id=chat_thread_id)

        # Delete chat associations from the database
        delete_association_query = project_chat_association.delete().where(
            project_chat_association.c.project_id == project_id
        )
        await database.execute(delete_association_query)

        # Delete chats from the database
        delete_chats_query = chats.delete().where(
            chats.c.chat_thread_id.in_(chat_thread_ids)
        )
        await database.execute(delete_chats_query)

        return {"message": f"All chats associated with project {project_id} have been deleted"}
    except Exception as e:
        raise e

# Function to insert chat data into the database
async def insert_chat_data_util(chat_thread_id, chat_name, chat_assistant_primary, chat_assistant_secondary, chat_goal):
    chat_query = chats.insert().values(
        chat_thread_id=chat_thread_id,
        chat_name=chat_name,
        chat_assistant_primary=chat_assistant_primary,
        chat_assistant_secondary=chat_assistant_secondary,
        chat_goal=chat_goal,
        created_at=datetime.datetime.now()
    )
    chat_id = await database.execute(chat_query)
    return chat_id

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

# Function to associate chat with a project
async def associate_chat_with_project_util(project_id, chat_id):
    association_query = project_chat_association.insert().values(
        project_id=project_id,
        chat_id=chat_id
    )
    await database.execute(association_query)

async def chat_thread_exists_util(primary_to_secondary_name: str, secondary_to_primary_name: str):
    query = chats.select().where(
        (chats.c.chat_name == primary_to_secondary_name) | 
        (chats.c.chat_name == secondary_to_primary_name)
    )
    result = await database.fetch_one(query)
    return result is not None

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
