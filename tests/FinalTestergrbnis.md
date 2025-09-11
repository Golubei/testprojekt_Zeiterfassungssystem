(.venv) PS C:\Users\Praktikant\workspace\ze> pytest
================================================================================================== test session starts ==================================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\Users\Praktikant\workspace\ze
collected 14 items                                                                                                                                                                                                       

tests\test_1_sqlite.py ....                                                                                                                                                                                        [ 28%]
tests\test_models.py ....                                                                                                                                                                                          [ 57%]
tests\test_routes.py ......                                                                                                                                                                                        [100%]

=================================================================================================== warnings summary ====================================================================================================
tests/test_1_sqlite.py: 16 warnings
tests/test_models.py: 16 warnings
tests/test_routes.py: 10 warnings
  C:\Users\Praktikant\workspace\ze\.venv\Lib\site-packages\sqlalchemy\sql\schema.py:3624: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    return util.wrap_callable(lambda ctx: fn(), fn)  # type: ignore

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================================================================ 14 passed, 42 warnings in 3.29s ============================================================================================