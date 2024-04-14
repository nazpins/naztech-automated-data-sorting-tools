@echo off

REM Prompt the user for the directory path
set /p directory="Enter the directory path: "

REM Run the Python script with the provided directory path
python organize_files_by_type.py "%directory%"

pause