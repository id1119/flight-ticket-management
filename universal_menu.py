import repository as repo
import inputs as iu
import copy
from main import *


def universal_menu():
    repo.load_all()
    while True:
        print(universal_menu())
        choice = input("Please choose functionality: ")
        if choice == '1':  # login
            iu.login()  # vraca poziciju ulogovanog
        elif choice == '2':
            print("Exiting...")
            repo.save_all()
            break
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