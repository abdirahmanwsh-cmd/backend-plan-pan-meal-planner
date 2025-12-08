from typing import Optional
from pydantic import BaseModel


# ---------- Shared fields for all meal requests ----------
class MealBase(BaseModel):
    name: str
    calories: int
    tags: Optional[str] = None          # simple comma-separated tags
    is_favorite: bool = False           # default: not favourite


# ---------- For creating a new meal ----------
class MealCreate(MealBase):
    pass


# ---------- For updating an existing meal ----------
class MealUpdate(BaseModel):
    name: Optional[str] = None
    calories: Optional[int] = None
    tags: Optional[str] = None
    is_favorite: Optional[bool] = None


# ---------- Full response object (what the frontend receives) ----------
class MealOut(MealBase):
    id: int
    user_id: Optional[int] = None       # included for auth / suggestion features

    class Config:
        from_attributes = True                # allow reading from SQLAlchemy models