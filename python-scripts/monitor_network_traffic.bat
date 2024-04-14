@echo off
set /p interval="Enter the monitoring interval (in seconds): "
python monitor_network_traffic.py %interval%
pause