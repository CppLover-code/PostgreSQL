"""
получение по ID
сложные фильтры
LIKE
count()
IN
AND / OR
relationships между таблицами
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import DeclarativeBase, Session, relationship

# Подключение
engine = create_engine(
    "postgresql://postgres:postgre212223@localhost:5432/blog_project"
)

# Base
class Base(DeclarativeBase):
    pass

# =========================
# USERS
# =========================
