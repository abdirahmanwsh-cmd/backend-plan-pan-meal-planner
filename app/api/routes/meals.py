from fastapi import APIRouter, Depends
from typing import List
from app.schemas.meal import MealCreate, MealUpdate, MealResponse
from app.db.database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(prefix="/meals", tags=["Meals"])

# Dependency the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all meals
@router.get("/", response_model=List[MealResponse])
def get_meals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return []  

# GET a single meal
@router.get("/{meal_id}", response_model=MealResponse)
def get_meal(meal_id: int, db: Session = Depends(get_db)):
    return {}  

# POST create meal
@router.post("/", response_model=MealResponse)
def create_meal(meal: MealCreate, db: Session = Depends(get_db)):
    return {}  

# PUT update meal
@router.put("/{meal_id}", response_model=MealResponse)
def update_meal(meal_id: int, meal: MealUpdate, db: Session = Depends(get_db)):
    return {}  

# DELETE meal
@router.delete("/{meal_id}")
def delete_meal(meal_id: int, db: Session = Depends(get_db)):
    return {"msg": "deleted"}  
