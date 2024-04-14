
import os
import sys
from PIL import Image
import imagehash

def find_duplicates(folder_path):
    hashes = {}
    duplicates = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as img:
                    hash = imagehash.average_hash(img)
                    if hash in hashes:
                        duplicates.append((filename, hashes[hash]))
                    else:
                        hashes[hash] = filename
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    return duplicates

folder_path = sys.argv[1]
try:
    duplicate_images = find_duplicates(folder_path)
    with open('duplicate_log.txt', 'w') as log:
        log.write(f"Total files checked: {len(os.listdir(folder_path))}\n")
        log.write(f"Total duplicates found: {len(duplicate_images)}\n")
        for dup in duplicate_images:
            log.write(f"Duplicate found: {dup[0]} and {dup[1]}\n")
            try:
                os.remove(os.path.join(folder_path, dup[0]))
                log.write(f"Removed: {dup[0]}\n")
            except Exception as e:
                log.write(f"Failed to remove {dup[0]}: {e}\n")
except Exception as e:
    print(f"Failed to process directory {folder_path}: {e}")

print(f'Results have been logged in duplicate_log.txt in the {folder_path} directory.')
