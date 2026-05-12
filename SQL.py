"""
SQL - язык для общения с базой данных.

Через SQL можно:
создавать таблицы
добавлять данные
искать данные
обновлять данные
удалять данные
"""
#*********************************************************
"""
Основные SQL-команды

1. Создание таблицы

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
);

2. Добавление данных

INSERT INTO users (name, age)
VALUES ('Mark', 25);

3. Получение данных

Все пользователи
SELECT * FROM users;

Только имя
SELECT name FROM users;

С условием
SELECT * FROM users
WHERE age > 18;

4. Обновление данных

UPDATE users
SET age = 30
WHERE id = 1;

5. Удаление данных

DELETE FROM users
WHERE id = 1;

6. JOIN — связывание таблиц

Таблица users
id	name
1	Mark

Таблица posts
id	title	user_id
1	Hello	1

user_id указывает на пользователя.

JOIN
SELECT users.name, posts.title
FROM users
JOIN posts
ON users.id = posts.user_id;

Что происходит:

берём users
соединяем posts
сравниваем:
users.id
posts.user_id
"""
#*********************************************************
"""
Индексы (Indexes)

Индексы ускоряют поиск. Без индекса база перебирает всё:
Создание индекса
CREATE INDEX idx_users_name
ON users(name);

Обычно индекс делают на:

id
email
username
foreign keys
"""
#*********************************************************