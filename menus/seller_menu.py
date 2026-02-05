import projekat.repository as repo
import projekat.inputs as iu
import copy

from projekat.inputs import enter_name
from projekat.main import *
import datetime

flights_copy = {}

def seller_menu():
    print("====MENU====")
    print("Status: seller")
    print("2) Exit application")
    print("3) View available flights")
    print("4) Search flight by")
    print("5) Search flight by multiple parameters")
    print("6) View 10 cheapest flights between two destinations")
    print("7) View flights at certain date +- flexible days")
    print("9) Logout")
    print("13) Buy ticket")
    print("14) Check-in")
    print("15) Change ticket info")
    print("16) Delete ticket")
    print("17) Search ticket by")



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

def buy_ticket_menu():
    print("===Buy Ticket===")
    print("1) Show all available flights for your destination")
    print("2) Enter concrete flight number: ")
    print("x) Go back")

def change_ticket_info_menu():
    print("===Change ticket info===")
    print("1) Concrete flight number")
    print("2) Departure date")
    print("3) Seat")
    print("x) Go back to main menu")

def search_ticket_by_menu():
    print("===Search ticket by===")
    print("1) Departure airport")
    print("2) Arrival airport")
    print("3) Departure date")
    print("4) Arrival date")
    print("5) Passenger name and lastname")
    print("x) Go back to main menu")

def seller_menu_main(logged_username):
    repo.load_all()
    while True:
        print(seller_menu())
        choice = input("Please choose functionality: ")
        if choice == '2':
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

            global flights_copy
            global concrete_flights_copy
            flights_copy = copy.deepcopy(repo.flights)
            concrete_flights_copy = copy.deepcopy(repo.concrete_flights)

            while True:
                search_flight_by_multiple_menu()
                choose = input("Select one of parameters that you want to search by: ")
                if choose == '1':
                    parameter = "departure_airport"
                    value = input("Enter departure airport: ")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '2':
                    parameter = "arrival_airport"
                    value = input("Enter arrival airport: ")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '3':
                    parameter = "departure_date"
                    value = input("Enter departure date: ")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '4':
                    parameter = "arrival_date"
                    value = input("Enter arrival date: ")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '5':
                    parameter = "departure_time"
                    value = input("Enter departure time: ")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '6':
                    parameter = "arrival_time"
                    value = input("Enter arrival time: ")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '7':
                    parameter = "airline"
                    value = input("Enter airline: ")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == 's':
                    repo.print_search_by_multiple(flights_copy, concrete_flights_copy)
                elif choose == 'x':
                    print("Going back..")
                    break
                else:
                    print("[ERROR] Invalid input!")
        elif choice == '6':
            flights_copy = copy.deepcopy(repo.flights)
            concrete_flights_copy = copy.deepcopy(repo.concrete_flights)
            departure_airport = input("Enter departure airport: ")
            repo.search_by_multiple(flights_copy, concrete_flights_copy, "departure_airport", departure_airport)
            arrival_airport = input("Enter arrival airport: ")
            repo.search_by_multiple(flights_copy, concrete_flights_copy, "arrival_airport", arrival_airport)
            repo.print_ten_cheapest_flights(flights_copy)
        elif choice == '7':
            while True:
                flights_copy = copy.deepcopy(repo.flights)
                concrete_flights_copy = copy.deepcopy(repo.concrete_flights)

                departure_airport = input("Enter departure airport: ")
                repo.search_by_multiple(flights_copy, concrete_flights_copy, "departure_airport", departure_airport)

                arrival_airport = input("Enter arrival airport: ")
                repo.search_by_multiple(flights_copy, concrete_flights_copy, "arrival_airport", arrival_airport)

                date = input("Enter date of flight: ")
                days = input("Enter number of flexible days: ")
                try:
                    repo.print_flights_by_search_date(flights_copy, concrete_flights_copy, date, days)
                    break
                except Exception:
                    print("[ERROR] Invalid date!")
        elif choice == '9':
            return "unregistered"
        elif choice == '13':
            while True:
                buy_ticket_menu()
                choose = input("Enter option: ")
                if choose =='1':

                    flights_copy = copy.deepcopy(repo.flights)
                    concrete_flights_copy = copy.deepcopy(repo.concrete_flights)
                    departure_airport = input("Enter departure airport: ")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy,"departure_airport", departure_airport)
                    arrival_airport = input("Enter arrival airport: ")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy,"arrival_airport", arrival_airport)
                    repo.print_search_by_multiple_concrete(flights_copy, concrete_flights_copy)
                elif choose == '2':
                    while True:
                        concrete_flight_number = iu.enter_concrete_flight_number(repo.concrete_flights)
                        if concrete_flight_number == 'x':
                            break
                        if not repo.has_free_seats(concrete_flight_number):
                            print("No available seats in this concrete flight, please try again.")
                            continue
                        print("==Are you already registered?==")
                        print("1) Yes!")
                        print("2) No!")
                        print("x) Go back")
                        choose1 = input("Enter answer: ")
                        if choose1 == '1':
                            while True:
                                username = iu.enter_name("username")
                                if username in repo.users:
                                    break
                                else:
                                    print("Entered username doesnt exist!")
                            ticket_number = repo.generate_ticket_number()
                            name = repo.users[username]["name"]
                            last_name = repo.users[username]["last_name"]
                            repo.tickets[ticket_number]={
                                "concrete_flight_number":concrete_flight_number,
                                "buyer_username": username,
                                "passenger_name":name,
                                "passenger_last_name":last_name,
                                "check_in":"no"
                            }
                        elif choose1 == '2':
                            ticket_number = repo.generate_ticket_number()
                            name = iu.enter_name("passenger name")
                            last_name = iu.enter_name("passenger last name")
                            repo.tickets[ticket_number]={
                                "concrete_flight_number":concrete_flight_number,
                                "buyer_username": logged_username,
                                "passenger_name":name,
                                "passenger_last_name":last_name,
                                "check_in":"no"
                            }
                        elif choose1 == "x":
                            break
                        else:
                            print("[ERROR] Invalid input! Please try again.")
                elif choose == 'x':
                    break
                else:
                    print("[ERROR] Invalid input! Please try again.")
        elif choice == '14':
            ticket_number = iu.enter_ticket_number()  # unosi broj karte

            if not repo.is_ticket_ready_for_checkin(ticket_number,
                                                    logged_username):  # provera da li je spremno za cekiranje
                continue
            taken_seats = repo.get_taken_seats(ticket_number)  # pravi skup zauzetih mesta

            rows = repo.print_taken_seats(taken_seats,
                                          ticket_number)  # ispisuje sva zauzeta sedista i vraca broj redova

            repo.tickets[ticket_number]["seat"] = iu.enter_seat(taken_seats, rows)  # unos sedista
        elif choice == '15':
            while True:
                print("===Change ticket info===")
                print("x) Go back")
                print("1) Enter ticket number")
                choose = input("Enter option: ")
                if choose == '1':
                    ticket_number = iu.enter_ticket_number()
                    change_ticket_info_menu()
                    choose = input("Enter option: ")
                    if choose == "1":
                        while True:
                            concrete_flight_number = iu.enter_concrete_flight_number(repo.concrete_flights)

                            if concrete_flight_number not in repo.concrete_flights:
                                print("Concrete flight doesnt exist")
                                continue

                            repo.tickets[ticket_number]["concrete_flight_number"] = concrete_flight_number
                            print("Successful")
                            break
                    if choose == "2":
                        departure_date = iu.enter_name("departure date")
                        repo.change_ticket_date(ticket_number, departure_date)
                        concrete_flight_number = iu.enter_concrete_flight_number(repo.concrete_flights)
                        if not concrete_flight_number:
                            continue
                        repo.tickets[ticket_number]["concrete_flight_number"] = concrete_flight_number
                    if choose == "3":
                        taken_seats = repo.get_taken_seats(ticket_number)  # pravi skup zauzetih mesta

                        rows = repo.print_taken_seats(taken_seats, ticket_number)  # ispisuje sva zauzeta sedista i vraca broj redova

                        repo.tickets[ticket_number]["seat"] = iu.enter_seat(taken_seats, rows)  # unos sedista
                elif choose == 'x':
                    break
                else:
                    print("[ERROR] Invalid input! Please try again.")
        elif choice == '16':
            while True:
                print("===Delete ticket===")
                print("x) Go back")
                print("1) Enter ticket number")
                choose = input("Enter option: ")
                if choose == '1':

                    while True:

                        ticket_number = iu.enter_ticket_number()

                        if ticket_number not in repo.tickets:
                            print("Ticket doesnt exist!")
                            continue

                        repo.tickets[ticket_number]["deleted"] = "yes"
                        break

                elif choose == 'x':
                    break
                else:
                    print("[ERROR] Invalid input! Please try again.")
        elif choice == '17':
            while True:
                search_ticket_by_menu()
                choose = input("Enter option: ")
                if choose == '1':
                    parameter = "departure_airport"
                    value = input("Enter departure airport: ")
                    repo.search_ticket_by_airport(parameter, value)
                elif choose == '2':
                    parameter = "arrival_airport"
                    value = input("Enter arrival airport: ")
                    repo.search_ticket_by_airport(parameter, value)
                elif choose == '3':
                    parameter = "departure_date"
                    value = input("Enter departure date: ")
                    repo.search_ticket_by_date(parameter, value)
                elif choose == '4':
                    parameter = "arrival_date"
                    value = input("Enter arrival date: ")
                    repo.search_ticket_by_date(parameter, value)
                elif choose == '5':
                    passenger_name = iu.enter_name("name")
                    passenger_last_name = iu.enter_name("last name")
                    repo.search_ticket_by_name(passenger_name, passenger_last_name)
                elif choose == 'x':
                    break
                else:
                    print("[ERROR] Invalid input! Please try again.")
        else:
            print("[ERROR] Invalid input! Please try again.")
# if __name__ == '__main__':
    # unregistered_menu_main()