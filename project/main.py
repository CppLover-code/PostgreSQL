from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

# Подключение к PostgreSQL
engine = create_engine(
    "postgresql://postgres:postgre212223@localhost:5432/users_project"
)