
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# Reads "Authorization: Bearer <token>" header
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Reject request if token missing
    if credentials is None or not credentials.credentials:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = credentials.credentials

    # TODO: Replace with real Firebase verification later
    # For now, accept any token and return a demo user
    return {
        "id": 1,
        "email": "demo@example.com",
        "name": "Demo User"
    }