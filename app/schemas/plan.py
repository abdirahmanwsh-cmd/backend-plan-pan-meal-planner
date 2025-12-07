from pydantic import BaseModel
from typing import List, Optional

# Schema for creating a meal plan
class MealPlanCreate(BaseModel):
    title: str
    user_id: Optional[int] = None

# Schema for creating a slot inside a plan
class MealSlotCreate(BaseModel):
    meal_id: int
    day: str  # e.g. Monday
    meal_time: str  # e.g. Breakfast

# Schema for a slot response
class MealSlotResponse(MealSlotCreate):
    id: int

    class Config:
        orm_mode = True

# Schema for meal plan response
class MealPlanResponse(BaseModel):
    id: int
    title: str
    slots: List[MealSlotResponse] = []

    class Config:
        orm_mode = True