# Ask for folder path
Write-Host "Enter the path of the folder with duplicate images:"
$folder_path = Read-Host

# Create Python Virtual Environment
Write-Host "Creating Python Virtual Environment..."
python -m venv venv
& ./venv/Scripts/Activate.ps1

# Install necessary libraries
Write-Host "Installing necessary libraries..."
pip install Pillow imagehash

# Run the Python script
Write-Host "Running duplicate removal script..."
python ./remove_duplicates.py $folder_path

# Deactivate the virtual environment
& ./venv/Scripts/Deactivate.ps1
Write-Host "Script execution completed."
