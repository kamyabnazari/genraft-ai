import os

# Importing fastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

# Importing openai
from openai import OpenAI

# Other imports
from dotenv import load_dotenv

load_dotenv()

frontend_public_url = os.getenv("PUBLIC_FRONTEND_URL", "http://default-frontend-url")
openai_api_key = os.getenv("OPENAI_API_KEY", 'default-openai-api-key')

running_tests_str = os.getenv('RUNNING_TESTS', 'false')
running_tests_bool = running_tests_str.lower() == 'true'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_public_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_openai_model():
    if running_tests_bool:
        print("Skipping model creation during tests.")
        return None
    
    # Create OpenAI model with retries
    client = OpenAI(api_key=openai_api_key)

    # If the above code executes successfully, return the OpenAI Client
    return client

# use the v LLM   
openai_model = create_openai_model() 

@app.get("/")
async def read_root():
    return {"message": "This is the backend for Genraft AI Project!"}

@app.get("/favicon.ico")
async def read_favicon():
    return FileResponse("favicon.ico", media_type="image/vnd.microsoft.icon")

@app.get("/health")
async def health_check():
    return {"status": "OK"}

@app.get("/api")
async def read_api_root():
    return {"message": "Welcome to the Genraft AI API!"}