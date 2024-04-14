@echo off
set /p file_path="Enter the file path to encrypt/decrypt: "
set /p key_path="Enter the path to the key file: "
set /p action="Enter 'encrypt' to encrypt the file or 'decrypt' to decrypt the file: "
python encrypt_decrypt_files.py %file_path% %key_path% %action%
pause