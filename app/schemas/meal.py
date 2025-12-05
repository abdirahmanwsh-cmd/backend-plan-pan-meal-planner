from pydantic import BaseModel
from typing import Optional

# Base schema for meals, used for create/update
class MealBase(BaseModel):
    name: str
    calories: int
    tags: Optional[str] = None  # optional comma-separated tags like "high-protein,lunch"

# Schema for creating a new meal
class MealCreate(MealBase):
    pass  # nothing extra, same fields as base

# Schema for updating an existing meal
class MealUpdate(BaseModel):
    name: Optional[str] = None
    calories: Optional[int] = None
    tags: Optional[str] = None

# Schema for sending meal info back to frontend
class MealResponse(MealBase):
    id: int
    is_favorite: Optional[bool] = False
    user_id: Optional[int] = None

    class Config:
        orm_mode = True  # allows returning SQLAlchemy models directly