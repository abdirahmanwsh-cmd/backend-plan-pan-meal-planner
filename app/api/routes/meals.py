from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.meal import Meal
from app.schemas.meal import MealCreate, MealUpdate, MealOut, MealSuggestion
import random

router = APIRouter(prefix="/meals", tags=["Meals"])


# Get all meals
@router.get("/", response_model=List[MealOut])
def get_meals(db: Session = Depends(get_db)):
    meals = db.query(Meal).all()
    return meals


# Get meal by ID
@router.get("/{meal_id}", response_model=MealOut)
def get_meal(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(404, "Meal not found")
    return meal


# Create a new meal
@router.post("/", response_model=MealOut)
def create_meal(data: MealCreate, db: Session = Depends(get_db)):
    new_meal = Meal(**data.dict())
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal


# Update an existing meal
@router.put("/{meal_id}", response_model=MealOut)
def update_meal(meal_id: int, data: MealUpdate, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(404, "Meal not found")

    for key, value in data.dict().items():
        setattr(meal, key, value)

    db.commit()
    db.refresh(meal)
    return meal


# Delete meal
@router.delete("/{meal_id}")
def delete_meal(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(404, "Meal not found")

    db.delete(meal)
    db.commit()
    return {"message": f"Meal {meal_id} deleted"}


# Favourite toggle
@router.post("/{meal_id}/favorite", response_model=MealOut)
def toggle_favorite(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(404, "Meal not found")

    # simple flip
    meal.is_favorite = not meal.is_favorite
    db.commit()
    db.refresh(meal)
    return meal

# ADD THIS ENDPOINT TO FIX THE /meals/suggestion ERROR
@router.get("/suggestion", response_model=MealResponse)
def get_meal_suggestion(db: Session = Depends(get_db)):
    # Get a random meal - simple implementation
    import random
    meals = db.query(Meal).all()
    if not meals:
        raise HTTPException(status_code=404, detail="No meals available")
    return random.choice(meals)
