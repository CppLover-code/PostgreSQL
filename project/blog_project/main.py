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

# Добавление постов
with Session(engine) as session:

    posts = [
         Post(title="Python Basics", user_id=1),
        Post(title="Flask Tutorial", user_id=1),

        Post(title="SQLAlchemy Guide", user_id=2),

        Post(title="PostgreSQL Tips", user_id=3),

        Post(title="REST API", user_id=4)
    ]
    
    session.add_all(posts)
    session.commit()
    print("Posts added")

# OPERATIONS
# Получить ВСЕХ пользователей
print("All users")
with Session(engine) as session:

    users = session.query(User).all() # запрос к табл. users(SELECT * FROM users;) и возвращаем все записи
    # теперь в users хранится список объектов User

    for user in users:
        print(user.id, user.name, user.age)

# ***********************************************************************************

# Получение по ID
print("Getting a user by ID")
with Session(engine) as session:
    user = session.get(User, 1)
    print(user.name, user.age)
# get() специально оптимизирован для поиска по PRIMARY KEY.
# ***********************************************************************************

# AND условие
print("AND condition")
from sqlalchemy import and_
with Session(engine) as session:
    
    users = session.query(User).filter(
        and_(
            User.age > 20,
            User.age < 35
        )
    ).all()

    for user in users:
        print(user.name, user.age)

"""
SQL аналог
SELECT * FROM users
WHERE age > 20
AND age < 35;
"""
# ***********************************************************************************
# OR условие
print("OR condition")
from sqlalchemy import or_

users = session.query(User).filter(
    or_(
        User.age < 20,
        User.age > 35
    )
).all()

for user in users:
        print(user.name, user.age)
"""
SQL аналог
WHERE age < 20
OR age > 35
"""

# ***********************************************************************************
# LIKE поиск
print("LIKE searching")
users = session.query(User).filter(
    User.name.like("M%") # % любые символы
).all()

for user in users:
    print(user.name, user.age)

"""
SQL аналог
SELECT * FROM users
WHERE name LIKE 'M%';
"""

"""
Примеры
LIKE	Что найдёт
M%	    Mark
%a	    Anna
%lex%	Alex
"""
# ***********************************************************************************
# count()
print("count()")

count = session.query(User).count()

print(count)

"""
SQL аналог
SELECT COUNT(*) FROM users;
"""

# ***********************************************************************************
# in()
print("in()")

users = session.query(User).filter(
    User.id.in_([1, 3, 5])
).all()

for user in users:
    print(user.name, user.age)

"""
SQL аналог
WHERE id IN (1, 3, 5)
"""

# ***********************************************************************************
# Relationship - Получить посты пользователя
print("Relationship")

with Session(engine) as session:

    user = session.get(User, 1)

    print(user.name, user.age)

    for post in user.posts:
        print(post.title)

"""
SQLAlchemy автоматически связывает:

users.id
↕
posts.user_id
"""
# Получить автора поста
with Session(engine) as session:

    post = session.get(Post, 1)

    print(post.title)

    print(post.user.name)

"""
Главное понимание relationships
Таблица	    Связь
users	    один пользователь
posts	    много постов

One to many
"""
