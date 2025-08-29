from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Рядок підключення до бази (заміни на свої налаштування)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# Для PostgreSQL: "postgresql://user:password@localhost/dbname"

# Створення двигуна (engine)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # тільки для SQLite!
)

# Створення сесії
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для моделей
Base = declarative_base()