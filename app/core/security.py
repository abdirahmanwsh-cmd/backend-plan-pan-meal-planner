from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.firebase import verify_token  
from app.schemas.user import UserOut          


# Read Authorization: Bearer <token> from headers
security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> UserOut:
    # 1) Reject missing / empty token
    if credentials is None or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header",
        )

    id_token = credentials.credentials

    # 2) Verify Firebase ID token
    try:
        decoded = verify_token(id_token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    # 3) Build a simple user object from Firebase data
    email = decoded.get("email")
    name = decoded.get("name") or decoded.get("display_name") or "User"
    firebase_uid = decoded.get("user_id")  # you can store/use this later

    # For now we don't have a users table lookup,
    # so we just return a dummy numeric id with real email & name.
    return UserOut(
        id=1,            # TODO: replace with real DB user id later
        email=email,
        name=name,
    )