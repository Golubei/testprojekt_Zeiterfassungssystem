import pytest

@pytest.fixture(scope="function")
def test_client():
    from main import app
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False
    client = app.test_client()
    return client

def test_dashboard_perf(benchmark, test_client):
    # Для тесту потрібний автентифікований користувач.
    # Реєструємо та логінемо Chef
    test_client.post("/chef_register", data={
        "email": "perf@example.com",
        "first_name": "Perf",
        "last_name": "Test",
        "password": "perfpass123",
        "password2": "perfpass123"
    }, follow_redirects=True)
    test_client.post("/login", data={
        "email": "perf@example.com",
        "password": "perfpass123"
    }, follow_redirects=True)

    # Вимірюємо продуктивність dashboard
    def get_dashboard():
        return test_client.get("/dashboard")

    result = benchmark(get_dashboard)
    assert result.status_code == 200