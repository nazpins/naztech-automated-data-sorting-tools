@echo off
echo Checking and setting up the environment...
IF NOT EXIST "env" (
    python -m venv env
    echo Environment created.
)

call env\Scripts\activate
echo Installing requirements...
pip install tensorflow transformers pillow
echo Requirements installed.

echo Launching Sort with Precision...
python sort-with-precision.py
pause
