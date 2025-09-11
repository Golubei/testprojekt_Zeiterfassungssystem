import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, set_engine

# --- СПОЧАТКУ створити engine і sessionmaker ---
test_engine = create_engine("sqlite:///:memory:")
set_engine(test_engine)
Base.metadata.create_all(bind=test_engine)

# --- ПОТІМ імпорт app ---
from main import app

@pytest.fixture(scope="function")
def test_client():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False
    client = app.test_client()
    return client

def test_login_flow(test_client):
    # Реєстрація Chef
    resp = test_client.post("/chef_register", data={
        "email": "chef@example.com",
        "first_name": "Chef",
        "last_name": "Test",
        "password": "pass123",
        "password2": "pass123"
    }, follow_redirects=True)
    print("\n--- chef_register ---\n", resp.data.decode())

    # Логін Chef
    resp = test_client.post("/login", data={
        "email": "chef@example.com",
        "password": "pass123"
    }, follow_redirects=True)
    print("\n--- login ---\n", resp.data.decode())

    # Доступ до dashboard
    resp = test_client.get("/dashboard")
    print("\n--- dashboard ---\n", resp.data.decode())

    assert b"Dashboard" in resp.data or b"Chef" in resp.data

def test_chef_register_and_login(test_client):
    # Реєстрація Chef через endpoint
    response = test_client.post("/chef_register", data={
        "email": "chef@example.com",
        "first_name": "Chef",
        "last_name": "Test",
        "password": "pass123",
        "password2": "pass123"
    }, follow_redirects=True)
    assert b"Chef successfully registered" in response.data or b"login" in response.data or b"Chef" in response.data

    # Логін Chef через endpoint
    response = test_client.post("/login", data={
        "email": "chef@example.com",
        "password": "pass123"
    }, follow_redirects=True)
    assert b"Chef Dashboard" in response.data or b"Dashboard" in response.data or b"Chef" in response.data

def test_dashboard_for_user(test_client):
    # Реєструємо користувача через endpoint для створення юзера (якщо є такий роут)
    # Якщо немає — додай такий роут для тестів або використовуй створення через шефа
    # Тут для прикладу через шефа
    test_client.post("/chef_register", data={
        "email": "chef@example.com",
        "first_name": "Chef",
        "last_name": "Test",
        "password": "pass123",
        "password2": "pass123"
    }, follow_redirects=True)
    test_client.post("/login", data={
        "email": "chef@example.com",
        "password": "pass123"
    }, follow_redirects=True)
    # Створити юзера через шеф-кабінет
    response = test_client.post("/chef/dashboard", data={
        "create_user": "1",
        "email": "userlogin@example.com",
        "first_name": "First",
        "last_name": "Last",
        "password": "password123",
        "password2": "password123"
    }, follow_redirects=True)
    assert b"Mitarbeiter erstellt" in response.data or b"Dashboard" in response.data

    # Логін звичайного юзера
    response = test_client.post("/login", data={
        "email": "userlogin@example.com",
        "password": "password123"
    }, follow_redirects=True)
    assert b"Dashboard" in response.data

    response = test_client.get("/dashboard")
    assert response.status_code == 200
    assert b"User" in response.data or b"Dashboard" in response.data

def test_dashboard_for_chef(test_client):
    # Реєструємо шефа через endpoint
    test_client.post("/chef_register", data={
        "email": "chef2@example.com",
        "first_name": "Chef2",
        "last_name": "Test2",
        "password": "password123",
        "password2": "password123"
    }, follow_redirects=True)
    response = test_client.post("/login", data={
        "email": "chef2@example.com",
        "password": "password123"
    }, follow_redirects=True)
    assert b"Chef Dashboard" in response.data or b"Dashboard" in response.data or b"Chef" in response.data

    response = test_client.get("/chef/dashboard")
    assert response.status_code == 200
    assert b"Chef" in response.data or b"Dashboard" in response.data

def test_logout(test_client):
    # Реєструємо користувача через endpoint для створення юзера (якщо є такий роут)
    test_client.post("/chef_register", data={
        "email": "chef3@example.com",
        "first_name": "Chef3",
        "last_name": "Test3",
        "password": "password123",
        "password2": "password123"
    }, follow_redirects=True)
    test_client.post("/login", data={
        "email": "chef3@example.com",
        "password": "password123"
    }, follow_redirects=True)
    # Створити юзера через шеф-кабінет
    test_client.post("/chef/dashboard", data={
        "create_user": "1",
        "email": "userlogout@example.com",
        "first_name": "Logout",
        "last_name": "Test",
        "password": "password123",
        "password2": "password123"
    }, follow_redirects=True)

    response = test_client.post("/login", data={
        "email": "userlogout@example.com",
        "password": "password123"
    }, follow_redirects=True)
    assert b"Dashboard" in response.data or b"User" in response.data

    response = test_client.get("/logout", follow_redirects=True)
    assert b"Erfolgreich ausgeloggt" in response.data or b"Login" in response.data

def test_test123(test_client):
    response = test_client.get("/test123")
    assert response.status_code == 200
    assert b"OK!" in response.data