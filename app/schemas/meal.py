from pydantic import BaseModel
from typing import Optional


# Base fields shared across meal requests
class MealBase(BaseModel):
    name: str
    calories: int
    tags: Optional[str] = None  # still using simple comma tags for now


# For creating a new meal
class MealCreate(MealBase):
    pass


# For updates (keeping it simple for the sprint)
class MealUpdate(MealBase):
    pass


# Full response object (what the FE actually receives)
class MealOut(MealBase):
    id: int
    is_favorite: bool = False  # added this for the suggestion feature
    user_id: Optional[int] = None

    class Config:
        orm_mode = True


# For daily suggestion endpoint
class MealSuggestion(BaseModel):
    id: int
    name: str
    calories: int
    reason: str  # e.g. "favourite" or "random pick"

    class Config:
        orm_mode = True
            