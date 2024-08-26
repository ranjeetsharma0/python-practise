import os
from cryptography.fernet import Fernet
from hashlib import sha256

# Load or generate key
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        return key

def encrypt_message(message: str, key: bytes) -> str:
    return Fernet(key).encrypt(message.encode()).decode()

def decrypt_message(encrypted_message: str, key: bytes) -> str:
    return Fernet(key).decrypt(encrypted_message.encode()).decode()

def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()

def check_master_password(stored_hash: str, entered_password: str) -> bool:
    return stored_hash == hash_password(entered_password)

# Check if master password exists
if os.path.exists("masterpwd.txt"):
    with open("masterpwd.txt", "r") as f:
        stored_master_pwd_hash = f.read().strip()
else:
    # If not set, user can create one
    master_pwd = input("Create a master password: ")
    stored_master_pwd_hash = hash_password(master_pwd)
    with open("masterpwd.txt", "w") as f:
        f.write(stored_master_pwd_hash)

# input and check master password
master_pwd = input("Enter the master password: ")

if not check_master_password(stored_master_pwd_hash, master_pwd):
    print("Incorrect master password!")
    exit()

# Load the encrypttion key
key = load_key()

def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, encrypted_passw = data.split("|")
                passw = decrypt_message(encrypted_passw, key)
                print("User:" , user , "| Password:" , passw)
    except FileNotFoundError:
        print("No passwords stored yet.")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    encrypted_pwd = encrypt_message(pwd, key)

    with open('password.txt', 'a') as f:
        f.write(name + "|"  + encrypted_pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
