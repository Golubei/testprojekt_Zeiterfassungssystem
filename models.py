from datetime import datetime
from enum import Enum
from sqlalchemy import (
    Column, Integer, String, DateTime, Boolean, Text, Enum as SqlEnum, ForeignKey
)
from sqlalchemy.orm import relationship
from flask_login import UserMixin          # ДОДАТИ!
from db import Base
import calendar

class UserRole(Enum):
    User = "User"
    Chef = "Chef"

class User(Base, UserMixin):               # ДОДАТИ UserMixin!
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(SqlEnum(UserRole), nullable=False)
    first_name = Column(String, nullable=False)     # Ім'я
    last_name = Column(String, nullable=False)      # Прізвище
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    zeitbuchungen = relationship("Zeitbuchung", back_populates="user")

    # ДОДАТИ, якщо хочеш явну реалізацію (але UserMixin вже це має):
    def get_id(self):
        return str(self.id)

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    zeitbuchungen = relationship("Zeitbuchung", back_populates="client")

class Zeitbuchung(Base):
    __tablename__ = "zeitbuchungen"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="zeitbuchungen")
    client = relationship("Client", back_populates="zeitbuchungen")