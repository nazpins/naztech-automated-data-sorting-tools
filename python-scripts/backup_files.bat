@echo off
set /p src_dir="Enter the source directory path: "
set /p dst_dir="Enter the destination directory path: "
set /p encrypt_files="Do you want to encrypt the backup files? (y/n): "
python backup_files.py %src_dir% %dst_dir% %encrypt_files%
pause