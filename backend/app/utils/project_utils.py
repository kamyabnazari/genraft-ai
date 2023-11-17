from fastapi import HTTPException
from app.models.database import projects
from app.dependencies import get_database
from sqlalchemy import select

database = get_database()

async def get_project_folder_path_util(project_id: int):
    query = select([projects.c.folder_path]).where(projects.c.id == project_id)
    result = await database.fetch_one(query)
    if result:
        return result['folder_path']
    else:
        raise HTTPException(status_code=404, detail=f"Project with id {project_id} not found")

async def get_project_idea_initial_util(project_id: int):
    query = select([projects.c.idea_initial]).where(projects.c.id == project_id)
    result = await database.fetch_one(query)
    if result:
        return result['idea_initial']
    else:
        raise HTTPException(status_code=404, detail=f"Project with id {project_id} not found")