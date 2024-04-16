@echo off
echo Creating a virtual environment...
python -m venv env

echo Activating the virtual environment...
call env\Scripts\activate

echo Installing required packages...
pip install transformers nltk

echo Installing TensorFlow for deep learning capabilities...
pip install tensorflow

echo Optionally, you can uncomment the next line to install PyTorch instead of or in addition to TensorFlow
REM pip install torch torchvision torchaudio

echo Running the AI Maintenance Utility...
python main.py

echo.
echo AI Maintenance Utility has finished running. Press any key to exit.
pause > nul
