import repository as repo
import inputs as iu

def menu():
    print("====MENU====")
    print("1) Login")
    print("2) Exit application")
    print("3) View available flights")
    print("4) Search flight by")

def search_flight_by_menu():
    print("===Search flight by===")
    print("1) Departure airport")
    print("2) Arrival airport")
    print("3) Departure date")
    print("4) Arrival date")
    print("5) Departure time")
    print("6) Airline")

def main():
    while True:
        repo.load_all()
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
                choose=''
                search_flight_by_menu()
                choose == input("What do you want to search by?: ")
                if choose == '1':
                    parameter = "departure_airport"
                    value = input("Enter departure airport")
                    repo.search_by(parameter, value)
                # elif choice == '':
                # elif choice == '':
                # elif choice == '':
                # elif choice == '':
                # elif choice == '':








if __name__=="__main__":
    main()
    # repo.load_all()
    # for k,v in repo.concrete_flights.items():
    #     print(k,v)