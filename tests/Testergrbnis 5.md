(.venv) PS C:\Users\Praktikant\workspace\ze> pytest
================================================================================================= test session starts ==================================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\Users\Praktikant\workspace\ze
collected 14 items                                                                                                                                                                                                      

tests\test_1_sqlite.py ....                                                                                                                                                                                       [ 28%]
tests\test_models.py ....                                                                                                                                                                                         [ 57%]
tests\test_routes.py .FFFF.                                                                                                                                                                                       [100%]

======================================================================================================= FAILURES =======================================================================================================
_______________________________________________________________________________________________ test_register_and_login ________________________________________________________________________________________________

test_client = <FlaskClient <Flask 'main'>>

    def test_register_and_login(test_client):
        # Зареєструвати Chef
        response = test_client.post("/register", data={
            "email": "chef@example.com",
            "first_name": "Chef",
            "last_name": "Test",
            "password": "pass123",
            "password2": "pass123"
        }, follow_redirects=True)
>       assert b"Teamleiter erfolgreich registriert" in response.data
E       AssertionError: assert b'Teamleiter erfolgreich registriert' in b'<!doctype html>\n<html lang=en>\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>\n'
E        +  where b'<!doctype html>\n<html lang=en>\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>\n' = <WrapperTestResponse 207 bytes [404 NOT FOUND]>.data

tests\test_routes.py:63: AssertionError
_______________________________________________________________________________________________ test_dashboard_for_user ________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

    def test_dashboard_for_user(test_client):
        user = create_test_user(role=UserRole.User)
        response = login(test_client, "userlogin@example.com", "password123")
>       assert b"Dashboard" in response.data    # title сторінки юзера
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       assert b'Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>'
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data

tests\test_routes.py:72: AssertionError
_______________________________________________________________________________________________ test_dashboard_for_chef ________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

    def test_dashboard_for_chef(test_client):
        chef = create_test_user(role=UserRole.Chef)
        response = login(test_client, "userlogin@example.com", "password123")
>       assert b"Chef Dashboard" in response.data   # title сторінки шефа
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       assert b'Chef Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>'
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data

tests\test_routes.py:81: AssertionError
_____________________________________________________________________________________________________ test_logout ______________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

    def test_logout(test_client):
        user = create_test_user()
        login(test_client, "userlogin@example.com", "password123")
        response = test_client.get("/logout", follow_redirects=True)
>       assert b"Erfolgreich ausgeloggt" in response.data
E       assert b'Erfolgreich ausgeloggt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>'
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3473 bytes [200 OK]>.data

tests\test_routes.py:91: AssertionError
=================================================================================================== warnings summary =================================================================================================== 
tests/test_1_sqlite.py: 16 warnings
tests/test_models.py: 16 warnings
tests/test_routes.py: 6 warnings
  C:\Users\Praktikant\workspace\ze\.venv\Lib\site-packages\sqlalchemy\sql\schema.py:3624: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    return util.wrap_callable(lambda ctx: fn(), fn)  # type: ignore

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============================================================================================== short test summary info ================================================================================================ 
FAILED tests/test_routes.py::test_register_and_login - AssertionError: assert b'Teamleiter erfolgreich registriert' in b'<!doctype html>\n<html lang=en>\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entere...
FAILED tests/test_routes.py::test_dashboard_for_user - assert b'Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</butt...
FAILED tests/test_routes.py::test_dashboard_for_chef - assert b'Chef Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?<...
FAILED tests/test_routes.py::test_logout - assert b'Erfolgreich ausgeloggt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort ver...
====================================================================================== 4 failed, 10 passed, 38 warnings in 1.38s ======================================================================================= 