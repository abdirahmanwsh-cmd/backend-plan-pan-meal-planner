from typing import Optional
from pydantic import BaseModel, EmailStr

# Shape of user data returned to frontend
class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: Optional[str] = None  

    class Config:
        from_attributes = True