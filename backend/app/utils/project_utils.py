from fastapi import HTTPException
from app.models.database import projects
from app.dependencies import get_database
from sqlalchemy import select, update

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

async def get_project_idea_final_util(project_id: int):
    query = select([projects.c.idea_final]).where(projects.c.id == project_id)
    result = await database.fetch_one(query)
    if result:
        return result['idea_final']
    else:
        raise HTTPException(status_code=404, detail=f"Project with id {project_id} not found")

async def get_project_technical_plan_util(project_id: int):
    query = select([projects.c.technical_plan]).where(projects.c.id == project_id)
    result = await database.fetch_one(query)
    if result:
        return result['technical_plan']
    else:
        raise HTTPException(status_code=404, detail=f"Project with id {project_id} not found")

async def save_project_idea_final_util(project_id: int, final_idea: str):
    query = update(projects).where(projects.c.id == project_id).values(idea_final=final_idea)
    await database.execute(query)

async def save_project_technical_plan_util(project_id: int, technical_plan: str):
    query = update(projects).where(projects.c.id == project_id).values(technical_plan=technical_plan)
    await database.execute(query)