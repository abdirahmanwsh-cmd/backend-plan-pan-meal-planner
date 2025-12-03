from typing import Optional
from pydantic import BaseModel, EmailStr

# Shape of user data returned to frontend
class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: Optional[str] = None  # Python 3.8-friendly

    class Config:
        orm_mode = True