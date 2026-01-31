import projekat.repository as repo
import datetime
import projekat.menus.buyer_menu as buyer

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            if repo.users[username]["password"] == password:
                return username
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

def enter_concrete_flight_number(concrete_flights):
    while True:
        print("x) Go back")
        concrete_flight_number = input("Enter concrete flight number: ")
        if concrete_flight_number == 'x':
            return
        if is_concrete_flight_number_valid(concrete_flight_number):
            if int(repo.has_free_seats(concrete_flight_number)) >= 0:
                return concrete_flight_number
            else:
                print("[ERROR] Flight is already fully booked!")
        else:
            pass

def is_concrete_flight_number_valid(concrete_flight_number):
    while True:
        try:
            _ = repo.concrete_flights[concrete_flight_number]
            return True
        except Exception:
            print("[ERROR] Invalid concrete flight number")
            return False

