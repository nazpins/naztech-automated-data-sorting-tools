import os
import shutil
from cryptography.fernet import Fernet

def backup_files(src_dir, dst_dir, encrypt=False):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    if encrypt:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        with open(os.path.join(dst_dir, 'key.key'), 'wb') as key_file:
            key_file.write(key)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)

        if os.path.isfile(src_path):
            if encrypt:
                with open(src_path, 'rb') as file:
                    original = file.read()
                encrypted = fernet.encrypt(original)
                with open(dst_path + '.enc', 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
            else:
                shutil.copy2(src_path, dst_path)
        elif os.path.isdir(src_path):
            backup_files(src_path, dst_path, encrypt)

if __name__ == '__main__':
    src_dir = input("Enter the source directory path: ")
    dst_dir = input("Enter the destination directory path: ")
    encrypt_files = input("Do you want to encrypt the backup files? (y/n): ").lower() == 'y'
    backup_files(src_dir, dst_dir, encrypt_files)
    print("Backup completed successfully.")