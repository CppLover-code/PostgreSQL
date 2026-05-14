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

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    # Связь с Post
    posts = relationship("Post", back_populates="user")

"""
back_populates в SQLAlchemy связывает две модели между собой в обе стороны.

Проще говоря:
если есть User и Post, то:

у пользователя есть список постов
у поста есть владелец (пользователь)

back_populates говорит SQLAlchemy, что эти два поля связаны друг с другом
"""
# =========================
# POSTS
# =========================

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id")) # ForeignKey("users.id") означает: пост принадлежит пользователю.

    # связь с User
    user = relationship("User", back_populates="posts")

# Создание таблиц
Base.metadata.create_all(engine)

# Добавление пользователей
with Session(engine) as session:

    users = [
        User(name="Mark", age=25),
        User(name="Alex", age=30),
        User(name="Anna", age=22),
        User(name="John", age=40),
        User(name="Lisa", age=19)
    ]

    session.add_all(users)
    session.commit()
    print("Users added")
    