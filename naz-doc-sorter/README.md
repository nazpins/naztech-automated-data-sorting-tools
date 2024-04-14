# Naztech Doc Sorter

## Overview
This script organizes your documents by renaming them according to metadata fetched from the Google Books API and sorting them into folders named after the authors.

## Setup
1. Ensure Python is installed on your system.
2. Clone this repository or download the scripts.
3. Run `start.sh` (Linux/Mac) or `start.bat` (Windows) to set up the environment and start the script.

## Usage
1. Run the `start` script corresponding to your operating system.
2. Enter your Google Books API key when prompted.
3. Enter the full path to the directory containing the documents to sort.
4. Choose whether to include the datetime in the filenames.
5. The script will process the files and organize them into author-specific folders.

## Dependencies
- requests

## Warning
Please back up your data before running this script as it will reorganize your files and directories.
