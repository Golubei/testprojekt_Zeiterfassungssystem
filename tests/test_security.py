import pytest

@pytest.fixture(scope="function")
def test_client():
    from main import app
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False
    client = app.test_client()
    return client

def test_sql_injection_login(test_client):
    # Спроба SQL injection через поле email
    response = test_client.post("/login", data={
        "email": "' OR 1=1 --",
        "password": "any_password"
    }, follow_redirects=True)
    # Має бути помилка входу, а не обхід автентифікації
    assert "Ungültige E-Mail oder Passwort." in response.data.decode("utf-8")

def test_dashboard_access_without_login(test_client):
    # Доступ до захищеної сторінки без авторизації
    response = test_client.get("/dashboard", follow_redirects=True)
    # Має бути редірект на логін або flash-повідомлення
    data = response.data.decode("utf-8")
    assert "Login" in data or "Bitte melden Sie sich an" in data

def test_csrf_disabled_in_test(test_client):
    # CSRF повинен бути вимкнено для тестів, але в продакшн має бути увімкнено
    assert not test_client.application.config.get("WTF_CSRF_ENABLED", True), "CSRF захист має бути вимкнено для тестів"

def test_chef_register_duplicate_email(test_client):
    # Зареєструвати Chef з одним email
    test_client.post("/chef_register", data={
        "email": "chefsec@example.com",
        "first_name": "Chef",
        "last_name": "Sec",
        "password": "pass123",
        "password2": "pass123"
    }, follow_redirects=True)
    # Повторна реєстрація з тим же email
    response = test_client.post("/chef_register", data={
        "email": "chefsec@example.com",
        "first_name": "Chef",
        "last_name": "Sec",
        "password": "pass123",
        "password2": "pass123"
    }, follow_redirects=True)
    # Має бути помилка про дублюючий email
    data = response.data.decode("utf-8")
    assert "Email is already registered." in data or "bereits registriert" in data

def test_change_password_short(test_client):
    # Реєстрація та логін
    test_client.post("/chef_register", data={
        "email": "secpass@example.com",
        "first_name": "Sec",
        "last_name": "Pass",
        "password": "goodpass",
        "password2": "goodpass"
    }, follow_redirects=True)
    test_client.post("/login", data={
        "email": "secpass@example.com",
        "password": "goodpass"
    }, follow_redirects=True)
    # Зміна пароля на дуже короткий (менше 6 символів)
    response = test_client.post("/api/change_password", json={
        "password": "123",
        "password2": "123"
    })
    # Має бути помилка про мінімальну довжину
    data = response.data.decode("utf-8")
    assert (
        "Mindestlänge" in data or
        "6 Zeichen" in data or
        "Mindestlänge des Passworts beträgt 6 Zeichen" in data
    )