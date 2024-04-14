#!/bin/bash
# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python could not be found. Please install Python 3."
    exit
fi

# Run the sorter script
echo "Running naz-file-sorter..."
python3 sort_files.py
