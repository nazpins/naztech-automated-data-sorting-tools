import os

def rename_files(directory, old_pattern, new_pattern):
    for filename in os.listdir(directory):
        if old_pattern in filename:
            new_filename = filename.replace(old_pattern, new_pattern)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
    print("Files renamed successfully.")

if __name__ == '__main__':
    directory = input("Enter the directory path: ")
    old_pattern = input("Enter the old pattern to replace: ")
    new_pattern = input("Enter the new pattern: ")
    rename_files(directory, old_pattern, new_pattern)