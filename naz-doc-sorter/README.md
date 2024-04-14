# Naztech Doc Sorter

Naztech Doc Sorter is a program that organizes your documents by renaming them according to metadata fetched from the Google Books API and sorting them into folders named after the authors.

## Features

- Renames documents based on metadata from the Google Books API
- Organizes documents into folders named after the authors
- Provides a user-friendly interface with prompts for setup and usage

## Setup

1. Make sure you have Python installed on your system.
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

Please note that the script modifies the structure of the directory you specify by organizing files into folders. It is highly recommended to back up your data before running the script to avoid any unintended loss or modification of files.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Naztech Doc Sorter is developed by nazpins (https://github.com/nazpins).

Feel free to contribute to the project by submitting pull requests or reporting issues on the [GitHub repository](https://github.com/nazpins/naztech-software/tree/main/naz-doc-sorter).