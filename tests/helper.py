import random
import string
from werkzeug.security import generate_password_hash
from db import SessionLocal
from models import User, UserRole, Client, Zeitbuchung

def random_email(prefix="user"):
    """Генерує унікальний email для тестів."""
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{prefix}_{suffix}@example.com"

def random_password(length=10):
    """Генерує випадковий пароль."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_chef(email=None, password=None, first_name="Chef", last_name="Test"):
    """Створює тестового Chef у базі."""
    db = SessionLocal()
    email = email or random_email("chef")
    password = password or random_password()
    chef = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        hashed_password=generate_password_hash(password),
        role=UserRole.Chef,
        active=True,
    )
    db.add(chef)
    db.commit()
    db.refresh(chef)
    db.close()
    return {"email": chef.email, "password": password, "id": chef.id}

def create_user(email=None, password=None, first_name="User", last_name="Test"):
    """Створює тестового User у базі."""
    db = SessionLocal()
    email = email or random_email("user")
    password = password or random_password()
    user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        hashed_password=generate_password_hash(password),
        role=UserRole.User,
        active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return {"email": user.email, "password": password, "id": user.id}

def create_client(name=None):
    """Створює тестового клієнта у базі."""
    db = SessionLocal()
    name = name or f"Client_{''.join(random.choices(string.ascii_letters + string.digits, k=5))}"
    client = Client(
        name=name,
        active=True
    )
    db.add(client)
    db.commit()
    db.refresh(client)
    db.close()
    return {"name": client.name, "id": client.id}

def create_session(user_id, client_id, start_time, end_time=None, comment=""):
    """Створює Zeitbuchung (сесію) для тесту."""
    db = SessionLocal()
    session = Zeitbuchung(
        user_id=user_id,
        client_id=client_id,
        start_time=start_time,
        end_time=end_time,
        comment=comment
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    db.close()
    return session

def get_user_by_email(email):
    """Повертає User по email."""
    db = SessionLocal()
    user = db.query(User).filter_by(email=email).first()
    db.close()
    return user

def get_client_by_name(name):
    """Повертає Client по name."""
    db = SessionLocal()
    client = db.query(Client).filter_by(name=name).first()
    db.close()
    return client

def clear_db():
    """Очищає всі таблиці (для чистих тестів)."""
    db = SessionLocal()
    db.execute("DELETE FROM zeitbuchungen")
    db.execute("DELETE FROM audit_logs")
    db.execute("DELETE FROM users")
    db.execute("DELETE FROM clients")
    db.commit()
    db.close()