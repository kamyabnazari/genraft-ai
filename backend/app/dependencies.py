# This file can be simplified since you don't need to configure the OpenAI client anymore.

from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

def configure_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.public_frontend_url],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )