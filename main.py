import repository as repo
import inputs as iu
import universal_menu as uni
import copy

concrete_flights_copy = {}
def universal_menu():
    print("====MENU====")
    print("1) Login")
    print("2) Exit application")
    print("3) View available flights")
    print("4) Search flight by")
    print("5) Search flight by multiple parameters")
    print("6) View 10 cheapest flights between two destinations")
    print("7) View flights at certain date +- flexible days")

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
    uni.universal_menu()


if __name__=="__main__":
    main()
    # repo.load_all()
    # for k,v in repo.concrete_flights.items():
    #     print(k,v)