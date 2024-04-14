# Naztech File Sorter Lite

Naztech File Sorter Lite is a program that helps you organize files in a directory by sorting them into folders based on their file extensions. It provides a simple and efficient way to keep your files organized and easily accessible.

## Features

- Automatically sorts files into predefined folders based on their file extensions
- Supports a wide range of file types, including images, documents, audio, videos, applications, and archives
- Moves files with unknown extensions to an 'Other' folder
- Provides a user-friendly interface with clear prompts and messages
- Opens the sorted files directory automatically after the sorting process is complete

## Usage

1. Make sure you have Python installed on your system.
2. Download the `organize_files_by_type.py` script. 
    - You can also use the start.bat file to start the program at this point and skip the steps below.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script by executing the following command: python organize_files_by_type.py
5. When prompted, enter the path to the directory you want to sort.
6. The script will organize the files in the specified directory into folders based on their file extensions.
7. Once the sorting process is complete, the script will automatically open the sorted files directory.

## Warning

Please note that the script modifies the structure of the directory you specify by organizing files into folders. It is highly recommended to back up your data before running the script to avoid any unintended loss or modification of files.

## Supported File Types

The script supports the following file types:

- Images: .jpg, .jpeg, .png, .gif, .bmp
- Documents: .txt, .doc, .docx, .pdf, .xlsx, .csv, .md, .epub, .mobi
- Audio: .mp3, .wav, .flac, .aac
- Videos: .mp4, .avi, .mkv, .mov
- Applications: .exe, .msi
- Archives: .zip, .rar, .7z, .tar, .gz

Files with extensions not listed above will be moved to the 'Other' folder.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Naztech File Sorter Lite is developed by nazpins (https://github.com/nazpins).

Feel free to contribute to the project by submitting pull requests or reporting issues on the [GitHub repository](https://github.com/nazpins/naztech-software/tree/main/naz-file-sorter-lite).