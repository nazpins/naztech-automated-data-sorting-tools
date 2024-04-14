#!/bin/bash
clear

# Check for Python and report if not installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi

# Set up virtual environment
echo "Setting up virtual environment..."
python3 -m venv env
source env/bin/activate

# Install necessary Python packages
echo "Installing required packages..."
pip install requests

# Run the script
echo "Running the script..."
python3 sort_docs.py
