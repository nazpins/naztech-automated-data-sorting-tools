# Windows Scripts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/en-us/windows)

A curated collection of 20 useful scripts for Windows power users, focusing on machine learning, automation, data sorting, security, and workflow improvements. These scripts are designed to streamline tasks, enhance productivity, and provide convenient utilities for various system management and file manipulation operations.

## Table of Contents

- [Scripts](#scripts)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Scripts

1. `block_exe_files_firewall.bat`: Blocks all .exe files in the current directory and its subdirectories using Windows Firewall.

2. `list_installed_apps_with_winget.bat`: Lists all installed applications and their corresponding winget install commands, saving the output to a text file.

3. `list_winget_install_commands.bat`: Lists only the winget install commands for all installed applications, saving the output to a text file.

4. `add_miniconda3_to_path.bat`: Adds Miniconda3 to the system's PATH environment variable.

5. `open_apps_folder.bat`: Opens the Windows Apps folder in File Explorer.

6. `restart_explorer.bat`: Restarts the Windows Explorer process.

7. `toggle_hidden_files.bat`: Toggles the visibility of hidden files and folders in Windows Explorer.

8. `create_system_restore_point.bat`: Creates a system restore point using PowerShell.

9. `update_all_apps.bat`: Updates all installed applications using the Windows Package Manager (winget).

10. `find_large_files.bat`: Finds all files larger than a specified size (default: 1 GB) in the current directory and its subdirectories, and outputs the list of files with their full paths and sizes to a text file.

11. `clean_temp_files.bat`: Cleans up the user's temporary files directory by deleting all files and subdirectories within it.

12. `reset_network_adapter.bat`: Resets the network adapter settings by releasing and renewing the IP address, flushing the DNS cache, and resetting the Winsock catalog and IP settings.

13. `enable_god_mode.bat`: Creates a special folder on the desktop named "GodMode" that provides quick access to various system settings and tools.

14. `list_installed_drivers.bat`: Generates a detailed list of all installed drivers on the system and saves it to a text file.

15. `monitor_cpu_usage.bat`: Continuously monitors the CPU usage and displays the current percentage in real-time, refreshing every second.

16. `find_duplicate_files.bat`: Finds all duplicate files in the current directory and its subdirectories based on their names and sizes, and outputs the list of duplicate files to a text file.

17. `list_installed_fonts.bat`: Generates a list of all installed fonts on the system and saves it to a text file.

18. `change_file_extensions.bat`: Changes the file extension of all files in the current directory from one extension to another (e.g., .txt to .md).

19. `convert_images_to_pdf.bat`: Converts all JPG images in the current directory into a single PDF file using PowerShell.

20. `backup_user_folders.bat`: Creates a backup of the user's essential folders (Desktop, Documents, Pictures, Videos, and Music) in a "Backup" directory within the user's Documents folder.

## Getting Started

### Prerequisites

- Windows operating system (Windows 7 or later)
- PowerShell (included in Windows by default)
- Windows Package Manager (winget) for certain scripts (optional)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nazpins/naztech-software/main/windows-scripts.git
   ```

2. You're ready to use the scripts! Double-click the `.bat` file and follow the prompts to provide the necessary inputs.

## Usage

To run a script, simply double-click on the corresponding `.bat` file or execute it from the command prompt. Follow the prompts or instructions provided by each script, if any.

Please note that some scripts may modify your files or system settings. It is recommended to create backups before running them and to use them with caution.

## Customization

Feel free to modify and customize the scripts to suit your specific needs. You can add additional features, change the input prompts, or integrate the scripts into your existing workflows.

## Contributing

Contributions to the Windows-Scripts collection are welcome! If you have any ideas for new scripts or improvements to existing ones, please submit a pull request or open an issue on the [GitHub repository](https://github.com/nazpins/naztech-software/main/windows-scripts).

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

Please use these scripts responsibly and ensure that you have the necessary permissions and backups before running them. The author of these scripts is not responsible for any data loss, security breaches, or other issues that may arise from the use of these scripts.

---

**Note**: Some scripts may require administrative privileges to run successfully.