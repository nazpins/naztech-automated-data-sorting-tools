@echo off
echo Checking and setting up the environment for GPU...
CALL conda activate tf_gpu

echo Launching Sort with Precision on GPU...
python sort-with-precision.py
pause