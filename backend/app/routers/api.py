from fastapi import APIRouter, Depends, HTTPException
from app.models.pydantic_models import GenerateMessageRequest
from openai import OpenAI
from app.dependencies import get_openai_client

router = APIRouter()

@router.get("/")
async def read_api_root():
    return {"message": "Welcome to the Genraft AI API!"}

@router.post("/generate_message")
async def generate_message(request_body: GenerateMessageRequest, openai_client: OpenAI = Depends(get_openai_client)):
    if openai_client is None:
        raise HTTPException(status_code=503, detail="OpenAI client not available")
    
    try:
        response = openai_client.Completion.create(
            model="text-davinci-003",
            prompt=request_body.prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))