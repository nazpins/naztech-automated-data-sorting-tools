import os

def create_user(username):
    os.system(f"net user {username} /add")
    print(f"User '{username}' created successfully.")

def modify_user(username, new_password):
    os.system(f"net user {username} {new_password}")
    print(f"User '{username}' modified successfully.")

def delete_user(username):
    os.system(f"net user {username} /delete")
    print(f"User '{username}' deleted successfully.")

if __name__ == '__main__':
    action = input("Enter 'create', 'modify', or 'delete' to manage user accounts: ")
    username = input("Enter the username: ")
    if action == 'create':
        create_user(username)
    elif action == 'modify':
        new_password = input("Enter the new password: ")
        modify_user(username, new_password)
    elif action == 'delete':
        delete_user(username)
    else:
        print("Invalid action. Please enter 'create', 'modify', or 'delete'.")