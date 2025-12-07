from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from app.db.database import Base, engine
from app.api.api import api_router




# 1) Create DB tables (for development / MVP)
Base.metadata.create_all(bind=engine)

# 2) Create FastAPI app
app = FastAPI(title="FitPlate API")

# 3) Allowed front-end origins (Vite dev server ports)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5172",
    "http://127.0.0.1:5172",
]

# 4) Add CORS middleware so React can call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # allow all HTTP methods
    allow_headers=["*"],   # allow all headers (including Authorization)
)

# 5) Include our API router (auth, health, etc.)
app.include_router(api_router)
