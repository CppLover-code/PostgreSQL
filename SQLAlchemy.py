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

from SQLAlchemy import create_engine
engine = create_engine(
    "postgresql://postgres:password@localhost/test_dbAlc"
)
