import os
import hashlib
import shutil
import logging
import re
import time

def setup_logging():
    logging.basicConfig(filename='organizer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def extract_metadata_from_filename(filename):
    pattern = r'(?P<author>[^_]+) - (?P<title>[^_]+)'
    match = re.match(pattern, filename)
    if match:
        return match.group('author'), match.group('title')
    else:
        return "Unknown", "Unknown"

def move_duplicates_to_bin(directory, bin_dir):
    hashes = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            filehash = file_hash(filepath)
            if filehash in hashes and not os.path.samefile(filepath, hashes[filehash]):
                if not os.path.exists(bin_dir):
                    os.makedirs(bin_dir)
                new_filename = f"{filename}_{int(time.time())}"
                shutil.move(filepath, os.path.join(bin_dir, new_filename))
                logging.info(f"Duplicate moved: {new_filename}")
            else:
                hashes[filehash] = filepath

def rename_file_based_on_metadata(filepath):
    dirname, filename = os.path.split(filepath)
    author, title = extract_metadata_from_filename(filename)
    file_ext = os.path.splitext(filepath)[1]
    new_filename = f"{author} - {title}{file_ext}" if not filename.endswith(file_ext) else filename
    new_filepath = os.path.join(dirname, new_filename)
    if new_filepath != filepath:
        os.rename(filepath, new_filepath)
        logging.info(f"Renamed '{filepath}' to '{new_filepath}'")
    return new_filepath

def organize_books(directory, bin_dir):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            updated_filepath = rename_file_based_on_metadata(filepath)
            author = os.path.basename(updated_filepath).split(' - ')[0]
            author_dir = os.path.join(directory, author)
            if not os.path.exists(author_dir):
                os.makedirs(author_dir)
            dest_path = os.path.join(author_dir, os.path.basename(updated_filepath))
            if not os.path.exists(dest_path):
                shutil.move(updated_filepath, dest_path)
                logging.info(f"Moved '{os.path.basename(updated_filepath)}' to '{dest_path}'")
            else:
                if not os.path.exists(bin_dir):
                    os.makedirs(bin_dir)
                shutil.move(updated_filepath, os.path.join(bin_dir, os.path.basename(updated_filepath)))
                logging.warning(f"Duplicate detected and moved to '{bin_dir}': {os.path.basename(updated_filepath)}")
        if not os.listdir(root) and root != directory:
            os.rmdir(root)
            logging.info(f"Removed empty folder: {root}")

def main():
    print("DISCLAIMER:")
    print("This script modifies filenames and metadata of your e-books.")
    print("It is strongly recommended to backup your books folder before proceeding.")
    ebook_directory = input("Enter the path to the folder containing your e-books: ").strip()
    bin_directory = os.path.join(ebook_directory, "DuplicateBin")

    setup_logging()
    move_duplicates_to_bin(ebook_directory, bin_directory)
    organize_books(ebook_directory, bin_directory)
    logging.info("Ebook organizing complete.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        input("Press Enter to exit...")

