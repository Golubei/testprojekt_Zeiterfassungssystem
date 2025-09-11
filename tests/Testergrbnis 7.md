(.venv) PS C:\Users\Praktikant\workspace> cd ye
cd : Der Pfad "C:\Users\Praktikant\workspace\ye" kann nicht gefunden werden, da er nicht vorhanden ist.
In Zeile:1 Zeichen:1
+ cd ye
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\Praktikant\workspace\ye:String) [Set-Location], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand
 
(.venv) PS C:\Users\Praktikant\workspace> cd ze
(.venv) PS C:\Users\Praktikant\workspace\ze> pytest
================================================================================================= test session starts ==================================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\Users\Praktikant\workspace\ze
collected 14 items                                                                                                                                                                                                      

tests\test_1_sqlite.py ....                                                                                                                                                                                       [ 28%]
tests\test_models.py ....                                                                                                                                                                                         [ 57%]
tests\test_routes.py .FFFF.                                                                                                                                                                                       [100%]

======================================================================================================= FAILURES =======================================================================================================
_____________________________________________________________________________________________ test_chef_register_and_login _____________________________________________________________________________________________

test_client = <FlaskClient <Flask 'main'>>

    def test_chef_register_and_login(test_client):
        # Реєстрація Chef
        response = test_client.post("/chef_register", data={
            "email": "chef@example.com",
            "first_name": "Chef",
            "last_name": "Test",
            "password": "pass123",
            "password2": "pass123"
        }, follow_redirects=True)
>       assert b"Teamleiter erfolgreich registriert" in response.data
E       assert b'Teamleiter erfolgreich registriert' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n           
 ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>'
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3481 bytes [200 OK]>.data

tests\test_routes.py:61: AssertionError
_______________________________________________________________________________________________ test_dashboard_for_user ________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

    def test_dashboard_for_user(test_client):
        create_test_user(role=UserRole.User)
        response = login(test_client, "userlogin@example.com", "password123")
>       assert b"Dashboard" in response.data
E       assert b'Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>'
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data

tests\test_routes.py:70: AssertionError
_______________________________________________________________________________________________ test_dashboard_for_chef ________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

    def test_dashboard_for_chef(test_client):
        create_test_user(role=UserRole.Chef)
        response = login(test_client, "userlogin@example.com", "password123")
>       assert b"Chef Dashboard" in response.data
E       assert b'Chef Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>'
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3470 bytes [200 OK]>.data

tests\test_routes.py:79: AssertionError
_____________________________________________________________________________________________________ test_logout ______________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

    def test_logout(test_client):
        create_test_user()
        login(test_client, "userlogin@example.com", "password123")
        response = test_client.get("/logout", follow_redirects=True)
>       assert b"Erfolgreich ausgeloggt" in response.data
E       assert b'Erfolgreich ausgeloggt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>'
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</button>\n        </form>\n    </div>\n</body>\n</html>' = <WrapperTestResponse 3473 bytes [200 OK]>.data

tests\test_routes.py:89: AssertionError
=================================================================================================== warnings summary =================================================================================================== 
tests/test_1_sqlite.py: 16 warnings
tests/test_models.py: 16 warnings
tests/test_routes.py: 6 warnings
  C:\Users\Praktikant\workspace\ze\.venv\Lib\site-packages\sqlalchemy\sql\schema.py:3624: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    return util.wrap_callable(lambda ctx: fn(), fn)  # type: ignore

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============================================================================================== short test summary info ================================================================================================ 
FAILED tests/test_routes.py::test_chef_register_and_login - assert b'Teamleiter erfolgreich registriert' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">...
FAILED tests/test_routes.py::test_dashboard_for_user - assert b'Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?</butt...
FAILED tests/test_routes.py::test_dashboard_for_chef - assert b'Chef Dashboard' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort vergessen?<...
FAILED tests/test_routes.py::test_logout - assert b'Erfolgreich ausgeloggt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Login</title>\n    <style>\n      ...ubmit();\n                }\n            ">Passwort ver...
====================================================================================== 4 failed, 10 passed, 38 warnings in 1.38s ======================================================================================= 