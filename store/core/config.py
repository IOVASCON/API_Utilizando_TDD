from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"  # Caminho do banco de dados SQLite

    class Config:
        env_file = ".env"

settings = Settings()
