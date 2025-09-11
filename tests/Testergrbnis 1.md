 PS C:\Users\Praktikant\workspace\ze> pip install pytest
Collecting pytest
  Downloading pytest-8.4.2-py3-none-any.whl.metadata (7.7 kB)
Requirement already satisfied: colorama>=0.4 in c:\users\praktikant\workspace\ze\.venv\lib\site-packages (from pytest) (0.4.6)
Collecting iniconfig>=1 (from pytest)
  Downloading iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Requirement already satisfied: packaging>=20 in c:\users\praktikant\workspace\ze\.venv\lib\site-packages (from pytest) (25.0)
Collecting pluggy<2,>=1.5 (from pytest)
  Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting pygments>=2.7.2 (from pytest)
  Using cached pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Downloading pytest-8.4.2-py3-none-any.whl (365 kB)
Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
Downloading iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Using cached pygments-2.19.2-py3-none-any.whl (1.2 MB)
Installing collected packages: pygments, pluggy, iniconfig, pytest
Successfully installed iniconfig-2.1.0 pluggy-1.6.0 pygments-2.19.2 pytest-8.4.2                                                                                                                                         
(.venv) PS C:\Users\Praktikant\workspace\ze> pytest
================================================================================================= test session starts ==================================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\Users\Praktikant\workspace\ze
collected 0 items / 2 errors                                                                                                                                                                                            

======================================================================================================== ERRORS ========================================================================================================
________________________________________________________________________________________ ERROR collecting tests/test_models.py _________________________________________________________________________________________ 
ImportError while importing test module 'C:\Users\Praktikant\workspace\ze\tests\test_models.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\test_models.py:2: in <module>
    from models import User, UserRole, Client, Zeitbuchung, AuditLog
E   ModuleNotFoundError: No module named 'models'
________________________________________________________________________________________ ERROR collecting tests/test_routes.py _________________________________________________________________________________________ 
ImportError while importing test module 'C:\Users\Praktikant\workspace\ze\tests\test_routes.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\test_routes.py:2: in <module>
    from main import app
E   ModuleNotFoundError: No module named 'main'
=============================================================================================== short test summary info ================================================================================================ 
ERROR tests/test_models.py
ERROR tests/test_routes.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 2 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
================================================================================================== 2 errors in 0.17s =================================================================================================== 
(.venv) PS C:\Users\Praktikant\workspace\ze> pytest
================================================================================================= test session starts ==================================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\Users\Praktikant\workspace\ze
collected 10 items                                                                                                                                                                                                      

tests\test_models.py ...F                                                                                                                                                                                         [ 40%]
tests\test_routes.py .FFF..                                                                                                                                                                                       [100%]

======================================================================================================= FAILURES =======================================================================================================
____________________________________________________________________________________________________ test_audit_log ____________________________________________________________________________________________________

self = <sqlalchemy.engine.base.Connection object at 0x0000020E90207590>, dialect = <sqlalchemy.dialects.sqlite.pysqlite.SQLiteDialect_pysqlite object at 0x0000020E80B734D0>
context = <sqlalchemy.dialects.sqlite.base.SQLiteExecutionContext object at 0x0000020E90476C10>, statement = <sqlalchemy.dialects.sqlite.base.SQLiteCompiler object at 0x0000020E90353750>
parameters = [(1, None, '2025-09-11 08:20:02.720081', None, 'audit', '2025-09-11 06:20:02.720476', ...)]

    def _exec_single_context(
        self,
        dialect: Dialect,
        context: ExecutionContext,
        statement: Union[str, Compiled],
        parameters: Optional[_AnyMultiExecuteParams],
    ) -> CursorResult[Any]:
        """continue the _execute_context() method for a single DBAPI
        cursor.execute() or cursor.executemany() call.
    
        """
        if dialect.bind_typing is BindTyping.SETINPUTSIZES:
            generic_setinputsizes = context._prepare_set_input_sizes()

            if generic_setinputsizes:
                try:
                    dialect.do_set_input_sizes(
                        context.cursor, generic_setinputsizes, context
                    )
                except BaseException as e:
                    self._handle_dbapi_exception(
                        e, str(statement), parameters, None, context
                    )

        cursor, str_statement, parameters = (
            context.cursor,
            context.statement,
            context.parameters,
        )

        effective_parameters: Optional[_AnyExecuteParams]

        if not context.executemany:
            effective_parameters = parameters[0]
        else:
            effective_parameters = parameters

        if self._has_events or self.engine._has_events:
            for fn in self.dispatch.before_cursor_execute:
                str_statement, effective_parameters = fn(
                    self,
                    cursor,
                    str_statement,
                    effective_parameters,
                    context,
                    context.executemany,
                )

        if self._echo:
            self._log_info(str_statement)

            stats = context._get_cache_stats()

            if not self.engine.hide_parameters:
                self._log_info(
                    "[%s] %r",
                    stats,
                    sql_util._repr_params(
                        effective_parameters,
                        batches=10,
                        ismulti=context.executemany,
                    ),
                )
            else:
                self._log_info(
                    "[%s] [SQL parameters hidden due to hide_parameters=True]",
                    stats,
                )

        evt_handled: bool = False
        try:
            if context.execute_style is ExecuteStyle.EXECUTEMANY:
                effective_parameters = cast(
                    "_CoreMultiExecuteParams", effective_parameters
                )
                if self.dialect._has_events:
                    for fn in self.dialect.dispatch.do_executemany:
                        if fn(
                            cursor,
                            str_statement,
                            effective_parameters,
                            context,
                        ):
                            evt_handled = True
                            break
                if not evt_handled:
                    self.dialect.do_executemany(
                        cursor,
                        str_statement,
                        effective_parameters,
                        context,
                    )
            elif not effective_parameters and context.no_parameters:
                if self.dialect._has_events:
                    for fn in self.dialect.dispatch.do_execute_no_params:
                        if fn(cursor, str_statement, context):
                            evt_handled = True
                            break
                if not evt_handled:
                    self.dialect.do_execute_no_params(
                        cursor, str_statement, context
                    )
            else:
                effective_parameters = cast(
                    "_CoreSingleExecuteParams", effective_parameters
                )
                if self.dialect._has_events:
                    for fn in self.dialect.dispatch.do_execute:
                        if fn(
                            cursor,
                            str_statement,
                            effective_parameters,
                            context,
                        ):
                            evt_handled = True
                            break
                if not evt_handled:
>                   self.dialect.do_execute(
                        cursor, str_statement, effective_parameters, context
                    )

.venv\Lib\site-packages\sqlalchemy\engine\base.py:1967:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <sqlalchemy.dialects.sqlite.pysqlite.SQLiteDialect_pysqlite object at 0x0000020E80B734D0>, cursor = <sqlite3.Cursor object at 0x0000020E9045ED40>
statement = 'INSERT INTO zeitbuchungen (user_id, client_id, start_time, end_time, comment, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)'
parameters = (1, None, '2025-09-11 08:20:02.720081', None, 'audit', '2025-09-11 06:20:02.720476', ...), context = <sqlalchemy.dialects.sqlite.base.SQLiteExecutionContext object at 0x0000020E90476C10>

    def do_execute(self, cursor, statement, parameters, context=None):
>       cursor.execute(statement, parameters)
E       sqlite3.IntegrityError: NOT NULL constraint failed: zeitbuchungen.client_id

.venv\Lib\site-packages\sqlalchemy\engine\default.py:951: IntegrityError

The above exception was the direct cause of the following exception:

db_session = <sqlalchemy.orm.session.Session object at 0x0000020E9047C640>

    def test_audit_log(db_session):
        user = User(
            email="audit@example.com",
            hashed_password="pass",
            role=UserRole.Chef,
            first_name="Audit",
            last_name="Master",
            active=True
        )
        db_session.add(user)
        db_session.commit()
        zb = Zeitbuchung(
            user_id=user.id,
            client_id=None,
            start_time=datetime.now(),
            comment="audit"
        )
        db_session.add(zb)
>       db_session.commit()

tests\test_models.py:92:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
.venv\Lib\site-packages\sqlalchemy\orm\session.py:2032: in commit
    trans.commit(_to_root=True)
<string>:2: in commit
    ???
.venv\Lib\site-packages\sqlalchemy\orm\state_changes.py:137: in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
.venv\Lib\site-packages\sqlalchemy\orm\session.py:1313: in commit
    self._prepare_impl()
<string>:2: in _prepare_impl
    ???
.venv\Lib\site-packages\sqlalchemy\orm\state_changes.py:137: in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
.venv\Lib\site-packages\sqlalchemy\orm\session.py:1288: in _prepare_impl
    self.session.flush()
.venv\Lib\site-packages\sqlalchemy\orm\session.py:4345: in flush
    self._flush(objects)
.venv\Lib\site-packages\sqlalchemy\orm\session.py:4480: in _flush
    with util.safe_reraise():
         ^^^^^^^^^^^^^^^^^^^
.venv\Lib\site-packages\sqlalchemy\util\langhelpers.py:224: in __exit__
    raise exc_value.with_traceback(exc_tb)
.venv\Lib\site-packages\sqlalchemy\orm\session.py:4441: in _flush
    flush_context.execute()
.venv\Lib\site-packages\sqlalchemy\orm\unitofwork.py:466: in execute
    rec.execute(self)
.venv\Lib\site-packages\sqlalchemy\orm\unitofwork.py:642: in execute
    util.preloaded.orm_persistence.save_obj(
.venv\Lib\site-packages\sqlalchemy\orm\persistence.py:93: in save_obj
    _emit_insert_statements(
.venv\Lib\site-packages\sqlalchemy\orm\persistence.py:1233: in _emit_insert_statements
    result = connection.execute(
.venv\Lib\site-packages\sqlalchemy\engine\base.py:1419: in execute
    return meth(
.venv\Lib\site-packages\sqlalchemy\sql\elements.py:526: in _execute_on_connection
    return connection._execute_clauseelement(
.venv\Lib\site-packages\sqlalchemy\engine\base.py:1641: in _execute_clauseelement
    ret = self._execute_context(
.venv\Lib\site-packages\sqlalchemy\engine\base.py:1846: in _execute_context
    return self._exec_single_context(
.venv\Lib\site-packages\sqlalchemy\engine\base.py:1986: in _exec_single_context
    self._handle_dbapi_exception(
.venv\Lib\site-packages\sqlalchemy\engine\base.py:2355: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
.venv\Lib\site-packages\sqlalchemy\engine\base.py:1967: in _exec_single_context
    self.dialect.do_execute(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <sqlalchemy.dialects.sqlite.pysqlite.SQLiteDialect_pysqlite object at 0x0000020E80B734D0>, cursor = <sqlite3.Cursor object at 0x0000020E9045ED40>
statement = 'INSERT INTO zeitbuchungen (user_id, client_id, start_time, end_time, comment, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)'
parameters = (1, None, '2025-09-11 08:20:02.720081', None, 'audit', '2025-09-11 06:20:02.720476', ...), context = <sqlalchemy.dialects.sqlite.base.SQLiteExecutionContext object at 0x0000020E90476C10>

    def do_execute(self, cursor, statement, parameters, context=None):
>       cursor.execute(statement, parameters)
E       sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) NOT NULL constraint failed: zeitbuchungen.client_id
E       [SQL: INSERT INTO zeitbuchungen (user_id, client_id, start_time, end_time, comment, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)]
E       [parameters: (1, None, '2025-09-11 08:20:02.720081', None, 'audit', '2025-09-11 06:20:02.720476', '2025-09-11 06:20:02.720483')]
E       (Background on this error at: https://sqlalche.me/e/20/gkpj)

.venv\Lib\site-packages\sqlalchemy\engine\default.py:951: IntegrityError
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
        assert b"Teamleiter erfolgreich registriert" in response.data

        # Логін Chef
        response = login(test_client, "chef@example.com", "pass123")
>       assert b"Erfolgreich eingeloggt" in response.data
E       assert b'Erfolgreich eingeloggt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Chef Dashboard</title>\n    <style... || \'\'));\n        }\n    })\n    .catch(e=>alert("Technischer Fehler: " + e));\n};\n    </script>\n</body>\n</html>'
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Chef Dashboard</title>\n    <style... || \'\'));\n        }\n    })\n    .catch(e=>alert("Technischer Fehler: " + e));\n};\n    </script>\n</body>\n</html>' = <WrapperTestResponse 24730 bytes [200 OK]>.data

tests\test_routes.py:61: AssertionError
_______________________________________________________________________________________________ test_dashboard_for_user ________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

    def test_dashboard_for_user(test_client):
        user = create_test_user(role=UserRole.User)
        response = login(test_client, "userlogin@example.com", "password123")
>       assert b"Erfolgreich eingeloggt" in response.data
E       assert b'Erfolgreich eingeloggt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Dashboard</title>\n    <style>\n  ...rror || \'\'));\n        }\n    })\n    .catch(e=>alert("Technischer Fehler: " + e));\n};\n</script>\n</body>\n</html>'
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Dashboard</title>\n    <style>\n  ...rror || \'\'));\n        }\n    })\n    .catch(e=>alert("Technischer Fehler: " + e));\n};\n</script>\n</body>\n</html>' = <WrapperTestResponse 23998 bytes [200 OK]>.data

tests\test_routes.py:66: AssertionError
_______________________________________________________________________________________________ test_dashboard_for_chef ________________________________________________________________________________________________ 

test_client = <FlaskClient <Flask 'main'>>

    def test_dashboard_for_chef(test_client):
        chef = create_test_user(role=UserRole.Chef)
        response = login(test_client, "userlogin@example.com", "password123")
>       assert b"Erfolgreich eingeloggt" in response.data
E       assert b'Erfolgreich eingeloggt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Chef Dashboard</title>\n    <style... || \'\'));\n        }\n    })\n    .catch(e=>alert("Technischer Fehler: " + e));\n};\n    </script>\n</body>\n</html>'
E        +  where b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Chef Dashboard</title>\n    <style... || \'\'));\n        }\n    })\n    .catch(e=>alert("Technischer Fehler: " + e));\n};\n    </script>\n</body>\n</html>' = <WrapperTestResponse 24732 bytes [200 OK]>.data

tests\test_routes.py:75: AssertionError
=================================================================================================== warnings summary =================================================================================================== 
tests/test_models.py: 14 warnings
tests/test_routes.py: 8 warnings
  C:\Users\Praktikant\workspace\ze\.venv\Lib\site-packages\sqlalchemy\sql\schema.py:3624: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    return util.wrap_callable(lambda ctx: fn(), fn)  # type: ignore

tests/test_routes.py::test_register_and_login
tests/test_routes.py::test_dashboard_for_user
tests/test_routes.py::test_dashboard_for_chef
tests/test_routes.py::test_logout
tests/test_routes.py::test_logout
  C:\Users\Praktikant\workspace\ze\main.py:28: LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    user = db.query(User).get(int(user_id))

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============================================================================================== short test summary info ================================================================================================ 
FAILED tests/test_models.py::test_audit_log - sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) NOT NULL constraint failed: zeitbuchungen.client_id
FAILED tests/test_routes.py::test_register_and_login - assert b'Erfolgreich eingeloggt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Chef Dashboard</title>\n    <style... || \'\'));\n        }\n    })\n    .catch(e=>alert("Te...
FAILED tests/test_routes.py::test_dashboard_for_user - assert b'Erfolgreich eingeloggt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Dashboard</title>\n    <style>\n  ...rror || \'\'));\n        }\n    })\n    .catch(e=>alert...
FAILED tests/test_routes.py::test_dashboard_for_chef - assert b'Erfolgreich eingeloggt' in b'<!DOCTYPE html>\n<html lang="de">\n<head>\n    <meta charset="UTF-8">\n    <title>Chef Dashboard</title>\n    <style... || \'\'));\n        }\n    })\n    .catch(e=>alert("Te...
======================================================================================= 4 failed, 6 passed, 27 warnings in 4.33s ======================================================================================= 