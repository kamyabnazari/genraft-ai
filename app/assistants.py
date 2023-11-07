from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenAI API key
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI Client with the API key
client = OpenAI()

def create_assistant():
    response = client.beta.assistants.create(
        name="Math Tutor",
        instructions="You are a personal math tutor. Write and run code to answer math questions.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-1106-preview"
    )
    return response

def create_thread():
    response = client.beta.threads.create()
    return response

def add_message_to_thread(thread_id, user_message):
    response = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_message
    )
    return response

def run_assistant(thread_id, assistant_id, instructions=None):
    response = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions=instructions
    )
    return response

def get_assistant_response(thread_id, run_id):
    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )
    if run_status['status'] == 'completed':
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        return messages
    else:
        return None
