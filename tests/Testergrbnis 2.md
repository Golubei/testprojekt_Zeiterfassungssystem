pytest
================================================================================================= test session starts ==================================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\Users\Praktikant\workspace\ze
collected 10 items                                                                                                                                                                                                      

tests\test_models.py ....                                                                                                                                                                                         [ 40%]
tests\test_routes.py ......                                                                                                                                                                                       [100%]

=================================================================================================== warnings summary ===================================================================================================
tests/test_models.py: 16 warnings
tests/test_routes.py: 8 warnings
  C:\Users\Praktikant\workspace\ze\.venv\Lib\site-packages\sqlalchemy\sql\schema.py:3624: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    return util.wrap_callable(lambda ctx: fn(), fn)  # type: ignore

tests/test_routes.py::test_register_and_login
tests/test_routes.py::test_dashboard_for_user
tests/test_routes.py::test_dashboard_for_user
tests/test_routes.py::test_dashboard_for_chef
tests/test_routes.py::test_dashboard_for_chef
tests/test_routes.py::test_logout
tests/test_routes.py::test_logout
  C:\Users\Praktikant\workspace\ze\main.py:28: LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    user = db.query(User).get(int(user_id))

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================================================================================== 10 passed, 31 warnings in 2.47s ============================================================================================