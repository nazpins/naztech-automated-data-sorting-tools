#!/bin/bash

# Prompt the user for the directory path
read -p "Enter the directory path: " directory

# Run the Python script with the provided directory path
python3 organize_files_by_type.py "$directory"

read -p "Press Enter to exit..."