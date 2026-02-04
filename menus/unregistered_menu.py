import projekat.repository as repo
import projekat.inputs as iu
import copy
from projekat.main import *

concrete_flights_copy = {}

def unregistered_menu():
    print("====MENU====")
    print("Status: unregistered")
    print("1) Login")
    print("2) Exit application")
    print("3) View available flights")
    print("4) Search flight by")
    print("5) Search flight by multiple parameters")
    print("6) View 10 cheapest flights between two destinations")
    print("7) View flights at certain date +- flexible days")
    print("8) Register")

def search_flight_by_menu():
    print("===Search flight by===")
    print("1) Departure airport")
    print("2) Arrival airport")
    print("3) Departure date")
    print("4) Arrival date")
    print("5) Departure time")
    print("6) Arrival time")
    print("7) Airline")
    print("x) Go back to main menu")

def search_flight_by_multiple_menu():
    print("===Search flights by multiple parameters===")
    print("1) Departure airport")
    print("2) Arrival airport")
    print("3) Departure date")
    print("4) Arrival date")
    print("5) Departure time")
    print("6) Arrival time")
    print("7) Airline")
    print("s) Search!!!")
    print("x) Go back to main menu")
def unregistered_menu_main():
    repo.load_all()
    while True:
        print(unregistered_menu())
        choice = input("Please choose functionality: ")
        if choice == '1':  # login
            username = iu.login()  # vraca naziv ulogovanog
            return username
        elif choice == '2':
            print("Exiting...")
            repo.save_all()
            return False
        elif choice == '3':
            repo.available_flights()
        elif choice == '4':
            while True:
                search_flight_by_menu()
                choose = input("What do you want to search by?: ")
                if choose == '1':
                    parameter = "departure_airport"
                    value = input("Enter departure airport: ")
                    repo.search_by(parameter, value)
                elif choose == '2':
                    parameter = "arrival_airport"
                    value = input("Enter arrival airport: ")
                    repo.search_by(parameter, value)
                elif choose == '3':
                    parameter = "departure_date"
                    value = input("Enter departure date: ")
                    repo.search_by(parameter, value)
                elif choose == '4':
                    parameter = "arrival_date"
                    value = input("Enter arrival date: ")
                    repo.search_by(parameter, value)
                elif choose == '5':
                    parameter = "departure_time"
                    value = input("Enter departure time: ")
                    repo.search_by(parameter, value)
                elif choose == '6':
                    parameter = "arrival_time"
                    value = input("Enter arrival time: ")
                    repo.search_by(parameter, value)
                elif choose == '7':
                    parameter = "airline"
                    value = input("Enter airline: ")
                    repo.search_by(parameter, value)
                elif choose == 'x':
                    print("Going back..")
                    break
                else:
                    print("[ERROR] Invalid input!")
        elif choice == '5':
            global concrete_flights_copy
            concrete_flights_copy = copy.deepcopy(repo.concrete_flights)
            while True:
                search_flight_by_multiple_menu()
                choose = input("Select one of parameters that you want to search by: ")
                if choose == '1':
                    parameter = "departure_airport"
                    value = input("Enter departure airport: ")
                    repo.search_by_multiple(concrete_flights_copy, parameter, value)
                elif choose == '2':
                    parameter = "arrival_airport"
                    value = input("Enter arrival airport: ")
                    repo.search_by_multiple(concrete_flights_copy, parameter, value)
                elif choose == '3':
                    parameter = "departure_date"
                    value = input("Enter departure date: ")
                    repo.search_by_multiple(concrete_flights_copy, parameter, value)
                elif choose == '4':
                    parameter = "arrival_date"
                    value = input("Enter arrival date: ")
                    repo.search_by_multiple(concrete_flights_copy, parameter, value)
                elif choose == '5':
                    parameter = "departure_time"
                    value = input("Enter departure time: ")
                    repo.search_by_multiple(concrete_flights_copy, parameter, value)
                elif choose == '6':
                    parameter = "arrival_time"
                    value = input("Enter arrival time: ")
                    repo.search_by_multiple(concrete_flights_copy, parameter, value)
                elif choose == '7':
                    parameter = "airline"
                    value = input("Enter airline: ")
                    repo.search_by_multiple(concrete_flights_copy, parameter, value)
                elif choose == 's':
                    repo.print_search_by_multiple(concrete_flights_copy)
                elif choose == 'x':
                    print("Going back..")
                    break
                else:
                    print("[ERROR] Invalid input!")
        elif choice == '6':
            concrete_flights_copy = copy.deepcopy(repo.concrete_flights)
            departure_airport = input("Enter departure airport: ")
            repo.search_by_multiple(concrete_flights_copy, "departure_airport", departure_airport)
            arrival_airport = input("Enter arrival airport: ")
            repo.search_by_multiple(concrete_flights_copy, "arrival_airport", arrival_airport)
            repo.print_ten_cheapest_flights(concrete_flights_copy)
        elif choice == '7':
            while True:
                concrete_flights_copy = copy.deepcopy(repo.concrete_flights)
                departure_airport = input("Enter departure airport: ")
                repo.search_by_multiple(concrete_flights_copy, "departure_airport", departure_airport)
                arrival_airport = input("Enter arrival airport: ")
                repo.search_by_multiple(concrete_flights_copy, "arrival_airport", arrival_airport)
                date = input("Enter date of flight: ")
                days = input("Enter number of flexible days: ")
                try:
                    repo.print_flights_by_search_date(concrete_flights_copy, date, days)
                    break
                except Exception:
                    print("[ERROR] Invalid date!")
        elif choice == '8':
            username = iu.enter_name("username")
            password = iu.enter_name("password")
            name = iu.enter_name("name")
            last_name = iu.enter_name("last name")
            phone_number = iu.enter_name("phone number")
            email = iu.enter_email()
            position = "buyer"
            passport_number = iu.enter_passport_optional()
            citizenship = iu.enter_optional("citizenship")
            gender = iu.enter_optional("gender")
            repo.users[username] = {
                "username" : username,
                "password" : password,
                "name" : name,
                "last_name" : last_name,
                "phone_number": phone_number,
                "email": email,
                "position" : position,
                "passport_number" : passport_number,
                "citizenship" : citizenship,
                "gender" : gender,
            }
        else:
            print("[ERROR] Invalid input! Please try again.")

if __name__ == '__main__':
    unregistered_menu_main()