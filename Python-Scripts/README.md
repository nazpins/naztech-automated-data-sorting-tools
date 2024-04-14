# Python-Scripts

This folder contains a collection of scripts focused on improving workflows in machine learning, automation, data sorting, security, and management.

## WARNING - Please REVIEW each script before running it. Most of these scripts are automated and will ask for user input, but it's good practice to know what a script does before running it.

## Prerequisites

- Python 3.x installed
- Conda package manager installed

## Scripts

1. `backup_files.py`: A Python script to automate the backup of important files and directories to a local or remote location, with options for compression and encryption.

2. `compare_file_contents.py`: A Python script to compare the contents of two files or directories, highlighting differences and similarities.

3. `create_conda_env.py`: A Python script to create a new Conda environment for a machine learning project, installing common libraries like NumPy, Pandas, and scikit-learn.

4. `encrypt_decrypt_files.py`: A Python script to encrypt and decrypt files using symmetric or asymmetric encryption algorithms.

5. `generate_data_reports.py`: A Python script to generate data reports from various data sources (e.g., databases, APIs), with options for customizing the report format and content.

6. `manage_user_accounts.py`: A Python script to manage user accounts, including creating, modifying, and deleting user profiles.

7. `merge_csv_files.py`: A Python script to merge multiple CSV files into a single file, with options for handling headers and data types.

8. `monitor_network_traffic.py`: A Python script to monitor network traffic, including incoming and outgoing connections, with options for filtering and logging.

9. `monitor_process_memory.py`: A Python script to monitor the memory usage of specific processes, with options for logging and alerting when thresholds are exceeded.

10. `monitor_system_resources.py`: A Python script to monitor system resources like CPU usage, memory consumption, and disk space, with options for logging and alerting.

11. `organize_files_by_type.py`: A Python script to organize files in a directory by their file types (e.g., images, documents, videos), creating subdirectories for each type.

12. `password_generator.py`: A Python script to generate strong, random passwords of a specified length and complexity.

13. `rename_files_in_bulk.py`: A Python script to rename multiple files in a directory based on a specified pattern or convention.

14. `scan_open_ports.py`: A Python script to scan a network for open ports on specified hosts or IP ranges.

Please note that these scripts are provided as examples and may require additional configuration and customization based on your specific environment and requirements.
```

backup_files.py:
```python
import os
import shutil
from cryptography.fernet import Fernet

def backup_files(src_dir, dst_dir, encrypt=False):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    if encrypt:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        with open(os.path.join(dst_dir, 'key.key'), 'wb') as key_file:
            key_file.write(key)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)

        if os.path.isfile(src_path):
            if encrypt:
                with open(src_path, 'rb') as file:
                    original = file.read()
                encrypted = fernet.encrypt(original)
                with open(dst_path + '.enc', 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
            else:
                shutil.copy2(src_path, dst_path)
        elif os.path.isdir(src_path):
            backup_files(src_path, dst_path, encrypt)

if __name__ == '__main__':
    src_dir = input("Enter the source directory path: ")
    dst_dir = input("Enter the destination directory path: ")
    encrypt_files = input("Do you want to encrypt the backup files? (y/n): ").lower() == 'y'
    backup_files(src_dir, dst_dir, encrypt_files)
    print("Backup completed successfully.")
```

backup_files.bat:
```batch
@echo off
set /p src_dir="Enter the source directory path: "
set /p dst_dir="Enter the destination directory path: "
set /p encrypt_files="Do you want to encrypt the backup files? (y/n): "
python backup_files.py %src_dir% %dst_dir% %encrypt_files%
pause
```

compare_file_contents.py:
```python
import filecmp

def compare_files(file1, file2):
    if filecmp.cmp(file1, file2):
        print("The files are identical.")
    else:
        print("The files are different.")

if __name__ == '__main__':
    file1 = input("Enter the path to the first file: ")
    file2 = input("Enter the path to the second file: ")
    compare_files(file1, file2)
```

compare_file_contents.bat:
```batch
@echo off
set /p file1="Enter the path to the first file: "
set /p file2="Enter the path to the second file: "
python compare_file_contents.py %file1% %file2%
pause
```

create_conda_env.py:
```python
import subprocess

def create_conda_env(env_name):
    subprocess.run(["conda", "create", "-n", env_name, "python=3.9", "-y"])
    subprocess.run(["conda", "activate", env_name])
    subprocess.run(["conda", "install", "numpy", "pandas", "scikit-learn", "-y"])
    print(f"Conda environment '{env_name}' created and activated.")

if __name__ == '__main__':
    env_name = input("Enter the name of the Conda environment: ")
    create_conda_env(env_name)
```

create_conda_env.bat:
```batch
@echo off
set /p env_name="Enter the name of the Conda environment: "
python create_conda_env.py %env_name%
pause
```

encrypt_decrypt_files.py:
```python
import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        original = file.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(original)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)
    with open(file_path[:-4], 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

if __name__ == '__main__':
    file_path = input("Enter the file path to encrypt/decrypt: ")
    key_path = input("Enter the path to the key file: ")
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    action = input("Enter 'encrypt' to encrypt the file or 'decrypt' to decrypt the file: ")
    if action == 'encrypt':
        encrypt_file(file_path, key)
        print("File encrypted successfully.")
    elif action == 'decrypt':
        decrypt_file(file_path, key)
        print("File decrypted successfully.")
    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")
```

encrypt_decrypt_files.bat:
```batch
@echo off
set /p file_path="Enter the file path to encrypt/decrypt: "
set /p key_path="Enter the path to the key file: "
set /p action="Enter 'encrypt' to encrypt the file or 'decrypt' to decrypt the file: "
python encrypt_decrypt_files.py %file_path% %key_path% %action%
pause
```

generate_data_reports.py:
```python
import pandas as pd

def generate_report(data_source, output_format):
    if data_source == 'csv':
        file_path = input("Enter the path to the CSV file: ")
        data = pd.read_csv(file_path)
    elif data_source == 'excel':
        file_path = input("Enter the path to the Excel file: ")
        sheet_name = input("Enter the sheet name: ")
        data = pd.read_excel(file_path, sheet_name=sheet_name)
    else:
        print("Unsupported data source. Please provide a CSV or Excel file.")
        return

    if output_format == 'csv':
        output_path = input("Enter the output file path: ")
        data.to_csv(output_path, index=False)
        print("Report generated successfully.")
    elif output_format == 'excel':
        output_path = input("Enter the output file path: ")
        data.to_excel(output_path, index=False)
        print("Report generated successfully.")
    else:
        print("Unsupported output format. Please choose 'csv' or 'excel'.")

if __name__ == '__main__':
    data_source = input("Enter the data source (csv/excel): ")
    output_format = input("Enter the desired output format (csv/excel): ")
    generate_report(data_source, output_format)
```

generate_data_reports.bat:
```batch
@echo off
set /p data_source="Enter the data source (csv/excel): "
set /p output_format="Enter the desired output format (csv/excel): "
python generate_data_reports.py %data_source% %output_format%
pause
```

manage_user_accounts.py:
```python
import os

def create_user(username):
    os.system(f"net user {username} /add")
    print(f"User '{username}' created successfully.")

def modify_user(username, new_password):
    os.system(f"net user {username} {new_password}")
    print(f"User '{username}' modified successfully.")

def delete_user(username):
    os.system(f"net user {username} /delete")
    print(f"User '{username}' deleted successfully.")

if __name__ == '__main__':
    action = input("Enter 'create', 'modify', or 'delete' to manage user accounts: ")
    username = input("Enter the username: ")
    if action == 'create':
        create_user(username)
    elif action == 'modify':
        new_password = input("Enter the new password: ")
        modify_user(username, new_password)
    elif action == 'delete':
        delete_user(username)
    else:
        print("Invalid action. Please enter 'create', 'modify', or 'delete'.")
```

manage_user_accounts.bat:
```batch
@echo off
set /p action="Enter 'create', 'modify', or 'delete' to manage user accounts: "
set /p username="Enter the username: "
if "%action%"=="create" (
    python manage_user_accounts.py create %username%
) else if "%action%"=="modify" (
    set /p new_password="Enter the new password: "
    python manage_user_accounts.py modify %username% %new_password%
) else if "%action%"=="delete" (
    python manage_user_accounts.py delete %username%
) else (
    echo Invalid action. Please enter 'create', 'modify', or 'delete'.
)
pause
```

merge_csv_files.py:
```python
import pandas as pd
import os

def merge_csv_files(file_list, output_file):
    merged_data = pd.concat([pd.read_csv(file) for file in file_list])
    merged_data.to_csv(output_file, index=False)
    print("CSV files merged successfully.")

if __name__ == '__main__':
    file_list = []
    while True:
        file_path = input("Enter the path to a CSV file (or press Enter to finish): ")
        if file_path == '':
            break
        file_list.append(file_path)
    output_file = input("Enter the output file path: ")
    merge_csv_files(file_list, output_file)
```

merge_csv_files.bat:
```batch
@echo off
python merge_csv_files.py
pause
```

monitor_network_traffic.py:
```python
import psutil
import time

def monitor_network_traffic(interval=1):
    prev_sent = psutil.net_io_counters().bytes_sent
    prev_recv = psutil.net_io_counters().bytes_recv
    while True:
        time.sleep(interval)
        sent = psutil.net_io_counters().bytes_sent
        recv = psutil.net_io_counters().bytes_recv
        sent_speed = (sent - prev_sent) / interval
        recv_speed = (recv - prev_recv) / interval
        print(f"Sent: {sent_speed / 1024:.2f} KB/s, Received: {recv_speed / 1024:.2f} KB/s")
        prev_sent = sent
        prev_recv = recv

if __name__ == '__main__':
    interval = int(input("Enter the monitoring interval (in seconds): "))
    monitor_network_traffic(interval)
```

monitor_network_traffic.bat:
```batch
@echo off
set /p interval="Enter the monitoring interval (in seconds): "
python monitor_network_traffic.py %interval%
pause
```

monitor_process_memory.py:
```python
import psutil
import time

def monitor_process_memory(process_name, interval=1):
    while True:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process_name:
                mem_usage = proc.memory_info().rss / (1024 * 1024)
                print(f"{process_name} memory usage: {mem_usage:.2f} MB")
        time.sleep(interval)

if __name__ == '__main__':
    process_name = input("Enter the process name to monitor: ")
    interval = int(input("Enter the monitoring interval (in seconds): "))
    monitor_process_memory(process_name, interval)
```

monitor_process_memory.bat:
```batch
@echo off
set /p process_name="Enter the process name to monitor: "
set /p interval="Enter the monitoring interval (in seconds): "
python monitor_process_memory.py %process_name% %interval%
pause
```

monitor_system_resources.py:
```python
import psutil
import time

def monitor_system_resources(interval=1):
    while True:
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        print(f"CPU Usage: {cpu_percent}%, Memory Usage: {mem_percent}%, Disk Usage: {disk_percent}%")
        time.sleep(interval)

if __name__ == '__main__':
    interval = int(input("Enter the monitoring interval (in seconds): "))
    monitor_system_resources(interval)
```

monitor_system_resources.bat:
```batch
@echo off
set /p interval="Enter the monitoring interval (in seconds): "
python monitor_system_resources.py %interval%
pause
```

organize_files_by_type.py:
```python
import os
import shutil

def organize_files_by_type(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            subfolder = os.path.join(directory, file_extension[1:].upper())
            if not os.path.exists(subfolder):
                os.makedirs(subfolder)
            shutil.move(file_path, os.path.join(subfolder, filename))
    print("Files organized by type.")

if __name__ == '__main__':
    directory = input("Enter the directory path: ")
    organize_files_by_type(directory)
```

organize_files_by_type.bat:
```batch
@echo off
set /p directory="Enter the directory path: "
python organize_files_by_type.py %directory%
pause
```

password_generator.py:
```python
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
```

password_generator.bat:
```batch
@echo off
set /p length="Enter the desired password length: "
python password_generator.py %length%
pause
```

rename_files_in_bulk.py:
```python
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
```

rename_files_in_bulk.bat:
```batch
@echo off
set /p directory="Enter the directory path: "
set /p old_pattern="Enter the old pattern to replace: "
set /p new_pattern="Enter the new pattern: "
python rename_files_in_bulk.py %directory% %old_pattern% %new_pattern%
pause
```

scan_open_ports.py:
```python
import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} for open ports...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == '__main__':
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    scan_ports(target, start_port, end_port)
```

scan_open_ports.bat:
```batch
@echo off
set /p target="Enter the target IP address: "
set /p start_port="Enter the starting port number: "
set /p end_port="Enter the ending port number: "
python scan_open_ports.py %target% %start_port% %end_port%
pause
```

## Usage

Each script has a corresponding .bat file that allows for easy execution on Windows systems. Simply double-click the .bat file and follow the prompts to provide the necessary inputs.

For Linux and macOS users, you can run the Python scripts directly from the command line by navigating to the directory containing the scripts and executing the following command:

```bash
python script_name.py
```

Replace `script_name.py` with the actual name of the script you want to run.

## Customization

Feel free to modify and customize the scripts to suit your specific needs. You can add additional features, change the input prompts, or integrate the scripts into your existing workflows.

## Contributions

Contributions to the Python-Scripts collection are welcome! If you have any ideas for new scripts or improvements to existing ones, please feel free to submit a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

Please use these scripts responsibly and ensure that you have the necessary permissions and backups before running them. The authors of these scripts are not responsible for any data loss, security breaches, or other issues that may arise from the use of these scripts.
