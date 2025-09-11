import requests

BASE_URL = "http://localhost:5000"

def get_flask_routes():
    # Цей список потрібно створити вручну або автоматично через introspection Flask-апки
    # Наприклад, якщо ти можеш імпортувати app з main, то:
    # from main import app
    # return [str(rule) for rule in app.url_map.iter_rules() if "GET" in rule.methods]
    return [
        "/", "/login", "/logout", "/chef_register",
        "/dashboard", "/chef/dashboard", "/chef/statistik", "/api/clients",
        "/api/users", "/api/session_history", "/api/statistik",
        "/chef/audit", "/api/audit", "/test123"
        # додай ще свої GET/POST/PUT/DELETE endpoints якщо треба
    ]

def test_all_get_endpoints():
    session = requests.Session()
    # Спочатку реєструємо та логінемо Chef
    email = "autotest_" + "12345@example.com"
    password = "testpass123"
    reg = session.post(f"{BASE_URL}/chef_register", data={
        "email": email,
        "first_name": "Chef",
        "last_name": "Test",
        "password": password,
        "password2": password
    }, allow_redirects=True)
    session.post(f"{BASE_URL}/login", data={
        "email": email,
        "password": password
    }, allow_redirects=True)

    errors = []
    for route in get_flask_routes():
        url = BASE_URL + route
        try:
            resp = session.get(url)
            print(f"GET {url} -> {resp.status_code}")
            if resp.status_code not in [200, 302]:
                errors.append(f"{url}: Status {resp.status_code}")
        except Exception as e:
            errors.append(f"{url}: Exception {str(e)}")

    assert not errors, f"Errors found: {errors}"

if __name__ == "__main__":
    test_all_get_endpoints()