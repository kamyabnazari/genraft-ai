from pydantic import BaseModel

class StepIdeaSubmitRequest(BaseModel):
    name: str
    idea: str

class GenerateAssistantRequest(BaseModel):
    name: str
    instructions: str
    initial_message: str