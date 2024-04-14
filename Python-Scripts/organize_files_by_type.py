import os
import shutil

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
    
    print("File organization completed.")

if __name__ == '__main__':
    # Prompt the user for the directory path
    directory = input("Enter the directory path: ")
    
    # Call the function to organize files by type
    organize_files_by_type(directory)