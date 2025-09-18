(.venv) PS C:\Users\Praktikant\workspace\ze> pytest
============================================================================================= test session starts ==============================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
benchmark: 5.1.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: C:\Users\Praktikant\workspace\ze
plugins: benchmark-5.1.0
collected 30 items                                                                                                                                                                                              

tests\test_1_sqlite.py ....                                                                                                                                                                               [ 13%]
tests\test_api.py .                                                                                                                                                                                       [ 16%]
tests\test_models.py ....                                                                                                                                                                                 [ 30%]
tests\test_performance.py .                                                                                                                                                                               [ 33%]
tests\test_routes.py ......                                                                                                                                                                               [ 53%]
tests\test_security.py .....                                                                                                                                                                              [ 70%]
tests\test_utils.py .........                                                                                                                                                                             [100%]


--------------------------------------------- benchmark: 1 tests ---------------------------------------------
Name (time in ms)          Min     Max    Mean  StdDev  Median     IQR  Outliers       OPS  Rounds  Iterations
--------------------------------------------------------------------------------------------------------------
test_dashboard_perf     1.5488  4.3587  1.6053  0.2617  1.5637  0.0202      2;17  622.9532     119           1
--------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean