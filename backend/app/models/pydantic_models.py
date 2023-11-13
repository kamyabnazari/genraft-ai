from pydantic import BaseModel
from datetime import datetime

class Project(BaseModel):
    id: int
    name: str
    idea_initial: str
    idea_final: str
    folder_path: str
    created_at: datetime

class ProjectStats(BaseModel):
    total_projects: int
    total_files: int
    total_assets: int

class InitializeProjectRequest(BaseModel):
    name: str
    idea: str

class GenerateAssistantRequest(BaseModel):
    name: str
    instructions: str
    initial_message: str