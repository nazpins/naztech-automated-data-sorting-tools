@echo off
setlocal EnableDelayedExpansion

REM Output file
set "outputFile=installed_apps_with_winget.txt"

REM Clear the output file if it exists
if exist "%outputFile%" del "%outputFile%"

REM List all installed apps
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