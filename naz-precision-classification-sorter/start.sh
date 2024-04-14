#!/bin/bash

echo "Checking and setting up the environment..."
if [ ! -d "env" ]; then
    python3 -m venv env
    echo "Environment created."
fi

source env/bin/activate
echo "Installing requirements..."
pip install tensorflow transformers pillow
echo "Requirements installed."

echo "Launching Sort with Precision..."
python3 sort-with-precision.py
