from fastapi import APIRouter, HTTPException
from app.models.pydantic_models import GenerateMessageRequest, GenerateAssistantRequest
from openai import OpenAI
from app.core.config import settings
import time

router = APIRouter()

client = OpenAI(api_key=settings.openai_api_key)

@router.get("/")
async def read_api_root():
    return {"message": "Welcome to the Genraft AI API!"}

@router.post("/generate_message")
async def generate_message(request_body: GenerateMessageRequest):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request_body.prompt}]
        )
        return {"message": chat_completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate_assistant")
async def generate_assistant(request_body: GenerateAssistantRequest):
    try:
        # Step 1: Create an Assistant
        assistant = client.beta.assistants.create(
            name=request_body.name,
            instructions=request_body.instructions,
            tools=[{"type": "code_interpreter"}],
            model="gpt-3.5-turbo"
        )

        # Step 2: Create a Thread
        thread = client.beta.threads.create()

        # Step 3: Add a Message to a Thread
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=request_body.initial_message
        )

        # Step 4: Run the Assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )

        # Step 5: Poll for the run completion and retrieve messages
        while True:
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run_status.status == "completed":
                break
            time.sleep(1)  # Sleep to avoid rate limits

        # Retrieve messages after the run is completed
        messages_response = client.beta.threads.messages.list(
            thread_id=thread.id
        )

        # Extract the Assistant's messages
        assistant_messages = [
            content_piece.text.value
            for message in messages_response.data
            if message.role == "assistant"
            for content_piece in message.content
            if content_piece.type == 'text' and hasattr(content_piece, 'text')
        ]

        return {"messages": assistant_messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))