from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base

# Single meal item (e.g. "Grilled Chicken Salad")
class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    calories = Column(Integer, nullable=False)
    # Comma-separated tags: "high-protein,breakfast"
    tags = Column(String, nullable=True)
    is_favorite = Column(Boolean, default=False)  # ADDED THIS LINE
    
    # Owner of the meal (optional for now)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User")