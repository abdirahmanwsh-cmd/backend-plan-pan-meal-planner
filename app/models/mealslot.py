from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

# Connects a meal to a specific day + meal time in a plan
class MealSlot(Base):
    __tablename__ = "meal_slots"

    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("meal_plans.id"), nullable=False)
    day = Column(String, nullable=False)        # e.g. "Monday"
    meal_time = Column(String, nullable=False)  # e.g. "Breakfast"
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)

    plan = relationship("MealPlan", back_populates="slots")
    meal = relationship("Meal")