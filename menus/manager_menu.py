import projekat.repository as repo
import projekat.inputs as iu
import copy

from projekat.inputs import enter_name
from projekat.main import *
import datetime

flights_copy = {}
concrete_flights_copy = {}

def manager_menu():
    print("====MENU====")
    print("Status: manager")
    print("2) Exit application")
    print("3) View available flights")
    print("4) Search flight by")
    print("5) Search flight by multiple parameters")
    print("6) View 10 cheapest flights between two destinations")
    print("7) View flights at certain date +- flexible days")
    print("9) Logout")
    print("17) Search ticket by")
    print("18) Register new seller")
    print("19) Make new flight")
    print("20) Change flight info")
    print("21) Delete tickets")
    print("22) Generate reports")


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

def change_flight_info_menu():
    print("===Change flight info===")
    print("1) Departure airport")
    print("2) Arrival airport")
    print("3) Departure time")
    print("4) Arrival time")
    print("5) Next day arrival")
    print("6) Airline")
    print("7) Airplane model")
    print("8) Price")
    print("x) Go back to main menu")

def tickets_reports_menu():
    print("===Generate reports for===")
    print("1) Purchase date")
    print("2) Departure date")
    print("3) Purchase date and seller username")
    print("4) Purchase date, total tickets and price")
    print("5) Departure date, total tickets and price")
    print("6) Purchase date, seller username, total tickets and price")
    print("7) Total tickets and price in last 30 days")
    print("x) Go back")


def manager_menu_main(logged_username):
    repo.load_all()
    while True:
        manager_menu()
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
                    value = enter_name("departure airport")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '2':
                    parameter = "arrival_airport"
                    value = enter_name("arrival airport")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '3':
                    parameter = "departure_date"
                    value = enter_name("departure date")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '4':
                    parameter = "arrival_date"
                    value = enter_name("arrival date")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '5':
                    parameter = "departure_time"
                    value = enter_name("departure time")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '6':
                    parameter = "arrival_time"
                    value = enter_name("arrival time")
                    repo.search_by_multiple(flights_copy, concrete_flights_copy, parameter, value)
                elif choose == '7':
                    parameter = "airline"
                    value = enter_name("airline")
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
        elif choice == '18':
            username = iu.enter_name("username")
            password = iu.enter_name("password")
            name = iu.enter_name("name")
            last_name = iu.enter_name("last name")
            phone_number = iu.enter_name("phone number")
            email = iu.enter_email()
            position = "seller"
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
        elif choice == '19':
            flight_number = iu.enter_name("flight number").upper()
            departure_airport = iu.enter_name("departure airport").upper()
            arrival_airport = iu.enter_name("arrival airport").upper()
            departure_time = iu.enter_name("departure time")
            arrival_time = iu.enter_name("arrival time")
            next_day_arrival = iu.enter_next_day_arrival()
            airline = iu.enter_name("airline")
            days_of_flight = iu.enter_days_of_flight().title()
            airplane_model = iu.enter_airplane_model().upper()
            price = iu.enter_price()
            repo.flights[flight_number]= {
                "departure_airport":departure_airport,
                "arrival_airport":arrival_airport,
                "departure_time":departure_time,
                "arrival_time":arrival_time,
                "next_day_arrival":next_day_arrival,
                "airline":airline,
                "days_of_flight":days_of_flight,
                "airplane_model":airplane_model,
                "price":price
            }
        elif choice == '20':
            while True:
                print("===Edit flight info===")
                print("x) Go back")
                print("1) Enter flight number")
                choose = input("Enter option: ")
                if choose == '1':
                    flight_number = iu.enter_name("flight number")
                    while True:
                        change_flight_info_menu()
                        choose = input("Enter option: ")
                        if choose == '1':
                            departure_airport = iu.enter_name("departure airport").upper()
                            repo.flights[flight_number]["departure_airport"] = departure_airport
                        elif choose == '2':
                            arrival_airport = iu.enter_name("arrival airport").upper()
                            repo.flights[flight_number]["arrival_airport"] = arrival_airport
                        elif choose == '3':
                            departure_time = iu.enter_name("departure time")
                            repo.flights[flight_number]["departure_time"] = departure_time
                        elif choose == '4':
                            arrival_time = iu.enter_name("arrival time")
                            repo.flights[flight_number]["arrival_time"] = arrival_time
                        elif choose == '5':
                            next_day_arrival = iu.enter_next_day_arrival()
                            repo.flights[flight_number]["next_day_arrival"] = next_day_arrival
                        elif choose == '6':
                            airline = iu.enter_name("airline")
                            repo.flights[flight_number]["airline"] = airline
                        elif choose == '7':
                            airplane_model = iu.enter_airplane_model().upper()
                            repo.flights[flight_number]["airplane_model"] = airplane_model
                        elif choose == '8':
                            price = iu.enter_price()
                            repo.flights[flight_number]["price"] = price
                        elif choose == 'x':
                           break
                        else:
                            print("[ERROR] Invalid input! Please try again.")
                elif choose == 'x':
                    break
                else:
                    print("[ERROR] Invalid input! Please try again.")
        elif choice == '21':
            deletable_tickets = copy.deepcopy(repo.tickets)

            deletable_tickets = repo.print_deletable_tickets(deletable_tickets)
            while True:
                print("==Delete tickets===")
                print("1) Delete all tickets")
                print("2) Delete ticket")
                print("x) Go back")
                choose = input("Enter option: ")
                if choose == '1':
                    repo.delete_all_deletable_tickets(deletable_tickets)
                    print("You have successfully deleted all deletable flights")
                    break
                elif choose == '2':
                    while True:
                        print("x) Go back")
                        ticket_number = iu.enter_ticket_number()
                        if not ticket_number:
                            break
                        repo.delete_deletable_flight(deletable_tickets, ticket_number)
                elif choose == 'x':
                    break
                else:
                    print("[ERROR] Invalid input! Please try again.")
        elif choice == '22':
            while True:
                tickets_reports_menu()
                choose = input("Enter option: ")
                if choose == '1':
                    purchase_date = iu.enter_name("purchase date")
                    repo.print_all_tickets_for_purchase_date(purchase_date)
                elif choose == '2':
                    departure_date = enter_name("departure date")
                    repo.print_all_tickets_for_departure_date(departure_date)
                elif choose == '3':
                    purchase_date = iu.enter_name("purchase date")
                    seller_username = iu.enter_name("seller username")
                    repo.print_all_tickets_for_purchase_date_seller_username(purchase_date, seller_username)
                elif choose == '4':
                    purchase_date = iu.enter_name("purchase date")
                    repo.print_sum_price_tickets(purchase_date)
                elif choose == '5':
                    departure_date = iu.enter_name("departure date")
                    repo.print_sum_price_tickets_departure_date(departure_date)
                elif choose == '6':
                    purchase_date = iu.enter_name("purchase date")
                    seller_username = iu.enter_name("seller username")
                    repo.print_sum_price_tickets_seller_purchase_date(purchase_date, seller_username)
                elif choose == '7':
                    repo.sum_price_tickets_last_30_days()
                elif choose == 'x':
                    break
                else:
                    print("[ERROR] Invalid input! Please try again.")
        else:
            print("[ERROR] Invalid input! Please try again.")
# if __name__ == '__main__':
    # unregistered_menu_main()