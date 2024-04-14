import os
import shutil
import webbrowser

def organize_files_by_type(directory):
    # Dictionary to store the mapping of file extensions to folder names
    extension_folders = {
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.bmp': 'Images',
        '.txt': 'Documents',
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.pdf': 'Documents',
        '.xlsx': 'Documents',
        '.csv': 'Documents',
        '.md': 'Documents',
        '.epub': 'Documents',
        '.mobi': 'Documents',
        '.mp3': 'Audio',
        '.wav': 'Audio',
        '.flac': 'Audio',
        '.aac': 'Audio',
        '.mp4': 'Videos',
        '.avi': 'Videos',
        '.mkv': 'Videos',
        '.mov': 'Videos',
        '.exe': 'Applications',
        '.msi': 'Applications',
        '.zip': 'Archives',
        '.rar': 'Archives',
        '.7z': 'Archives',
        '.tar': 'Archives',
        '.gz': 'Archives'
    }

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if the item is a file
        if os.path.isfile(file_path):
            # Get the file extension
            _, extension = os.path.splitext(filename)
            extension = extension.lower()
            
            # Check if the file extension exists in the mapping
            if extension in extension_folders:
                # Get the destination folder name
                folder_name = extension_folders[extension]
                
                # Create the destination folder if it doesn't exist
                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                
                # Move the file to the destination folder
                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {folder_name} folder.")
            else:
                # Create an 'Other' folder for files with unknown extensions
                other_folder = os.path.join(directory, 'Other')
                os.makedirs(other_folder, exist_ok=True)
                
                # Move the file to the 'Other' folder
                destination_path = os.path.join(other_folder, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to Other folder.")
        else:
            print(f"{filename} is not a file. Skipping.")
    
    print("\033[1;32mFile organization completed.\033[0m")
    print("\033[1;36mAccess your sorted files at:\033[0m", directory)

    try:
        webbrowser.open(f'file://{directory}')
        print("\033[1;35mOpening the sorted files directory...\033[0m")
    except Exception as e:
        print("\033[1;31mCould not open the folder automatically, please navigate to it manually.\033[0m")

if __name__ == '__main__':
    print("\033c", end="")  # ANSI escape code to clear the screen
    print("\033[1;34mNAZTECH FILE SORTER LITE\033[0m")
    print("\033[1;31;47mWARNING: BACK UP YOUR DATA FIRST\033[0m")  # Bold, red text on white background
    print("\033[1;33m" + "="*80 + "\033[0m")  # Yellow bold delimiters
    print("\033[1;33mThis script will modify the structure of the directory you specify by organizing files into folders.\033[0m")
    print("\033[1;33m" + "="*80 + "\033[0m")  # Yellow bold delimiters
    
    directory = input("\033[1;32mEnter the directory path: \033[0m")
    
    organize_files_by_type(directory)