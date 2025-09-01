from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "SantectAI CRUD Service"
    DATABASE_URL: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()
