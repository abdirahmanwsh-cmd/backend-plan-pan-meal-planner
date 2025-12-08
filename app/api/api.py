from fastapi import APIRouter
from app.api.routes import auth, meals, plans

api_router = APIRouter()

# Root fallback so '/' returns content (useful for Render health checks)
@api_router.get("/", include_in_schema=False)
def root_health():
	return {"status": "ok", "service": "FitPlate API"}

# Auth endpoints -> /auth/...
# Note: auth.router already has prefix="/auth" defined, so don't add prefix here
api_router.include_router(auth.router, tags=["auth"])

# Meals endpoints -> /meals/...
# Note: meals.router already has prefix="/meals" defined
api_router.include_router(meals.router, tags=["meals"])

# Plans endpoints -> /plans/...
# Note: plans.router already has prefix="/plans" defined
api_router.include_router(plans.router, tags=["plans"])
