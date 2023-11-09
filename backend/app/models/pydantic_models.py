from pydantic import BaseModel

class GenerateMessageRequest(BaseModel):
    prompt: str
