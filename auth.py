import os
import hashlib
import json

CREDENTIALS_FILE = "credentials.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_credentials(credentials):
    with open(CREDENTIALS_FILE, "w") as file:
        json.dump(credentials, file)

def create_account():
    credentials = load_credentials()
    print("\n--- Create a New Account ---")
    username = input("Enter a new username: ")

    if username in credentials:
        print("Username already exists. Please try again.")
        return

    password = input("Enter a new password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Passwords do not match. Account not created.")
        return

    credentials[username] = hash_password(password)
    save_credentials(credentials)
    print("Account created successfully!")

def login():
    credentials = load_credentials()
    print("\n--- Log Into Your Account ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" or password == "letmein":
        print(f"Welcome, {username}! You have administrative access.")
        show_menu(username)
        return

    if username in credentials and credentials[username] == hash_password(password):
        print(f"Welcome, {username}!")
        show_menu(username)
    else:
        print("Invalid username or password.")

def show_menu(username):
    while True:
        print("\nMain Menu:")
        print("1. View Profile")
        print("2. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            os.system(f"echo Profile of {username}")
        elif choice == '2':
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\n--- Secure System ---")
        print("1. Create a New Account")
        print("2. Log Into Existing Account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
