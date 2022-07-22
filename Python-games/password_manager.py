# Importing Library for encrypting:
from cryptography.fernet import Fernet

# Creating a key file to encrypt the password file
# One-time process***
# def create_key():
#     key = Fernet.generate_key()
#     with open('Key.key', 'wb') as key_file:
#         key_file.write(key)

# create_key()

def load_key():
    file = open('Python-games/Key.key', 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter the Master Password: ")
mas_key = load_key() + master_pwd.encode()
fer = Fernet(mas_key)

# Functional programming Approach:
def view():
    # Reading the txt file in read mode:
    with open('Python-games/passwords.txt', 'r') as pwd_file:
        for line in pwd_file.readlines():
            view_uname, view_pwd = line.rstrip('\n').split(': ')
            print(f"Username: {view_uname};     Password: {fer.decrypt(view_pwd.encode()).decode()}")

def add():
    username = input("Username: ")
    password = input("Password: ")

    # Writing to the file in Append mode:
    with open('Python-games/passwords.txt', 'a') as pwd_file:
        pwd_file.write(f"{username}: {fer.encrypt(password.encode()).decode()}\n")

while True:
    mode = input("\nDo you want to add a new password or view the exisiting password?\n (Choose: [View/Add]  [Q/q] to quit) \n")
    if (str(mode).lower() == 'q'):
        break
    elif (str(mode).lower() == 'view'):
        view()

    elif (str(mode).lower() == 'add'):
        add()

    else:
        print("Invalid Mode.")
        continue