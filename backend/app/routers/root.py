from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "This is the backend for Genraft AI Project!"}

@router.get("/favicon.ico")
async def read_favicon():
    return FileResponse("favicon.ico", media_type="image/vnd.microsoft.icon")

@router.get("/health")
async def health_check():
    return {"status": "OK"}
