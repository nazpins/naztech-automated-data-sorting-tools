#!/bin/bash

echo "Enter the path of the folder with duplicate images:"
read folder_path

echo "Creating Python Virtual Environment..."
python -m venv venv
source venv/bin/activate

echo "Installing necessary libraries..."
pip install Pillow imagehash

echo "Running duplicate removal script..."
python remove_duplicates.py "$folder_path"

if [ -d venv ]; then
    deactivate
fi

echo "Results have been logged in 'duplicate_log.txt'."
echo "Done."
read -p "Press enter to continue..."
