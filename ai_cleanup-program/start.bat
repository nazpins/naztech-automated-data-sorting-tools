@echo off
echo Creating a virtual environment...
python -m venv env

echo Activating the virtual environment...
call env\Scripts\activate

echo Installing required packages...
pip install transformers nltk

echo Running the AI Maintenance Utility...
python main.py

echo.
echo AI Maintenance Utility has finished running. Press any key to exit.
pause > nul
