import requests

BASE_URL = "http://localhost:5000"

def get_flask_routes():
    # Список ручних GET-роутів для тесту
    return [
        "/", "/login", "/logout", "/chef_register",
        "/dashboard", "/chef/dashboard", "/chef/statistik", "/api/clients",
        "/api/users", "/api/session_history", "/api/statistik",
        "/chef/audit", "/api/audit", "/test123"
        # Додай інші ендпоінти за потреби
    ]

def test_all_get_endpoints():
    session = requests.Session()
    # Реєстрація та логін Chef
    email = "autotest_" + "12345@example.com"
    password = "testpass123"
    reg = session.post(
        f"{BASE_URL}/chef_register",
        data={
            "email": email,
            "first_name": "Chef",
            "last_name": "Test",
            "password": password,
            "password2": password
        },
        allow_redirects=True,
        timeout=10
    )
    session.post(
        f"{BASE_URL}/login",
        data={
            "email": email,
            "password": password
        },
        allow_redirects=True,
        timeout=10
    )

    errors = []
    for route in get_flask_routes():
        url = BASE_URL + route
        try:
            resp = session.get(url, timeout=10)
            print(f"GET {url} -> {resp.status_code}")
            if resp.status_code not in [200, 302]:
                errors.append(f"{url}: Status {resp.status_code}")
        except Exception as e:
            errors.append(f"{url}: Exception {str(e)}")

    assert not errors, f"Errors found: {errors}"

if __name__ == "__main__":
    test_all_get_endpoints()