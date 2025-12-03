from fastapi import APIRouter
from .routes import auth

api_router = APIRouter()

# Simple health check
@api_router.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}

# Authentication routes
api_router.include_router(auth.router)