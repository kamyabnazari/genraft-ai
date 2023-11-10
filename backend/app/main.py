from fastapi import FastAPI
from app.core.config import settings
from app.routers import root, api
from app.dependencies import configure_cors, lifespan

app = FastAPI(title="Genraft AI Project Backend", lifespan=lifespan)

# Configure CORS
configure_cors(app)

app.include_router(root.router)
app.include_router(api.router, prefix="/api")