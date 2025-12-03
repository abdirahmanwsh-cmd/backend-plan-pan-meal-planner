from fastapi import FastAPI
from app.api.api import api_router
from app.db.database import Base, engine
# Import models so SQLAlchemy knows about them
from app import models  # noqa: F401  (used for side effects)

app = FastAPI()

app.include_router(api_router)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)