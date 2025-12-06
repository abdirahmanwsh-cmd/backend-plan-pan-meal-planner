from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.plan import MealPlan, MealSlot
from app.schemas.plan import MealPlanCreate, MealPlanResponse, MealSlotCreate, MealSlotResponse
from app.db.database import SessionLocal

router = APIRouter(prefix="/plans", tags=["Meal Plans"])

# simple DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get current user's plan (just returns first for now)
@router.get("/current", response_model=MealPlanResponse)
def get_current_plan(db: Session = Depends(get_db)):
    plan = db.query(MealPlan).first()
    if not plan:
        raise HTTPException(status_code=404, detail="No plan found")
    return plan

# create a new weekly plan
@router.post("/", response_model=MealPlanResponse)
def create_plan(plan: MealPlanCreate, db: Session = Depends(get_db)):
    new_plan = MealPlan(**plan.dict())
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return new_plan

# add a meal slot to a plan
@router.post("/{plan_id}/slots", response_model=MealSlotResponse)
def add_meal_slot(plan_id: int, slot: MealSlotCreate, db: Session = Depends(get_db)):
    plan = db.query(MealPlan).filter(MealPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    new_slot = MealSlot(plan_id=plan_id, **slot.dict())
    db.add(new_slot)
    db.commit()
    db.refresh(new_slot)
    return new_slot

# update a meal slot
@router.put("/slots/{slot_id}", response_model=MealSlotResponse)
def update_meal_slot(slot_id: int, slot: MealSlotCreate, db: Session = Depends(get_db)):
    existing_slot = db.query(MealSlot).filter(MealSlot.id == slot_id).first()
    if not existing_slot:
        raise HTTPException(status_code=404, detail="Slot not found")
    for key, value in slot.dict(exclude_none=True).items():
        setattr(existing_slot, key, value)
    db.commit()
    db.refresh(existing_slot)
    return existing_slot

# get all slots for a plan
@router.get("/{plan_id}/slots", response_model=List[MealSlotResponse])
def get_slots(plan_id: int, db: Session = Depends(get_db)):
    slots = db.query(MealSlot).filter(MealSlot.plan_id == plan_id).all()
    return slots