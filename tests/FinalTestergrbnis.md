(.venv) PS C:\Users\Praktikant\workspace\ze> pytest
============================================================================================= test session starts ==============================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
benchmark: 5.1.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: C:\Users\Praktikant\workspace\ze
plugins: benchmark-5.1.0
collected 21 items                                                                                                                                                                                              

tests\test_1_sqlite.py ....                                                                                                                                                                               [ 19%]
tests\test_api.py .                                                                                                                                                                                       [ 23%]
tests\test_models.py ....                                                                                                                                                                                 [ 42%]
tests\test_performance.py .                                                                                                                                                                               [ 47%]
tests\test_routes.py ......                                                                                                                                                                               [ 76%]
tests\test_security.py .....                                                                                                                                                                              [100%]

=============================================================================================== warnings summary ===============================================================================================
tests/test_1_sqlite.py: 16 warnings
tests/test_models.py: 16 warnings
tests/test_performance.py: 2 warnings
tests/test_routes.py: 10 warnings
tests/test_security.py: 4 warnings
  C:\Users\Praktikant\workspace\ze\.venv\Lib\site-packages\sqlalchemy\sql\schema.py:3624: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    return util.wrap_callable(lambda ctx: fn(), fn)  # type: ignore

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

---------------------------------------------- benchmark: 1 tests ---------------------------------------------
Name (time in ms)          Min      Max    Mean  StdDev  Median     IQR  Outliers       OPS  Rounds  Iterations
---------------------------------------------------------------------------------------------------------------
test_dashboard_perf     1.6669  18.3774  2.9902  2.0986  2.4112  1.2717       6;6  334.4213     111           1
---------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================== 21 passed, 48 warnings in 64.61s (0:01:04) ==================================================================================