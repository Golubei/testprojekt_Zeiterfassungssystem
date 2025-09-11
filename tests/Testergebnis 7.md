.venv) PS C:\Users\Praktikant\workspace\ze> pytest
================================================================================================== test session starts ==================================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\Users\Praktikant\workspace\ze
collected 14 items                                                                                                                                                                                                       

tests\test_1_sqlite.py ....                                                                                                                                                                                        [ 28%]
tests\test_models.py ....                                                                                                                                                                                          [ 57%]
tests\test_routes.py FFFFF.                                                                                                                                                                                        [100%]

======================================================================================================= FAILURES ========================================================================================================
____________________________________________________________________________________________________ test_login_flow ____________________________________________________________________________________________________

test_client = <FlaskClient <Flask 'main'>>

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

>       assert b"Dashboard" in resp.data or b"Chef" in resp.data
E       assert (b'Dashboard' in b'<!doctype html>\n<html lang=en>\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected...atically to the target URL: <a href="/login?next=%2Fdashboard">/login?next=%2Fdashboard</a>. If not, click the link.\n' or b'Chef' in b'<!doctype html>\n<html lang=en>\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected...atically to the target URL: <a href="/login?next=%2Fdashboard">/login?next=%2Fdashboard</a>. If not, click the link.\n')
E        +  where b'<!doctype html>\n<html lang=en>\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected...atically to the target URL: <a href="/login?next=%2Fdashboard">/login?next=%2Fdashboard</a>. If not, click the link.\n' = <WrapperTestResponse 235 bytes [302 FOUND]>.data
E        +  and   b'<!doctype html>\n<html lang=en>\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected...atically to the target URL: <a href="/login?next=%2Fdashboard">/login?next=%2Fdashboard</a>. If not, click the link.\n' = <WrapperTestResponse 235 bytes [302 FOUND]>.data

tests\test_routes.py:45: AssertionError
------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------- 

--- chef_register ---
 <!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #fafbfc;
        }
        .container {
            max-width: 370px;
            margin: 40px auto;
            background: #fff;
            border-radius: 12px;
            padding: 34px 28px 28px 28px;
            box-shadow: 0 2px 24px rgba(0,0,0,0.09);
        }
        h1 {
            text-align: left;
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-top: 16px;
            margin-bottom: 4px;
        }
        input[type="email"], input[type="password"] {
            width: 100%;
            padding: 9px;
            font-size: 1em;
            border: 1px solid #bbb;
            border-radius: 4px;
            margin-bottom: 8px;
            box-sizing: border-box;
            background: #f3f6fa;
        }
        button[type="submit"], .forgot-btn {
            width: 100%;
            background: #bdbdbd;
            color: #222;
            border: none;
            padding: 13px 0;
            margin-top: 14px;
            font-size: 1.04em;
            border-radius: 4px;
            cursor: pointer;
            text-align: center;
            font-weight: 600;
            transition: background 0.15s;
            display: block;
        }
        button[type="submit"]:hover, .forgot-btn:hover {
            background: #9e9e9e;
        }
        .forgot-btn {
            background: #bdbdbd;
            color: #222;
            margin-top: 10px;
            text-decoration: underline;
            border: none;
        }
        .flash-danger { color: red; }
        .flash-success { color: green; }
    </style>
    <script>
      window.addEventListener('DOMContentLoaded', function() {
        // Очищення полів навіть якщо браузер намагається автозаповнити
        var email = document.getElementById('email');
        var password = document.getElementById('password');
        if(email) email.value = '';
        if(password) password.value = '';
      });
    </script>
</head>
<body>
    <div class="container">
        <h1>Login</h1>


            <ul>

                <li class="flash-warning">Chef is already registered. Please log in.</li>

            </ul>


        <form method="POST" autocomplete="off">
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" autocomplete="off" required>

            <label for="password">Passwort:</label>
            <input type="password" name="password" id="password" autocomplete="off" required>

            <button type="submit" name="login">Login</button>
        </form>
        <form method="POST">
            <input type="hidden" name="reset_email" id="reset_email" value="">
            <button type="submit" name="forgot" class="forgot-btn" onclick="
                event.preventDefault();
                var email = prompt('Bitte geben Sie Ihre E-Mail für das Zurücksetzen des Passworts ein:');
                if(email) {
                  document.getElementById('reset_email').value = email;
                  this.form.submit();
                }
            ">Passwort vergessen?</button>
        </form>
    </div>
</body>
</html>
USER FOUND: None
PASSWORD OK: None
USER ACTIVE: None

--- login ---
 <!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #fafbfc;
        }
        .container {
            max-width: 370px;
            margin: 40px auto;
            background: #fff;
            border-radius: 12px;
            padding: 34px 28px 28px 28px;
            box-shadow: 0 2px 24px rgba(0,0,0,0.09);
        }
        h1 {
            text-align: left;
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-top: 16px;
            margin-bottom: 4px;
        }
        input[type="email"], input[type="password"] {
            width: 100%;
            padding: 9px;
            font-size: 1em;
            border: 1px solid #bbb;
            border-radius: 4px;
            margin-bottom: 8px;
            box-sizing: border-box;
            background: #f3f6fa;
        }
        button[type="submit"], .forgot-btn {
            width: 100%;
            background: #bdbdbd;
            color: #222;
            border: none;
            padding: 13px 0;
            margin-top: 14px;
            font-size: 1.04em;
            border-radius: 4px;
            cursor: pointer;
            text-align: center;
            font-weight: 600;
            transition: background 0.15s;
            display: block;
        }
        button[type="submit"]:hover, .forgot-btn:hover {
            background: #9e9e9e;
        }
        .forgot-btn {
            background: #bdbdbd;
            color: #222;
            margin-top: 10px;
            text-decoration: underline;
            border: none;
        }
        .flash-danger { color: red; }
        .flash-success { color: green; }
    </style>
    <script>
      window.addEventListener('DOMContentLoaded', function() {
        // Очищення полів навіть якщо браузер намагається автозаповнити
        var email = document.getElementById('email');
        var password = document.getElementById('password');
        if(email) email.value = '';
        if(password) password.value = '';
      });
    </script>
</head>
<body>
    <div class="container">
        <h1>Login</h1>


            <ul>

                <li class="flash-danger">Ungültige E-Mail oder Passwort.</li>

            </ul>


        <form method="POST" autocomplete="off">
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" autocomplete="off" required>

            <label for="password">Passwort:</label>
            <input type="password" name="password" id="password" autocomplete="off" required>

            <button type="submit" name="login">Login</button>
        </form>
        <form method="POST">
            <input type="hidden" name="reset_email" id="reset_email" value="">
            <button type="submit" name="forgot" class="forgot-btn" onclick="
                event.preventDefault();
                var email = prompt('Bitte geben Sie Ihre E-Mail für das Zurücksetzen des Passworts ein:');
                if(email) {
                  document.getElementById('reset_email').value = email;
                  this.form.submit();
                }
            ">Passwort vergessen?</button>
        </form>
    </div>
</body>
</html>

--- dashboard ---
 <!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/login?next=%2Fdashboard">/login?next=%2Fdashboard</a>. If not, click the link.

_____________________________________________________________________________________________ test_chef_register_and_login ______________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

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
>       assert b"Chef Dashboard" in response.data or b"Dashboard" in response.data or b"Chef" in response.data
E       assert (b'Chef Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' or b'Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' or b'Chef' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>')
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data
E        +  and   b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data
E        +  and   b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data

tests\test_routes.py:63: AssertionError
------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------- 
USER FOUND: None
PASSWORD OK: None
USER ACTIVE: None
________________________________________________________________________________________________ test_dashboard_for_user ________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

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
>       assert b"Mitarbeiter erstellt" in response.data or b"Dashboard" in response.data
E       assert (b'Mitarbeiter erstellt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' or b'Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>')
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3473 bytes [200 OK]>.data
E        +  and   b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3473 bytes [200 OK]>.data

tests\test_routes.py:89: AssertionError
------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------- 
USER FOUND: None
PASSWORD OK: None
USER ACTIVE: None
________________________________________________________________________________________________ test_dashboard_for_chef ________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

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
>       assert b"Chef Dashboard" in response.data or b"Dashboard" in response.data or b"Chef" in response.data
E       assert (b'Chef Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' or b'Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' or b'Chef' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>')
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data
E        +  and   b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data
E        +  and   b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data

tests\test_routes.py:115: AssertionError
------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------- 
USER FOUND: None
PASSWORD OK: None
USER ACTIVE: None
______________________________________________________________________________________________________ test_logout ______________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

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
>       assert b"Dashboard" in response.data or b"User" in response.data
E       assert (b'Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' or b'User' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>')
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data
E        +  and   b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data

tests\test_routes.py:148: AssertionError
------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------- 
USER FOUND: None
PASSWORD OK: None
USER ACTIVE: None
USER FOUND: None
PASSWORD OK: None
USER ACTIVE: None
=================================================================================================== warnings summary ==================================================================================================== 
tests/test_1_sqlite.py: 16 warnings
tests/test_models.py: 16 warnings
  C:\Users\Praktikant\workspace\ze\.venv\Lib\site-packages\sqlalchemy\sql\schema.py:3624: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    return util.wrap_callable(lambda ctx: fn(), fn)  # type: ignore

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================================================================ short test summary info ================================================================================================ 
FAILED tests/test_routes.py::test_login_flow - assert (b'Dashboard' in b'<!doctype html>\n<html lang=en>\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected...atically to the target URL: <a href="/login?next=%2Fdashboard">/logi...
FAILED tests/test_routes.py::test_chef_register_and_login - assert (b'Chef Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?<...
FAILED tests/test_routes.py::test_dashboard_for_user - assert (b'Mitarbeiter erstellt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort verge...
FAILED tests/test_routes.py::test_dashboard_for_chef - assert (b'Chef Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?<...
FAILED tests/test_routes.py::test_logout - assert (b'Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</butt...
======================================================================================= 5 failed, 9 passed, 32 warnings in 1.17s ======================================================================================== 