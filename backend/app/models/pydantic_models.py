from pydantic import BaseModel
from datetime import datetime

class Project(BaseModel):
    id: int
    name: str
    idea_initial: str
    idea_final: str
    company_goal: str
    design_strategy: str
    technical_plan: str
    folder_path: str
    created_at: datetime
    current_phase: str | None
    current_stage: str | None

class Assistant(BaseModel):
    id: int
    assistant_id: str
    assistant_name: str
    assistant_type: str
    assistant_instructions: str
    assistant_model: str
    created_at: datetime

class ProjectAssistantAssociation(BaseModel):
    project_id: int
    assistant_id: int

class ProjectChatAssociation(BaseModel):
    project_id: int
    chat_message_id: int
    chat_type: str

class ProjectStats(BaseModel):
    total_projects: int
    total_files: int
    total_assets: int

class InitializeProjectRequest(BaseModel):
    name: str
    idea: str

class CreateAssistantRequest(BaseModel):
    assistant_name: str
    assistant_type: str
    assistant_model: str

class CreateChatRequest(BaseModel):
    chat_name: str
    chat_assistant_primary: str
    chat_assistant_secondary: str

class UpdateProgressRequest(BaseModel):
    current_phase: str
    current_stage: str