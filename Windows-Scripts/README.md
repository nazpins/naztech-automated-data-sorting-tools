# Useful Windows Scripts

This folder contains a collection of 20 useful scripts for Windows power users, focusing on machine learning, automation, data sorting, security, and workflow improvements.

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

Please note that some of these scripts may modify your files or system settings. It is recommended to create backups before running them and to use them with caution.
```

block_exe_files_firewall.bat:
```batch
@echo off
setlocal enableextensions
cd /d "%~dp0"

REM Block all .exe files in the current directory and its subdirectories using Windows Firewall
for /R %%f in (*.exe) do (
    netsh advfirewall firewall add rule name="Blocked: %%f" dir=out program="%%f" action=block
)
pause
```

list_installed_apps_with_winget.bat:
```batch
@echo off
setlocal EnableDelayedExpansion

REM Output file
set "outputFile=installed_apps_with_winget.txt"

REM Clear the output file if it exists
if exist "%outputFile%" del "%outputFile%"

REM List all installed apps and their corresponding winget install commands
for /f "tokens=*" %%a in ('powershell "Get-AppxPackage | Select-Object Name"') do (
    set "appName=%%a"
    REM Remove the 'Name' prefix from the output
    set "cleanAppName=!appName:Name=!"

    REM Check if the app name is not empty and not a header
    if not "!cleanAppName!"=="" if not "!cleanAppName!"=="----" (
        REM Output the app name and the winget install command
        echo !cleanAppName! >> "%outputFile%"
        echo winget install !cleanAppName! >> "%outputFile%"
        echo. >> "%outputFile%"
    )
)

echo Done. Check the file '%outputFile%' for the list and commands.
pause
```

list_winget_install_commands.bat:
```batch
@echo off
setlocal EnableDelayedExpansion

REM Output file
set "outputFile=winget_install_commands.txt"

REM Clear the output file if it exists
if exist "%outputFile%" del "%outputFile%"

REM List only the winget install commands for all installed apps
for /f "tokens=*" %%a in ('powershell "Get-AppxPackage | Select-Object Name"') do (
    set "appName=%%a"
    REM Remove the 'Name' prefix from the output
    set "cleanAppName=!appName:Name=!"

    REM Check if the app name is not empty and not a header
    if not "!cleanAppName!"=="" if not "!cleanAppName!"=="----" (
        REM Output only the winget install command
        echo winget install !cleanAppName! >> "%outputFile%"
    )
)

echo Done. Check the file '%outputFile%' for the commands.
pause
```

add_miniconda3_to_path.bat:
```batch
@echo off
REM Add Miniconda3 to the system's PATH environment variable
SETX PATH "%PATH%;C:\ProgramData\miniconda3;C:\ProgramData\miniconda3\Scripts;C:\ProgramData\miniconda3\Library\bin"
pause
```

open_apps_folder.bat:
```batch
@echo off
REM Open the Windows Apps folder in File Explorer
start shell:AppsFolder
```

restart_explorer.bat:
```batch
@echo off
REM Restart the Windows Explorer process
taskkill /f /im explorer.exe
start explorer.exe
```

toggle_hidden_files.bat:
```batch
@echo off
REM Toggle the visibility of hidden files and folders in Windows Explorer
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden | find "0x1" > nul
if %errorlevel% == 0 (
    reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 0 /f
    echo Hidden files and folders are now visible.
) else (
    reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 1 /f
    echo Hidden files and folders are now hidden.
)
pause
```

create_system_restore_point.bat:
```batch
@echo off
REM Create a system restore point using PowerShell
powershell -ExecutionPolicy Bypass -Command "Checkpoint-Computer -Description 'Manual Restore Point' -RestorePointType 'MODIFY_SETTINGS'"
pause
```

update_all_apps.bat:
```batch
@echo off
REM Update all installed applications using the Windows Package Manager (winget)
winget upgrade --all
pause
```

find_large_files.bat:
```batch
@echo off
REM Find all files larger than a specified size (default: 1 GB) in the current directory and its subdirectories
set "size=1000000000"
set "outputFile=large_files.txt"
powershell -ExecutionPolicy Bypass -Command "Get-ChildItem -Recurse -ErrorAction SilentlyContinue | Where-Object {$_.Length -gt %size%} | Select-Object FullName,Length | Out-File -FilePath '%outputFile%'"
echo Done. Check the file '%outputFile%' for the list of large files.
pause
```

clean_temp_files.bat:
```batch
@echo off
REM Clean up the user's temporary files directory by deleting all files and subdirectories within it
del /q /f /s %temp%\*
for /d %%G in ("%temp%\*") do rd /s /q "%%~G"
pause
```

reset_network_adapter.bat:
```batch
@echo off
REM Reset the network adapter settings
ipconfig /release
ipconfig /renew
ipconfig /flushdns
netsh winsock reset
netsh int ip reset
pause
```

enable_god_mode.bat:
```batch
@echo off
REM Create a special folder on the desktop named "GodMode" that provides quick access to various system settings and tools
md "%UserProfile%\Desktop\GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}"
pause
```

list_installed_drivers.bat:
```batch
@echo off
REM Generate a detailed list of all installed drivers on the system and save it to a text file
driverquery /fo list /v > installed_drivers.txt
echo Done. Check the file 'installed_drivers.txt' for the list of installed drivers.
pause
```

monitor_cpu_usage.bat:
```batch
@echo off
REM Continuously monitor the CPU usage and display the current percentage in real-time
:loop
cls
powershell -ExecutionPolicy Bypass -Command "(Get-Counter -Counter '\Processor(_Total)\% Processor Time' -SampleInterval 1 -MaxSamples 1).CounterSamples[0].CookedValue"
timeout /t 1 /nobreak > nul
goto loop
```

find_duplicate_files.bat:
```batch
@echo off
REM Find all duplicate files in the current directory and its subdirectories based on their names and sizes
powershell -ExecutionPolicy Bypass -Command "Get-ChildItem -Recurse -File | Group-Object -Property Name, Length | Where-Object { $_.Count -gt 1 } | Select-Object -ExpandProperty Group | Out-File -FilePath 'duplicate_files.txt'"
echo Done. Check the file 'duplicate_files.txt' for the list of duplicate files.
pause
```

list_installed_fonts.bat:
```batch
@echo off
REM Generate a list of all installed fonts on the system and save it to a text file
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" > installed_fonts.txt
echo Done. Check the file 'installed_fonts.txt' for the list of installed fonts.
pause
```

change_file_extensions.bat:
```batch
@echo off
REM Change the file extension of all files in the current directory from one extension to another (e.g., .txt to .md)
set "oldExtension=.txt"
set "newExtension=.md"
ren *%oldExtension% *%newExtension%
pause
```

convert_images_to_pdf.bat:
```batch
@echo off
REM Convert all JPG images in the current directory into a single PDF file using PowerShell
set "outputFile=combined.pdf"
powershell -ExecutionPolicy Bypass -Command "$images = Get-ChildItem -File -Filter '*.jpg'; $images | ForEach-Object { Add-Type -AssemblyName System.Drawing; $image = [System.Drawing.Image]::FromFile($_.FullName); $pdf = New-Object System.Drawing.Printing.PrintDocument; $pdf.DefaultPageSettings.Landscape = $true; $pdf.PrinterSettings.PrinterName = 'Microsoft Print to PDF'; $pdf.PrinterSettings.PrintToFile = $true; $pdf.PrinterSettings.PrintFileName = '%outputFile%'; $pdf.PrintPage += { param($sender, $e) $e.Graphics.DrawImage($image, 0, 0, $e.PageBounds.Width, $e.PageBounds.Height) }; $pdf.Print() }"
echo Done. Check the file '%outputFile%' for the combined PDF.
pause
```

backup_user_folders.bat:
```batch
@echo off
REM Create a backup of the user's essential folders in a "Backup" directory within the user's Documents folder
set "backupDir=%UserProfile%\Documents\Backup"
robocopy "%UserProfile%\Desktop" "%backupDir%\Desktop" /E /XO /XX
robocopy "%UserProfile%\Documents" "%backupDir%\Documents" /E /XO /XX
robocopy "%UserProfile%\Pictures" "%backupDir%\Pictures" /E /XO /XX
robocopy "%UserProfile%\Videos" "%backupDir%\Videos" /E /XO /XX
robocopy "%UserProfile%\Music" "%backupDir%\Music" /E /XO /XX
pause
```
## Customization

Feel free to modify and customize the scripts to suit your specific needs. You can add additional features, change the input prompts, or integrate the scripts into your existing workflows.

## Contributions

Contributions to the Windows-Scripts collection are welcome! If you have any ideas for new scripts or improvements to existing ones, please feel free to submit a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

Please use these scripts responsibly and ensure that you have the necessary permissions and backups before running them. The authors of these scripts are not responsible for any data loss, security breaches, or other issues that may arise from the use of these scripts.