from fastapi import APIRouter, HTTPException
from app.utils.assistant_utils import create_assistant
from app.models.database import assistants, project_assistant_association
from app.dependencies import get_database
from datetime import datetime

router = APIRouter()
database = get_database()

@router.post("/start")
async def start_preparation(id: int):
    return {"message": "Start Preparation Phase for project!"}

@router.get("/idea")
async def get_idea(id: int):
    return {"id": id, "idea_initial": "This is the initial idea!"}

@router.post("/stakeholder-assistant")
async def create_stakeholder_assistant(id: int):
    try:
        # Create an assistant using the utility function
        assistant_data = await create_assistant("Stakeholder Assistant", "You are a stakeholder for a software company that creates fiancial software.")
        
        # Insert the assistant data into the assistants table
        assistant_query = assistants.insert().values(
            assistant_id=assistant_data.id,
            type="stakeholder",
            created_at=datetime.now()
        )
        assistant_id = await database.execute(assistant_query)

        # Associate the assistant with the project
        association_query = project_assistant_association.insert().values(
            project_id=id,
            assistant_id=assistant_id
        )
        await database.execute(association_query)

        return {"message": "Stakeholder Assistant Created Successfully for project", "assistant_id": assistant_data.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/consultant-assistant")
async def create_consultant_assistant(id: int):
    return {"message": "Consultant Assistant Created Successfully for project!"}

@router.get("/done")
async def finish_preparation(id: int):
    return {"message": "Preparation Phase Done for project!"}
