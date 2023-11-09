from fastapi import APIRouter, HTTPException
from app.models.pydantic_models import GenerateMessageRequest
from openai import OpenAI
from app.core.config import settings

router = APIRouter()

@router.get("/")
async def read_api_root():
    return {"message": "Welcome to the Genraft AI API!"}

@router.post("/generate_message")
async def generate_message(request_body: GenerateMessageRequest):
    client = OpenAI(api_key=settings.openai_api_key)
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request_body.prompt}]
        )
        return {"message": chat_completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

