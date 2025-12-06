from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.schemas.plan import MealPlanCreate, MealPlanResponse, MealSlotCreate, MealSlotResponse
from app.models.plan import MealPlan
from app.models.mealslot import MealSlot
from app.db.database import SessionLocal

router = APIRouter(prefix="/plans", tags=["Meal Plans"])

# Simple DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET current plan (just returns the first plan for now)
@router.get("/current", response_model=MealPlanResponse)
def get_current_plan(db: Session = Depends(get_db)):
    plan = db.query(MealPlan).first()
    if not plan:
        raise HTTPException(status_code=404, detail="No meal plan found")
    return plan

# CREATE new plan
@router.post("/", response_model=MealPlanResponse)
def create_plan(plan: MealPlanCreate, db: Session = Depends(get_db)):
    new_plan = MealPlan(**plan.dict())
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return new_plan

# ADD a slot to a plan
@router.post("/{plan_id}/slots", response_model=MealSlotResponse)
def add_slot(plan_id: int, slot: MealSlotCreate, db: Session = Depends(get_db)):
    plan = db.query(MealPlan).filter(MealPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    new_slot = MealSlot(**slot.dict(), plan_id=plan_id)
    db.add(new_slot)
    db.commit()
    db.refresh(new_slot)
    return new_slot

# UPDATE a slot
@router.put("/slots/{slot_id}", response_model=MealSlotResponse)
def update_slot(slot_id: int, slot: MealSlotCreate, db: Session = Depends(get_db)):
    existing = db.query(MealSlot).filter(MealSlot.id == slot_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Slot not found")
    for key, value in slot.dict().items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return existing

# GET shopping list (aggregate meals in current plan)
@router.get("/shopping-list", response_model=List[str])
def get_shopping_list(db: Session = Depends(get_db)):
    plan = db.query(MealPlan).first()
    if not plan:
        return []
    ingredients = []
    for slot in plan.slots:
        if hasattr(slot.meal, "tags") and slot.meal.tags:
            ingredients += slot.meal.tags.split(",")  # just using tags as ingredients
    # remove duplicates
    unique_ingredients = list(set(ingredients))
    return unique_ingredients
