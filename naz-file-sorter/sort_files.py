import os
import shutil
import webbrowser
from datetime import datetime

def fallback_name(original_name, extension, include_datetime):
    if include_datetime:
        timestamp = datetime.now().strftime("_%Y%m%d%H%M%S")
        return f"{original_name}{timestamp}{extension}"
    else:
        return f"{original_name}{extension}"

def categorize_and_move(file_path, base_dir):
    _, extension = os.path.splitext(file_path)
    file_type = extension.lower()
    if file_type in ['.docx', '.doc', '.txt', '.pdf']:
        category = 'Documents'
    elif file_type in ['.jpg', '.jpeg', '.png', '.gif']:
        category = 'Pictures'
    elif file_type in ['.mp3', '.wav', '.aac']:
        category = 'Audio'
    elif file_type in ['.mp4', '.avi', '.mov']:
        category = 'Videos'
    else:
        category = 'Others'  # Additional category for unmatched types

    target_dir = os.path.join(base_dir, category, file_type.replace('.', ''))
    os.makedirs(target_dir, exist_ok=True)
    target_file_path = os.path.join(target_dir, os.path.basename(file_path))
    shutil.move(file_path, target_file_path)

def main():
    print("\033c", end="")  # ANSI escape code to clear the screen
    print("\033[1;34mNAZTECH FILE SORTER STARTED...\033[0m")
    print("\033[1;31;47mWARNING: BACK UP YOUR DATA FIRST\033[0m")  # Bold, red text on white background
    print("\033[1;33m" + "="*80 + "\033[0m")  # Yellow bold delimiters
    print("\033[1;33mThis script will modify the structure of the directory you specify by organizing files into folders.\033[0m")
    print("\033[1;33m" + "="*80 + "\033[0m")  # Yellow bold delimiters

    include_datetime = input("\n\033[1;32mDo you want to include datetime in file names? (Y/N): \033[0m").strip().upper() == 'Y'
    directory_to_sort = input("\033[1;32mPlease enter the full path to the directory you wish to sort: \033[0m").strip()
    sorted_files_path = os.path.join(directory_to_sort, 'SortedFiles')  # 'SortedFiles' within the user-specified directory

    for root, dirs, files in os.walk(directory_to_sort, topdown=False):  # Ensure we do not rearrange as we walk
        for file in files:
            file_path = os.path.join(root, file)
            if 'SortedFiles' not in root:  # Avoid re-sorting already sorted files
                original_name, extension = os.path.splitext(file)
                new_name = fallback_name(original_name, extension, include_datetime)
                new_file_path = os.path.join(root, new_name)
                os.rename(file_path, new_file_path)
                categorize_and_move(new_file_path, sorted_files_path)

    print("\033[1;36mFiles have been organized. Access your sorted files at: " + sorted_files_path + "\033[0m")
    try:
        webbrowser.open(f'file://{sorted_files_path}')  # Opens the folder in the file explorer
        print("\033[1;35mOpening the sorted files directory...\033[0m")
    except Exception as e:
        print("\033[1;31mCould not open the folder automatically, please navigate to it manually.\033[0m")

if __name__ == "__main__":
    main()
