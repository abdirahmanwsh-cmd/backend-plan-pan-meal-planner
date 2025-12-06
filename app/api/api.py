from fastapi import APIRouter
from .routes import auth, meals, plans

api_router = APIRouter()

# Health check
@api_router.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}

# Auth endpoints
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

# Meal CRUD endpoints
api_router.include_router(meals.router, prefix="/meals", tags=["meals"])

# Weekly plans, slots, shopping list
api_router.include_router(plans.router, prefix="/plans", tags=["plans"])