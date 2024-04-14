import os
import webbrowser
import requests
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='doc_sorter.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def sanitize_filename(name):
    """Sanitize the file name by replacing invalid characters."""
    invalid_chars = '<>:"/\\|?*'
    for ch in invalid_chars:
        name = name.replace(ch, '_')
    return name

def fetch_metadata(query, api_key):
    """Fetch metadata from the Google Books API."""
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {'q': query, 'key': api_key}
    response = requests.get(base_url, params=params)
    logging.info(f'Searching for: {query}')
    if response.status_code != 200:
        logging.error(f'Error fetching metadata: {response.status_code}')
        logging.error(f'Response content: {response.text}')
        return query, 'Unknown Author'
    data = response.json()
    logging.info(f'Response Data: {data}')
    if data['totalItems'] > 0:
        book = data['items'][0]['volumeInfo']
        title = book.get('title', 'Unknown Title')
        authors = book.get('authors', ['Unknown Author'])
        logging.info(f'Found Title: {title}, Author: {authors[0]}')
        return title, authors[0]
    logging.warning(f'No results found for query: {query}')
    return query, 'Unknown Author'

def rename_and_sort_files(directory, sorted_path, include_datetime, api_key):
    """Rename and move files based on fetched metadata."""
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            if 'SortedFiles' not in root:
                original_name, extension = os.path.splitext(file)
                title, author = fetch_metadata(original_name, api_key)
                safe_title = sanitize_filename(title)
                safe_author = sanitize_filename(author)
                new_name = f"{safe_author} - {safe_title}{extension}"
                new_file_path = os.path.join(root, new_name)
                author_dir = os.path.join(sorted_path, safe_author)
                if not os.path.exists(author_dir):
                    os.makedirs(author_dir)
                final_path = os.path.join(author_dir, new_name)
                try:
                    os.rename(file_path, final_path)
                except OSError as e:
                    logging.error(f'Failed to rename or move file {file_path} to {final_path}: {e}')

def main():
    """Main function to execute the script functionalities."""
    print("\033c", end="")  # Clear screen
    print("\033[1;34mNAZTECH DOC SORTER STARTED...\033[0m")
    print("\033[1;31;47mWARNING: BACK UP YOUR DATA FIRST\033[0m")
    print("\033[1;33m" + "="*80 + "\033[0m")
    print("\033[1;33mThis script will modify the structure of the directory you specify by organizing files into folders.\033[0m")
    print("\033[1;33m" + "="*80 + "\033[0m")

    api_key = input("\033[1;32mPlease enter your Google Books API key: \033[0m").strip()
    if not api_key:
        print("\033[1;31mAPI Key is required to fetch metadata from Google Books API.\033[0m")
        return  # Exit the script if API key is not provided
    include_datetime = input("\033[1;32mDo you want to include datetime in file names? (Y/N): \033[0m").strip().upper() == 'Y'
    directory_to_sort = input("\033[1;32mPlease enter the full path to the directory you wish to sort: \033[0m").strip()
    sorted_files_path = os.path.join(directory_to_sort, 'SortedFiles')

    rename_and_sort_files(directory_to_sort, sorted_files_path, include_datetime, api_key)

    print("\033[1;36mFiles have been organized. Access your sorted files at: " + sorted_files_path + "\033[0m")
    try:
        webbrowser.open(f'file://{sorted_files_path}')
        print("\033[1;35mOpening the sorted files directory...\033[0m")
    except Exception as e:
        print(f"\033[1;31mCould not open the folder automatically, please navigate to it manually. Error: {e}\033[0m")

if __name__ == "__main__":
    main()
