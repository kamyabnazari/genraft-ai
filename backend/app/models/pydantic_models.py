from pydantic import BaseModel

class GenerateMessageRequest(BaseModel):
    prompt: str

class GenerateAssistantRequest(BaseModel):
    name: str
    instructions: str
    initial_message: str