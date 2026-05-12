from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:postgre212223@localhost:5432/postgres"
)

connection = engine.connect()

print("CONNECTED")