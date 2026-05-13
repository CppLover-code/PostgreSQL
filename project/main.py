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

"""

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
        User(name="David", age=31, city="Prague"),
        User(name="Anna", age=32, city="Batumi")
    ]

    session.add_all(users)                          # добавляет сразу список объектов.
    session.commit()
    print("Users added")

"""

# ***********************************************************************************
# Получить ВСЕХ пользователей

with Session(engine) as session:

    users = session.query(User).all() # запрос к табл. users(SELECT * FROM users;) и возвращаем все записи
    # теперь в users хранится список объектов User

    for user in users:
        print(user.id, user.name, user.age, user.city)

# ***********************************************************************************
# Получить ПЕРВОГО пользователя

with Session(engine) as session:

    user = session.query(User).first() # возвращаем 1 объект
    """
    SELECT * FROM users
    LIMIT 1;
    """

    print(user.id, user.name, user.age, user.city)

# ***********************************************************************************
# Поиск по условию - filter_by()

with Session(engine) as session:

    user = session.query(User).filter_by(name='Anna').first() # поиск первого пользователя с именем Anna

    print(user.id, user.name, user.age, user.city)

# ***********************************************************************************
# Поиск по условию - filter_by() нескольких пользователей

with Session(engine) as session:

    users = session.query(User).filter_by(city='Batumi').all()
    print("******************************************")
    for user in users:
         print(user.id, user.name, user.age, user.city)

"""
SELECT * FROM users
WHERE city = 'Batumi';
"""

# ***********************************************************************************
# удаление всех пользователей, кроме первых 11

with Session(engine) as session:

    users_to_delete = (
        session.query(User)
        .order_by(User.id)          # сортируем по ID
        .offset(11)                 # пропускаем первые 11 пользователей
        .all()                      # получаем всех остальных
    )

    for user in users_to_delete:
        session.delete(user)        # удаляем

    session.commit()                # сохраняем изменения

# ***********************************************************************************
# filter() — более мощный поиск
