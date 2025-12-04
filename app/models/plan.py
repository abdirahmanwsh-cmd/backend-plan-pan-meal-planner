from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

# Weekly meal plan for one user
class MealPlan(Base):
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    # Link to the user who owns this plan
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    user = relationship("User")
    slots = relationship("MealSlot", back_populates="plan")