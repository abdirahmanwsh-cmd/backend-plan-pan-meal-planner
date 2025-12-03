from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FitPlate API"
    DATABASE_URL: str = "sqlite:///./fitplate.db"

    class Config:
        env_file = ".env"


settings = Settings()