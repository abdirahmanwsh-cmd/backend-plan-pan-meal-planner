from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.schemas.meal import MealCreate, MealUpdate, MealResponse
from app.models.meal import Meal
from app.db.database import SessionLocal

router = APIRouter(prefix="/meals", tags=["Meals"])

# Simple DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all meals
@router.get("/", response_model=List[MealResponse])
def get_meals(db: Session = Depends(get_db)):
    meals = db.query(Meal).all()
    return meals

# GET single meal
@router.get("/{meal_id}", response_model=MealResponse)
def get_meal(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    return meal

# CREATE meal
@router.post("/", response_model=MealResponse)
def create_meal(meal: MealCreate, db: Session = Depends(get_db)):
    new_meal = Meal(**meal.dict())
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal

# UPDATE meal
@router.put("/{meal_id}", response_model=MealResponse)
def update_meal(meal_id: int, meal: MealUpdate, db: Session = Depends(get_db)):
    existing = db.query(Meal).filter(Meal.id == meal_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Meal not found")
    for key, value in meal.dict(exclude_none=True).items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return existing

# DELETE meal
@router.delete("/{meal_id}")
def delete_meal(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    db.delete(meal)
    db.commit()
    return {"msg": f"Meal {meal_id} deleted"}

