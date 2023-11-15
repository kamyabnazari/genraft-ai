from fastapi import APIRouter

router = APIRouter()

@router.post("/start")
async def start_idea_creation(id: int):
    return {"message": "Start Idea Creation Phase for project!"}

@router.get("/idea")
async def get_idea(id: int):
    return {"id": id, "idea_initial": "Initial idea in Idea Creation Phase!"}

@router.post("/chat-stakeholder-consultant")
async def chat_with_stakeholder_and_consultant(id: int):
    return {"message": "Chat between stakeholder and consultant concluded for project!"}

@router.get("/result")
async def get_idea_creation_result(id: int):
    return {"id": id, "idea_final": "Final idea in Idea Creation Phase!"}

@router.get("/done")
async def finish_idea_creation(id: int):
    return {"message": "Idea Creation Phase Done for project!"}
