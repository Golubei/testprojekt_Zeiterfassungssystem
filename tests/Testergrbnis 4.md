.venv) PS C:\Users\Praktikant\workspace\ze> pytest
================================================================================================= test session starts ==================================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\Users\Praktikant\workspace\ze
collected 14 items                                                                                                                                                                                                      

tests\test_1_sqlite.py ....                                                                                                                                                                                       [ 28%]
tests\test_models.py ....                                                                                                                                                                                         [ 57%]
tests\test_routes.py EEEEEE                                                                                                                                                                                       [100%]

======================================================================================================== ERRORS ========================================================================================================
________________________________________________________________________________________ ERROR at setup of test_index_redirect _________________________________________________________________________________________
file C:\Users\Praktikant\workspace\ze\tests\test_routes.py, line 49
  def test_index_redirect(test_client):
E       fixture 'test_client' not found
>       available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, db_session, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\Users\Praktikant\workspace\ze\tests\test_routes.py:49
______________________________________________________________________________________ ERROR at setup of test_register_and_login _______________________________________________________________________________________ 
file C:\Users\Praktikant\workspace\ze\tests\test_routes.py, line 54
  def test_register_and_login(test_client):
E       fixture 'test_client' not found
>       available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, db_session, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\Users\Praktikant\workspace\ze\tests\test_routes.py:54
______________________________________________________________________________________ ERROR at setup of test_dashboard_for_user _______________________________________________________________________________________ 
file C:\Users\Praktikant\workspace\ze\tests\test_routes.py, line 69
  def test_dashboard_for_user(test_client):
E       fixture 'test_client' not found
>       available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, db_session, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\Users\Praktikant\workspace\ze\tests\test_routes.py:69
______________________________________________________________________________________ ERROR at setup of test_dashboard_for_chef _______________________________________________________________________________________ 
file C:\Users\Praktikant\workspace\ze\tests\test_routes.py, line 78
  def test_dashboard_for_chef(test_client):
E       fixture 'test_client' not found
>       available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, db_session, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\Users\Praktikant\workspace\ze\tests\test_routes.py:78
____________________________________________________________________________________________ ERROR at setup of test_logout _____________________________________________________________________________________________ 
file C:\Users\Praktikant\workspace\ze\tests\test_routes.py, line 87
  def test_logout(test_client):
E       fixture 'test_client' not found
>       available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, db_session, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\Users\Praktikant\workspace\ze\tests\test_routes.py:87
____________________________________________________________________________________________ ERROR at setup of test_test123 ____________________________________________________________________________________________ 
file C:\Users\Praktikant\workspace\ze\tests\test_routes.py, line 93
  def test_test123(test_client):
E       fixture 'test_client' not found
>       available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, db_session, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

C:\Users\Praktikant\workspace\ze\tests\test_routes.py:93
=================================================================================================== warnings summary =================================================================================================== 
tests/test_1_sqlite.py: 16 warnings
tests/test_models.py: 16 warnings
  C:\Users\Praktikant\workspace\ze\.venv\Lib\site-packages\sqlalchemy\sql\schema.py:3624: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    return util.wrap_callable(lambda ctx: fn(), fn)  # type: ignore

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============================================================================================== short test summary info ================================================================================================ 
ERROR tests/test_routes.py::test_index_redirect
ERROR tests/test_routes.py::test_register_and_login
ERROR tests/test_routes.py::test_dashboard_for_user
ERROR tests/test_routes.py::test_dashboard_for_chef
ERROR tests/test_routes.py::test_logout
ERROR tests/test_routes.py::test_test123
======================================================================================= 8 passed, 32 warnings, 6 errors in 0.83s =======================================================================================