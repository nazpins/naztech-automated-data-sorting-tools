@echo off
set /p process_name="Enter the process name to monitor: "
set /p interval="Enter the monitoring interval (in seconds): "
python monitor_process_memory.py %process_name% %interval%
pause