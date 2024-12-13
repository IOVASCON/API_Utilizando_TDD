from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from store.core.config import settings

print(f"DATABASE_URL: {settings.DATABASE_URL}")

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL  # Carrega a URL do banco de dados

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
