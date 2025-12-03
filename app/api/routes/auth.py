from fastapi import APIRouter, Depends
from ...core.security import get_current_user
from ...schemas.user import UserOut

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/me", response_model=UserOut)
def read_me(current_user = Depends(get_current_user)):
    # Returns the current logged-in user
    return current_user