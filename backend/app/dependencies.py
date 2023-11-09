from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from openai import OpenAI

def configure_openai_client(app: FastAPI):
    # CORS middleware configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.public_frontend_url],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # OpenAI client configuration
    if settings.running_tests:
        app.state.openai_client = None
    else:
        app.state.openai_client = OpenAI(api_key=settings.openai_api_key)

# This function can be used to retrieve the client in route handlers

def get_openai_client(request: Request):
    if not hasattr(request.app.state, "openai_client"):
        # Only configure the client if it's not already configured
        request.app.state.openai_client = OpenAI(api_key=settings.openai_api_key) if not settings.running_tests else None
    return request.app.state.openai_client
