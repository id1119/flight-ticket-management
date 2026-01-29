import repository as repo
import inputs as iu
import copy

flights_copy = {}
def menu():
    print("====MENU====")
    print("1) Login")
    print("2) Exit application")
    print("3) View available flights")
    print("4) Search flight by")
    print("5) Search flight by multiple parameters")
    print("6) View 10 cheapest flights between two destinations")

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

def main():
    repo.load_all()
    while True:
        print(menu())
        choice = input("Please choose functionality: ")
        if choice == '1':       #login
            iu.login()          #vraca poziciju ulogovanog
        elif choice == '2':
            print("Exiting...")
            repo.save_all()
            break
        elif choice == '3':
            repo.available_flights()
        elif choice =='4':
            while True:
                # choose=''
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
        elif choice =='5':
            global flights_copy
            flights_copy = copy.deepcopy(repo.flights)
            while True:
                search_flight_by_multiple_menu()
                choose = input("Select one of parameters that you want to search by: ")
                if choose == '1':
                    parameter = "departure_airport"
                    value = input("Enter departure airport: ")
                    repo.search_by_multiple(flights_copy, parameter, value)
                elif choose == '2':
                    parameter = "arrival_airport"
                    value = input("Enter arrival airport: ")
                    repo.search_by_multiple(flights_copy, parameter, value)
                elif choose == '3':
                    parameter = "departure_date"
                    value = input("Enter departure date: ")
                    repo.search_by_multiple(flights_copy, parameter, value)
                elif choose == '4':
                    parameter = "arrival_date"
                    value = input("Enter arrival date: ")
                    repo.search_by_multiple(flights_copy, parameter, value)
                elif choose == '5':
                    parameter = "departure_time"
                    value = input("Enter departure time: ")
                    repo.search_by_multiple(flights_copy, parameter, value)
                elif choose == '6':
                    parameter = "arrival_time"
                    value = input("Enter arrival time: ")
                    repo.search_by_multiple(flights_copy, parameter, value)
                elif choose == '7':
                    parameter = "airline"
                    value = input("Enter airline: ")
                    repo.search_by_multiple(flights_copy, parameter, value)
                elif choose == 's':
                    repo.print_search_by_multiple(flights_copy)
                elif choose == 'x':
                    print("Going back..")
                    break
                else:
                    print("[ERROR] Invalid input!")
        elif choice == '6':
            flights_copy = copy.deepcopy(repo.flights)
            departure_airport = input("Enter departure airport: ")
            repo.search_by_multiple(flights_copy,"departure_airport", departure_airport )
            arrival_airport = input("Enter arrival airport: ")
            repo.search_by_multiple(flights_copy,"arrival_airport", arrival_airport )
            repo.print_ten_cheapest_flights(flights_copy)
        elif choice == '7':
            flights_copy = copy.deepcopy(repo.flights)
            departure_airport = input("Enter departure airport: ")
            repo.search_by_multiple(flights_copy,"departure_airport", departure_airport )
            arrival_airport = input("Enter arrival airport: ")
            repo.search_by_multiple(flights_copy,"arrival_airport", arrival_airport )
            date = input("Enter date of flight: ")
            days = input("Enter number of flexible days: ")


if __name__=="__main__":
    main()
    # repo.load_all()
    # for k,v in repo.concrete_flights.items():
    #     print(k,v)