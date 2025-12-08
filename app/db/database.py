import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use DATABASE_URL from environment (Render/Railway/Vercel) or fall back to config
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    # Fall back to config if env var not set (local development)
    try:
        from app.core.config import settings
        DATABASE_URL = settings.DATABASE_URL
    except Exception:
        # Last resort: SQLite for local dev
        DATABASE_URL = "sqlite:///./fitplate.db"

# Create the SQLAlchemy engine
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for ORM models
Base = declarative_base()


# Dependency used in routes: gives a DB session and closes it afterwards
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()