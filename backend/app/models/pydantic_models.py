from pydantic import BaseModel

class StepIdeaSubmitRequest(BaseModel):
    name: str
    idea: str

class GenerateAssistantRequest(BaseModel):
    name: str
    instructions: str
    initial_message: str

class ProjectStats(BaseModel):
    total_projects: int
    total_files: int
    total_assets: int