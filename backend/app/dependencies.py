from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from databases import Database

DATABASE_URL = "sqlite:///./mydatabase.db"
database = Database(DATABASE_URL)

@asynccontextmanager
async def lifespan(app):
    # Startup logic: connect to the database
    await database.connect()
    yield
    # Shutdown logic: disconnect from the database
    await database.disconnect()

def configure_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.public_frontend_url],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def get_database():
    return database