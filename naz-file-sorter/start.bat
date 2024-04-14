@echo off
echo Setting up the environment...
python -m venv env
call env\Scripts\activate
pip install requests
echo Environment setup complete.
echo Running sort_files.py...
python sort_files.py
echo sort_files.py has finished running.
pause
