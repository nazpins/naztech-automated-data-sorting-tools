
# Duplicate Photo Hash Deleter

## Description
Duplicate Photo Hash Deleter is a utility to identify and remove duplicate images in a specified directory. It uses hashing algorithms provided by the `imagehash` library to detect duplicates effectively.

## Installation

### Prerequisites
- Python 3.x
- PIL (Pillow)
- imagehash

### Setup
Clone this repository to your local machine:
```bash
git clone https://github.com/your-github-username/duplicate-photo-hash-deleter.git
cd duplicate-photo-hash-deleter
```

Install the necessary Python libraries:
```bash
pip install Pillow imagehash
```

## Usage

To run the script, navigate to the script's directory and execute:
```bash
# For Windows Batch
remove_duplicates.bat

# For PowerShell
./remove_duplicates.ps1

# Directly with Python
python remove_duplicates.py <path-to-your-images-folder>
```

### Batch and PowerShell Scripts
Enter the path to the folder containing the images when prompted. The script will handle the rest, logging the duplicates found and removed in `duplicate_log.txt`.

### Python Script
Provide the path as a command-line argument. Results will be logged similarly.

## Contributing
Feel free to fork this project and submit pull requests or open an issue if you find any bugs.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
