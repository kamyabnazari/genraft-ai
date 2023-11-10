from fastapi import APIRouter, HTTPException
from app.models.pydantic_models import StepIdeaSubmitRequest, GenerateAssistantRequest
from app.models.database import projects
from app.dependencies import get_database
from app.core.config import settings
from openai import OpenAI, OpenAIError
import json
import time

router = APIRouter()
client = OpenAI(api_key=settings.openai_api_key)

@router.get("/")
async def read_api_root():
    return {"message": "Welcome to the Genraft AI API!"}

@router.post("/step_idea_submit")
async def generate_message(request_body: StepIdeaSubmitRequest):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request_body.idea}]
        )
        generated_message = chat_completion.choices[0].message.content

        # Database action
        query = projects.insert().values(
            name="Example Project Name",
            idea_initial=request_body.idea,
            idea_final=generated_message,
            chat_history_idea="History in JSON"
        )
        await get_database().execute(query)

        return {"message": generated_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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

@router.post("/generate_assistant")
async def generate_assistant(request_body: GenerateAssistantRequest):
    try:
        assistant = client.beta.assistants.create(
            name=request_body.name,
            instructions=request_body.instructions,
            tools=[{"type": "code_interpreter"}],
            model="gpt-3.5-turbo"
        )
        thread = client.beta.threads.create()
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=request_body.initial_message
        )
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )
        if not await poll_for_completion(thread.id, run.id):
            raise HTTPException(status_code=500, detail="Assistant run did not complete in time.")

        messages_response = client.beta.threads.messages.list(thread_id=thread.id)
        assistant_messages = [
            cp.text.value for msg in messages_response.data if msg.role == "assistant"
            for cp in msg.content if cp.type == 'text' and hasattr(cp, 'text')
        ]
        return {"messages": assistant_messages}
    except OpenAIError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
