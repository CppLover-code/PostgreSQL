"""
ORM (Object-Relational Mapping — объектно-реляционное отображение) — это технология 
программирования, которая связывает базы данных с концепциями объектно-ориентированных 
языков, позволяя работать с записями в БД как с обычными объектами в коде, не написав 
ни строчки SQL. Она автоматически преобразует данные между таблицами БД и объектами 
кода. 

Самая популярная ORM для Flask — SQLAlchemy.
Установка
pip install sqlalchemy psycopg2-binary
"""
# Подключение к PostgreSQL

from sqlalchemy import create_engine
engine = create_engine(
    "postgresql://postgres:postgre212223@localhost:5432/test_dbSQLAlchemy"
)

# Создание модели

# специальный базовый класс для моделей SQLAlchemy.
# Через него SQLAlchemy понимает:"Эти классы будут таблицами базы данных."
from sqlalchemy.orm import DeclarativeBase
# Импортируем инструменты для создания колонок таблицы.
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

class Base(DeclarativeBase): # создаем базовый класс, все модели будут наследоваться от него
    pass

"""
SQLAlchemy собирает все модели через Base.

Потом может:

создать таблицы
видеть связи
делать запросы
"""

class User(Base):                           # Таблица User
    __tablename__ = "users"                 # таблица в PostgreSQL будет называться users

    id = Column(Integer, primary_key=True)  # Создание Колонка ID
    name = Column(String)                   # Создание Колонка name

Base.metadata.create_all(engine)            # Создание таблицы

"""
Главное понимание
Python-класс = таблица
"""

# Создание объекта
"""
создаем объект Python, 
Но SQLAlchemy понимает:
это будущая строка в БД.
"""
# объект реально записывается в PostgreSQL.

with Session(engine) as session:

    user = User(name="Mark")

    session.add(user)

    session.commit()
    print("User added")

