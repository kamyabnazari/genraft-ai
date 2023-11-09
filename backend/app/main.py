from fastapi import FastAPI
from app.core.config import settings
from app.routers import root, api
from app.dependencies import configure_openai_client
from app.dependencies import get_openai_client

app = FastAPI(title="Genraft AI Project Backend")

# Configurations like CORS can be abstracted into a separate function if desired
# This setup assumes CORS settings and other middlewares are defined in app/dependencies.py
configure_openai_client(app)

app.include_router(root.router)
app.include_router(api.router, prefix="/api")