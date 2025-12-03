from fastapi import FastAPI

from .db.database import Base, engine
from .api.api import api_router

# Create DB tables (for development / MVP)
Base.metadata.create_all(bind=engine)

# THIS is what uvicorn is looking for:
app = FastAPI(title="FitPlate API")

# Include our API router
app.include_router(api_router)