from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.schemas.meal import MealCreate, MealUpdate, MealResponse
from app.db.database import SessionLocal
from app.models.meal import Meal

router = APIRouter(prefix="/meals", tags=["Meals"])

# simple DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get all meals
@router.get("/", response_model=List[MealResponse])
def get_meals(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    meals = db.query(Meal).offset(skip).limit(limit).all()
    return meals

# get a single meal by id
@router.get("/{meal_id}", response_model=MealResponse)
def get_meal(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    return meal

# create a new meal
@router.post("/", response_model=MealResponse)
def create_meal(meal: MealCreate, db: Session = Depends(get_db)):
    new_meal = Meal(**meal.dict())
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal

# update an existing meal
@router.put("/{meal_id}", response_model=MealResponse)
def update_meal(meal_id: int, meal: MealUpdate, db: Session = Depends(get_db)):
    existing_meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not existing_meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    for key, value in meal.dict(exclude_none=True).items():
        setattr(existing_meal, key, value)
    db.commit()
    db.refresh(existing_meal)
    return existing_meal

# delete a meal
@router.delete("/{meal_id}")
def delete_meal(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    db.delete(meal)
    db.commit()
    return {"msg": f"Meal {meal_id} deleted successfully"}

# toggle favorite for a meal
@router.patch("/{meal_id}/favorite")
def toggle_favorite(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    meal.is_favorite = not meal.is_favorite
    db.commit()
    return {"favorite": meal.is_favorite}

# ADD THIS ENDPOINT TO FIX THE /meals/suggestion ERROR
@router.get("/suggestion", response_model=MealResponse)
def get_meal_suggestion(db: Session = Depends(get_db)):
    # Get a random meal - simple implementation
    import random
    meals = db.query(Meal).all()
    if not meals:
        raise HTTPException(status_code=404, detail="No meals available")
    return random.choice(meals)