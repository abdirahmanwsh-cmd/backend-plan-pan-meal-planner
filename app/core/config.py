from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FitPlate API"
    DATABASE_URL: str = "postgresql://meal_user:your_password@localhost:5432/meal_planner"

    class Config:
        env_file = ".env"


settings = Settings()