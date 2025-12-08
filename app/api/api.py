from fastapi import APIRouter
from app.api.routes import auth, meals, plans

api_router = APIRouter()

# Health is in main.py, leave it there

# Auth endpoints -> /auth/...
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

# Meals endpoints -> /meals/...
api_router.include_router(meals.router, tags=["meals"])  # NO prefix here

# Plans endpoints -> /plans/... 
api_router.include_router(plans.router, tags=["plans"])  # NO prefix here
