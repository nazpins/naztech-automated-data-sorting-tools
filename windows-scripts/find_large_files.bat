@echo off
set "size=1000000000"
set "outputFile=large_files.txt"
powershell -ExecutionPolicy Bypass -Command "Get-ChildItem -Recurse -ErrorAction SilentlyContinue | Where-Object {$_.Length -gt %size%} | Select-Object FullName,Length | Out-File -FilePath '%outputFile%'"
echo Done. Check the file '%outputFile%' for the list of large files.
pause