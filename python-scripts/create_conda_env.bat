@echo off
set /p env_name="Enter the name of the Conda environment: "
python create_conda_env.py %env_name%
pause