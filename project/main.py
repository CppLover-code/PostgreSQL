from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

# Подключение к PostgreSQL
engine = create_engine(
    "postgresql://postgres:postgre212223@localhost:5432/users_project"
)

# Базовый класс
class Base(DeclarativeBase):
    pass

# Модель таблицы
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    city = Column(String)

# Создание таблицы
Base.metadata.create_all(engine)

# Добавим пользователей
with Session(engine) as session:

    users = [
        User(name="Max", age=25, city="Batumi"),
        User(name="Alex", age=30, city="Tbilisi"),
        User(name="Anna", age=22, city="Kyiv"),
        User(name="John", age=28, city="London"),
        User(name="Kate", age=19, city="Paris"),

        User(name="Mike", age=35, city="Berlin"),
        User(name="Sara", age=27, city="Rome"),
        User(name="Tom", age=40, city="Madrid"),
        User(name="Lisa", age=24, city="Warsaw"),
        User(name="David", age=31, city="Prague")
    ]

    session.add_all(users)                          # добавляет сразу список объектов.
    session.commit()
    print("Users added")