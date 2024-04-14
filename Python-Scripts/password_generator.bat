@echo off
set /p length="Enter the desired password length: "
python password_generator.py %length%
pause