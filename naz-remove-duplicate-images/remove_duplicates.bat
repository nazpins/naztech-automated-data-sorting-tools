
@echo off
echo Enter the path of the folder with duplicate images:
set /p folder_path=

echo Creating Python Virtual Environment...
python -m venv venv
call venv\Scripts\activate

echo Installing necessary libraries...
pip install Pillow imagehash

echo Running duplicate removal script...
python remove_duplicates.py "%folder_path%"

if exist venv call venv\Scripts\deactivate
echo Results have been logged in 'duplicate_log.txt'.
echo Done.
pause
