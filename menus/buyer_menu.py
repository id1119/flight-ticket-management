import projekat.repository as repo
import projekat.inputs as iu
import copy
from projekat.main import *
import datetime
flights_copy = {}

def buyer_menu():
    print("====MENU====")
    print("Status: buyer")
    print("2) Exit application")
    print("3) View available flights")
    print("4) Search flight by")
    print("5) Search flight by multiple parameters")
    print("6) View 10 cheapest flights between two destinations")
    print("7) View flights at certain date +- flexible days")
    print("9) Logout")
    print("10) Buy ticket")
    print("11) View bought tickets")
    print("12) Ticket check-in")



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

def buyer_menu_main(logged_username):
    repo.load_all()
    global flights_copy
    while True:
        print(buyer_menu())
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
                    print("[ERROR] Invalid input! Please try again.")
        elif choice == '5':
            flights_copy = copy.deepcopy(repo.concrete_flights)
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
                    print("[ERROR] Invalid input! Please try again.")
        elif choice == '6':
            flights_copy = copy.deepcopy(repo.concrete_flights)
            departure_airport = input("Enter departure airport: ")
            repo.search_by_multiple(flights_copy, "departure_airport", departure_airport)
            arrival_airport = input("Enter arrival airport: ")
            repo.search_by_multiple(flights_copy, "arrival_airport", arrival_airport)
            repo.print_ten_cheapest_flights(flights_copy)
        elif choice == '7':
            while True:
                flights_copy = copy.deepcopy(repo.concrete_flights)
                departure_airport = input("Enter departure airport: ")
                repo.search_by_multiple(flights_copy, "departure_airport", departure_airport)
                arrival_airport = input("Enter arrival airport: ")
                repo.search_by_multiple(flights_copy, "arrival_airport", arrival_airport)
                date = input("Enter date of flight: ")
                days = input("Enter number of flexible days: ")
                try:
                    repo.print_flights_by_search_date(flights_copy, date, days)
                    break
                except Exception:
                    print("[ERROR] Invalid date!")
        elif choice == '9':
            return "unregistered"
        elif choice == '10':
            while True:
                buy_ticket_menu()
                choose = input("Enter option: ")
                if choose =='1':
                    flights_copy = copy.deepcopy(repo.concrete_flights)
                    departure_airport = input("Enter departure airport: ")
                    repo.search_by_multiple(flights_copy, "departure_airport", departure_airport)
                    arrival_airport = input("Enter arrival airport: ")
                    repo.search_by_multiple(flights_copy, "arrival_airport", arrival_airport)
                    repo.print_search_by_multiple(flights_copy)
                elif choose == '2':
                    while True:
                        concrete_flight_number = iu.enter_concrete_flight_number(repo.concrete_flights)
                        print("==Are you buying ticket for yourself?==")
                        print("1) Yes!")
                        print("2) No!")
                        print("x) Go back")
                        choose1 = input("Enter answer: ")
                        if choose1 == '1':
                            ticket_number = repo.generate_ticket_number()
                            name = repo.users[logged_username]["name"]
                            last_name = repo.users[logged_username]["last_name"]
                            repo.tickets[ticket_number]={
                                "concrete_flight_number":concrete_flight_number,
                                "buyer_username": logged_username,
                                "passenger_name":name,
                                "passenger_last_name":last_name
                            }
                            print("===Continue===")
                            print("1) Buy new ticket connected to current flight")
                            print("x) Go back")
                            choose2= input("Enter option: ")
                            if choose2 == '1':
                                flights_copy = copy.deepcopy(repo.concrete_flights)
                                arrival_airport = repo.concrete_flights[concrete_flight_number]["arrival_airport"]
                                repo.search_by_multiple(flights_copy, "departure_airport", arrival_airport)
                                arrival_date = repo.concrete_flights[concrete_flight_number]["arrival_date"]
                                arrival_time = repo.concrete_flights[concrete_flight_number]["arrival_time"]

                                arrival_dt = datetime.datetime.strptime(
                                    arrival_date + " " + arrival_time,
                                    "%d.%m.%Y. %H:%M"
                                )

                                arrival_dt_max = arrival_dt + datetime.timedelta(minutes=120)

                                repo.print_by_dt_min_max(flights_copy ,arrival_dt, arrival_dt_max)
                            elif choose2 == 'x':
                                break
                            else:
                                print("[ERROR] Invalid input! Please try again.")
                        elif choose1 == '2':
                            ticket_number = repo.generate_ticket_number()
                            name = iu.enter_name("passenger name")
                            last_name = iu.enter_name("passenger last name")
                            repo.tickets[ticket_number]={
                                "concrete_flight_number":concrete_flight_number,
                                "buyer_username": logged_username,
                                "passenger_name":name,
                                "passenger_last_name":last_name
                            }
                            while True:
                                print("===Continue===")
                                print("1) Buy ticket for same flight for new passenger")
                                print("x) Go back")
                                choose2= input("Enter option: ")
                                if choose2 == '1':
                                    ticket_number = repo.generate_ticket_number()
                                    name = iu.enter_name("passenger name")
                                    last_name = iu.enter_name("passenger last name")
                                    repo.tickets[ticket_number]={
                                    "concrete_flight_number":concrete_flight_number,
                                    "buyer_username": logged_username,
                                    "passenger_name":name,
                                    "passenger_last_name":last_name
                                }
                                elif choose2 == 'x':
                                    break
                                else:
                                    print("[ERROR] Invalid input! Please try again.")
                        elif choose1 == "x":
                            break
                        else:
                            print("[ERROR] Invalid input! Please try again.")
                elif choose == 'x':
                    break
                else:
                    print("[ERROR] Invalid input! Please try again.")
            else:
                print("[ERROR] Invalid input! Please try again.")
        elif choice == '11':
            repo.print_available_tickets_for_user(logged_username)
        elif choice == '12':
            ticket_number = iu.enter_ticket_number()
            repo.is_ticket_ready_for_checkin(ticket_number, logged_username)
        else:
            print("[ERROR] Invalid input! Please try again.")
if __name__ == '__main__':
    buyer_menu()