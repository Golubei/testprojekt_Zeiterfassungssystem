import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, set_engine
from datetime import datetime

# --- СПОЧАТКУ створити engine і sessionmaker ---
test_engine = create_engine("sqlite:///:memory:")
TestSessionLocal = sessionmaker(bind=test_engine)
set_engine(test_engine)
Base.metadata.create_all(bind=test_engine)

# --- ПОТІМ імпорт app ---
from main import app
from models import User, UserRole, Client, Zeitbuchung, AuditLog
from werkzeug.security import generate_password_hash


@pytest.fixture(scope="function")
def db_session():
    # Очищуємо та створюємо структуру БД перед кожним тестом
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    session = TestSessionLocal()
    yield session
    session.close()

def test_create_user(db_session):
    user = User(
        email="testuser@example.com",
        hashed_password="hashed_pass",
        role=UserRole.User,
        first_name="Test",
        last_name="User",
        active=True
    )
    db_session.add(user)
    db_session.commit()
    assert user.id is not None
    found = db_session.query(User).filter_by(email="testuser@example.com").first()
    assert found is not None
    assert found.first_name == "Test"
    assert found.role == UserRole.User

def test_create_client(db_session):
    client = Client(name="TestClient", active=True)
    db_session.add(client)
    db_session.commit()
    assert client.id is not None
    found = db_session.query(Client).filter_by(name="TestClient").first()
    assert found is not None
    assert found.active

def test_create_zeitbuchung_and_relationships(db_session):
    user = User(
        email="user2@example.com",
        hashed_password="pass2",
        role=UserRole.User,
        first_name="Ivan",
        last_name="Ivanov",
        active=True
    )
    client = Client(name="Client2", active=True)
    db_session.add(user)
    db_session.add(client)
    db_session.commit()

    zb = Zeitbuchung(
        user_id=user.id,
        client_id=client.id,
        start_time=datetime(2023, 1, 1, 9, 0),
        end_time=datetime(2023, 1, 1, 17, 0),
        comment="Test comment"
    )
    db_session.add(zb)
    db_session.commit()
    assert zb.id is not None

    zb_from_db = db_session.query(Zeitbuchung).filter_by(id=zb.id).first()
    assert zb_from_db.user.id == user.id
    assert zb_from_db.client.id == client.id

def test_audit_log(db_session):
    user = User(
        email="audit@example.com",
        hashed_password="pass",
        role=UserRole.Chef,
        first_name="Audit",
        last_name="Master",
        active=True
    )
    client = Client(name="AuditClient", active=True)
    db_session.add(user)
    db_session.add(client)
    db_session.commit()
    zb = Zeitbuchung(
        user_id=user.id,
        client_id=client.id,
        start_time=datetime.now(),
        comment="audit"
    )
    db_session.add(zb)
    db_session.commit()

    log = AuditLog(
        timestamp=datetime.now(),
        user_id=user.id,
        session_id=zb.id,
        action="edit",
        details='{"field":"value"}'
    )
    db_session.add(log)
    db_session.commit()
    log_from_db = db_session.query(AuditLog).filter_by(id=log.id).first()
    assert log_from_db.action == "edit"
    assert log_from_db.user_id == user.id