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

def enter_name(name_type):
    while True:
        name = input(f"Enter {name_type}: ")
        if name == "":
            print(f"[ERROR] Invalid {name_type}, please try again.")
        else:
            return name

def enter_email():
    while True:
        email = input("Enter email: ")
        try:
            user, domen = email.split("@")
            name, com = domen.split(".")
            return email
        except:
            print(f"[ERROR] Invalid email, please try again.")

def enter_passport():
    while True:
        print("To skip click x")
        passport_number = input("Enter passport number(9 numbers):")
        if passport_number == 'x':
            return None
        elif passport_number == '':
            print(f"[ERROR] Invalid passport number, please try again.")
        elif len(passport_number) != 9:
            print(f"[ERROR] Invalid passport number, please try again.")
        else:
            return passport_number

def enter_optional(type):
    while True:
        print("To skip click x")
        optional = input(f"Enter {type}")
        if optional == "":
            print(f"[ERROR] Invalid passport number, please try again.")
        elif optional == 'x':
            return None
        else:
            return optional
