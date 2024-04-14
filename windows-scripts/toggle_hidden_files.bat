@echo off
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden | find "0x1" > nul
if %errorlevel% == 0 (
    reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 0 /f
    echo Hidden files and folders are now visible.
) else (
    reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 1 /f
    echo Hidden files and folders are now hidden.
)
pause