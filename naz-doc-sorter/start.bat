@echo off
cls

:: Check for Python and report if not installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python.
    pause
    exit /b
)

:: Set up virtual environment
echo Setting up virtual environment...
python -m venv env
call env\Scripts\activate

:: Install necessary Python packages
echo Installing required packages...
pip install requests

:: Run the script
echo Running the script...
python sort_docs.py
pause
