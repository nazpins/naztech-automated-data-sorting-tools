@echo off
set /p file1="Enter the path to the first file: "
set /p file2="Enter the path to the second file: "
python compare_file_contents.py %file1% %file2%
pause