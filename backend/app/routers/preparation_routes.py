from fastapi import APIRouter

router = APIRouter()

@router.post("/start")
async def start_preparation(id: int):
    return {"message": "Start Preparation Phase for project!"}

@router.get("/idea")
async def get_idea(id: int):
    return {"id": id, "idea_initial": "This is the initial idea!"}

@router.post("/stakeholder-assistant")
async def create_stakeholder_assistant(id: int):
    return {"message": "Stakeholder Assistant Created Successfully for project!"}

@router.post("/consultant-assistant")
async def create_consultant_assistant(id: int):
    return {"message": "Consultant Assistant Created Successfully for project!"}

@router.get("/done")
async def finish_preparation(id: int):
    return {"message": "Preparation Phase Done for project!"}
