@echo off
powershell -ExecutionPolicy Bypass -Command "Checkpoint-Computer -Description 'Manual Restore Point' -RestorePointType 'MODIFY_SETTINGS'"
pause