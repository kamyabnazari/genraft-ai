from openai import OpenAI, OpenAIError
from app.core.config import settings
from app.models.database import assistants, project_assistant_association
from app.dependencies import get_database
from sqlalchemy import select
import time
import datetime

client = OpenAI(api_key=settings.openai_api_key)
database = get_database()

async def create_new_assistant(name, instructions, model):
    try:
        return client.beta.assistants.create(
            name=name,
            instructions=instructions,
            tools=[{"type": "code_interpreter"}],
            model=model
        )
    except OpenAIError as e:
        raise e

async def create_thread():
    try:
        return client.beta.threads.create()
    except OpenAIError as e:
        raise e

async def send_initial_message(thread_id, assistant_id, initial_message):
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

async def get_assistant_messages(thread_id):
    try:
        messages_response = client.beta.threads.messages.list(thread_id=thread_id)
        return [
            cp.text.value for msg in messages_response.data if msg.role == "assistant"
            for cp in msg.content if cp.type == 'text' and hasattr(cp, 'text')
        ]
    except OpenAIError as e:
        raise e

async def delete_project_assistants(project_id: int):
    try:
        # Retrieve assistant IDs associated with the project
        assistant_ids = await get_project_openai_assistant_ids(project_id)

        # Delete each assistant from OpenAI
        for assistant_id in assistant_ids:
            client.beta.assistants.delete(assistant_id=assistant_id)

        # Delete assistant associations from the database
        delete_association_query = project_assistant_association.delete().where(
            project_assistant_association.c.project_id == project_id
        )
        await database.execute(delete_association_query)

        # Delete assistants from the database
        delete_assistants_query = assistants.delete().where(
            assistants.c.assistant_id.in_(assistant_ids)
        )
        await database.execute(delete_assistants_query)

        return {"message": f"All assistants associated with project {project_id} have been deleted"}
    except Exception as e:
        raise e

# Function to insert assistant data into the database
async def insert_assistant_data(assistant_id, assistant_name, assistant_type, assistant_instructions, assistant_model):
    assistant_query = assistants.insert().values(
        assistant_id=assistant_id,
        assistant_name=assistant_name,
        assistant_type=assistant_type,
        assistant_instructions=assistant_instructions,
        assistant_model=assistant_model,
        created_at=datetime.datetime.now()
    )
    assistant_id = await database.execute(assistant_query)
    return assistant_id

# Function to associate assistant with a project
async def associate_assistant_with_project(project_id, assistant_id):
    association_query = project_assistant_association.insert().values(
        project_id=project_id,
        assistant_id=assistant_id
    )
    await database.execute(association_query)

async def assistant_exists(name: str, assistant_type: str):
    query = assistants.select().where(
        (assistants.c.assistant_name == name) & (assistants.c.assistant_type == assistant_type)
    )
    result = await database.fetch_one(query)
    return result is not None

async def get_project_openai_assistant_ids(project_id: int):
    # Define a SQL query to join project_assistant_association with assistants
    # to fetch the OpenAI assistant IDs (assistant_id from assistants table)
    join_query = select([
        assistants.c.assistant_id
    ]).select_from(
        project_assistant_association.join(assistants, project_assistant_association.c.assistant_id == assistants.c.id)
    ).where(
        project_assistant_association.c.project_id == project_id
    )

    # Execute the query and fetch results
    result = await database.fetch_all(join_query)
    return [row['assistant_id'] for row in result]
