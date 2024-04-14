@echo off
echo Checking and setting up the environment for CPU...
CALL conda activate tf_cpu

echo Launching Sort with Precision on CPU...
python sort-with-precision.py
pause