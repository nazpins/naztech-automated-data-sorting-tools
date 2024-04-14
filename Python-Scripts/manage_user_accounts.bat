@echo off
set /p action="Enter 'create', 'modify', or 'delete' to manage user accounts: "
set /p username="Enter the username: "
if "%action%"=="create" (
    python manage_user_accounts.py create %username%
) else if "%action%"=="modify" (
    set /p new_password="Enter the new password: "
    python manage_user_accounts.py modify %username% %new_password%
) else if "%action%"=="delete" (
    python manage_user_accounts.py delete %username%
) else (
    echo Invalid action. Please enter 'create', 'modify', or 'delete'.
)
pause