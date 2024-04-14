import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        original = file.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(original)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)
    with open(file_path[:-4], 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

if __name__ == '__main__':
    file_path = input("Enter the file path to encrypt/decrypt: ")
    key_path = input("Enter the path to the key file: ")
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    action = input("Enter 'encrypt' to encrypt the file or 'decrypt' to decrypt the file: ")
    if action == 'encrypt':
        encrypt_file(file_path, key)
        print("File encrypted successfully.")
    elif action == 'decrypt':
        decrypt_file(file_path, key)
        print("File decrypted successfully.")
    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")