@echo off
set /p target="Enter the target IP address: "
set /p start_port="Enter the starting port number: "
set /p end_port="Enter the ending port number: "
python scan_open_ports.py %target% %start_port% %end_port%
pause