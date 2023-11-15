from pydantic import BaseModel
from datetime import datetime

class Project(BaseModel):
    id: int
    name: str
    idea_initial: str
    idea_final: str
    folder_path: str
    created_at: datetime

class ChatMessage(BaseModel):
    id: int
    thread_id: str
    content: str
    role: str
    created_at: datetime

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

class GenerateAssistantRequest(BaseModel):
    name: str
    instructions: str
    initial_message: str