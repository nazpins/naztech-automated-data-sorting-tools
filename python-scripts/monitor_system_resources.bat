@echo off
set /p interval="Enter the monitoring interval (in seconds): "
python monitor_system_resources.py %interval%
pause