from fastapi import FastAPI
from app.routers import root, project_routes, stats_routes, assistants_routes
from app.dependencies import configure_cors, lifespan

app = FastAPI(title="Genraft AI Project Backend", lifespan=lifespan)

# Configure CORS
configure_cors(app)

app.include_router(root.router)
app.include_router(stats_routes.router, prefix="/api/stats")
app.include_router(project_routes.router, prefix="/api/projects")
app.include_router(assistants_routes.router, prefix="/api/projects/{id}/assistants")