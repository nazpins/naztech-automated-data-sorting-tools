```markdown
# naz-file-sorter

The naz-file-sorter is a Python-based utility that helps you organize your files into categorized directories based on their type. It supports custom categorizations such as Documents, Pictures, Videos, and Audio. You can also choose whether to include datetime stamps in the filenames.

## Features

- Categorizes files into Documents, Pictures, Videos, Audio, and Others.
- Option to append datetime to filenames for better version management.
- Places sorted files within a 'SortedFiles' directory inside the chosen directory.

## Prerequisites

Ensure you have Python installed on your machine. This script has been tested with Python 3.8 and above.

## Setup

To set up the script, clone this repository or download the files directly into a directory of your choice.

## Installation

No additional libraries are required to run the script as it uses built-in Python modules. If you encounter any issues, you may need to ensure your Python installation is correct and includes the standard library.

## Usage

### Windows

To use the script on Windows, navigate to the directory containing `sort_files.py` and run the following command in your command prompt:

```cmd
python sort_files.py
```

### Linux

To use the script on Linux, navigate to the directory containing `sort_files.py` and run the following commands in your terminal:

```bash
chmod +x start.sh
./start.sh
```

Follow the prompts in the terminal to specify the directory you want to sort and whether to include datetime in the filenames.

## Warning

This script will modify the directories and files in the path you specify. Ensure you have backups of your data before running this script.

## Contribution

Contributions are welcome. Please fork this repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

