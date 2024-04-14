@echo off
set /p directory="Enter the directory path: "
set /p old_pattern="Enter the old pattern to replace: "
set /p new_pattern="Enter the new pattern: "
python rename_files_in_bulk.py %directory% %old_pattern% %new_pattern%
pause