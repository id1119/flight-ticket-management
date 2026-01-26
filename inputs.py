import repository as repo
import datetime

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            if repo.users[username]["password"] == password:
                return repo.users[username]["position"]
        except Exception:
            print("[ERROR] Invalid credentials! Please try again.")


