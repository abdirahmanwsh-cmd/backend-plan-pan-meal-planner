from pydantic import BaseModel
from typing import Optional

# Meal schema used for requests/responses
class MealBase(BaseModel):
    name: str
    calories: int
    tags: Optional[list[str]] = None # Tags are optional

#Schema to create a meal
class MealCreate(MealBase):
    pass # Inherits all fields from MealBase

# Schema to update a meal
class MealUpdate(BaseModel):
    name: Optional[str] = None
    calories: Optional[int] = None
    tags: Optional[list[str]] = None

# Schema to represent a meal in responses
class MealResponse(MealBase):
    id: int

    class Config:
        orm_mode = True # Enable ORM mode for compatibility with ORM objects