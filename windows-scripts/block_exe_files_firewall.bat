@echo off
setlocal enableextensions
cd /d "%~dp0"

for /R %%f in (*.exe) do (
    netsh advfirewall firewall add rule name="Blocked: %%f" dir=out program="%%f" action=block
)
pause