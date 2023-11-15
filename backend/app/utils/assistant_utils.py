from openai import OpenAI, OpenAIError
from app.core.config import settings
import time

client = OpenAI(api_key=settings.openai_api_key)

async def create_assistant(name, instructions):
    try:
        return client.beta.assistants.create(
            name=name,
            instructions=instructions,
            tools=[{"type": "code_interpreter"}],
            model="gpt-3.5-turbo"
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
