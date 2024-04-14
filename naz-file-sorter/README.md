# Naztech File Sorter

The Naztech File Sorter is a Python-based utility that helps you organize your files into categorized directories based on their type. It supports custom categorizations such as Documents, Pictures, Videos, and Audio. You can also choose whether to include datetime stamps in the filenames.

## Features

- Categorizes files into Documents, Pictures, Videos, Audio, and Others
- Option to append datetime to filenames for better version management
- Places sorted files within a 'SortedFiles' directory inside the chosen directory

## Prerequisites

Ensure you have Python installed on your machine. This script has been tested with Python 3.8 and above.

## Setup

To set up the script, clone this repository or download the files directly into a directory of your choice.

## Installation

No additional libraries are required to run the script as it uses built-in Python modules. If you encounter any issues, you may need to ensure your Python installation is correct and includes the standard library.

## Usage

### Windows

1. Make sure you have Python installed on your system.
2. Download the `sort_files.py` script.
3. Open a command prompt and navigate to the directory where the script is located.
4. Run the script by executing the following command:
   ```
   python sort_files.py
   ```
5. Follow the prompts to specify the directory you want to sort and whether to include datetime in the filenames.

### Linux

1. Make sure you have Python installed on your system.
2. Download the `sort_files.py` script and the `start.sh` file.
3. Open a terminal and navigate to the directory where the script and shell file are located.
4. Make the shell file executable by running the following command:
   ```
   chmod +x start.sh
   ```
5. Run the script by executing the following command:
   ```
   ./start.sh
   ```
6. Follow the prompts to specify the directory you want to sort and whether to include datetime in the filenames.

## Warning

Please note that the script modifies the structure of the directory you specify by organizing files into folders. It is highly recommended to back up your data before running the script to avoid any unintended loss or modification of files.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

NAZTECH Doc Sorter is developed by nazpins (https://github.com/nazpins).

Feel free to contribute to the project by submitting pull requests or reporting issues on the [GitHub repository](https://github.com/nazpins/naz-doc-sorter).