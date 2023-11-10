from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from databases import Database
import logging
import os

# Create the Genraft AI data folder
folder_path = './genraft_ai_data'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Create database instance
DATABASE_URL = "sqlite:///./genraft_ai_data/genraftai.db"
database = Database(DATABASE_URL)

# Connect to the database instance and create the .db file
@asynccontextmanager
async def lifespan(app):
    try:
        # Startup logic: connect to the database
        await database.connect()
        query = "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)"
        await database.execute(query)
    except Exception as e:
        logging.error(f"Failed to connect to the database: {e}")
        raise
    yield
    try:
        # Shutdown logic: disconnect from the database
        await database.disconnect()
    except Exception as e:
        logging.error(f"Failed to disconnect from the database: {e}")
        raise

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