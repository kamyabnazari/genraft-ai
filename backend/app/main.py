from fastapi import FastAPI
from app.routers import root, project_routes, stats_routes, assistant_routes, preparation_routes, idea_creation_routes
from app.dependencies import configure_cors, lifespan

app = FastAPI(title="Genraft AI Project Backend", lifespan=lifespan)

# Configure CORS
configure_cors(app)

app.include_router(root.router)
app.include_router(stats_routes.router, prefix="/api/stats")
app.include_router(assistant_routes.router, prefix="/api/assistants")
app.include_router(project_routes.router, prefix="/api/projects")
app.include_router(preparation_routes.router, prefix="/api/projects/{id}/preparation")
app.include_router(idea_creation_routes.router, prefix="/api/projects/{id}/idea-creation")