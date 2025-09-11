import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///test.db")  # дефолт — test.db
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def set_engine(new_engine):
    global engine, SessionLocal
    engine = new_engine
    SessionLocal = sessionmaker(bind=engine)