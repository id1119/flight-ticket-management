import datetime
import csv
import inputs as iu

users = {}
flights = {}
concrete_flights = {}
airports = {}
airplane_models = {}
tickets = {}

def load_all():
    global users
    users = {}
    with open("csv_files/users.csv", "r", encoding="utf-8") as file:
        rows = csv.DictReader(file)
        for row in rows:
            username = row["username"]
            users[username] = row

    global flights
    flights = {}
    with open("csv_files/flights.csv", "r", encoding="utf-8") as file:
        rows = csv.DictReader(file)
        for row in rows:
            flight_number = row["flight_number"]
            flights[flight_number] = row

    global concrete_flights
    concrete_flights = {}
    with open("csv_files/concrete_flights.csv", "r", encoding="utf-8") as file:
        rows = csv.DictReader(file)
        for row in rows:
            concrete_flight_number = row["concrete_flight_number"]
            concrete_flights[concrete_flight_number] = row

    global airports
    airports = {}
    with open("csv_files/airports.csv", "r", encoding="utf-8") as file:
        rows = csv.DictReader(file)
        for row in rows:
            airport_code = row["airport_code"]
            airports[airport_code] = row

    global airplane_models
    airplane_models = {}
    with open("csv_files/airplane_models.csv", "r", encoding="utf-8") as file:
        rows = csv.DictReader(file)
        for row in rows:
            model = row["model"]
            airplane_models[model] = row

    global tickets
    tickets = {}
    with open("csv_files/tickets.csv", "r", encoding="utf-8") as file:
        rows = csv.DictReader(file)
        for row in rows:
            ticket = row["ticket_number"]
            tickets[ticket] = row

def save_all():

    users_fields = [
        "username", "password", "name", "last_name", "position",
        "passport_number", "citizenship", "phone_number", "email", "gender"
    ]
    with open("csv_files/users.csv", "w", newline="", encoding="utf-8") as file:  # newline izbegava prazne redove
        writer = csv.DictWriter(file, fieldnames=users_fields)
        writer.writeheader()
        for username, values in users.items():
            row = {"username": username, **values}  # **values koristimo zato sto prosledjujemo kao red samo JEDAN recnik a da
            writer.writerow(row)

    flights_fields = [
        "flight_number", "departure_airport", "arrival_airport","departure_time",
        "arrival_time", "next_day_arrival", "airline", "days_of_flight", "airplane_model", "price"
    ]
    with open("csv_files/flights.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=flights_fields)
        writer.writeheader()
        for flight_number, values in flights.items():
            row = {"flight_number":flight_number, **values}
            writer.writerow(row)

    concrete_flights_fields = [
        "concrete_flight_number","flight_number", "departure_airport", "arrival_airport", "departure_date", "arrival_date",
        "departure_time", "arrival_time", "next_day_arrival", "airline", "airplane_model", "price"
    ]
    with open("csv_files/concrete_flights.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=concrete_flights_fields)
        writer.writeheader()
        for concrete_flight_number, values in concrete_flights.items():
            row = {"concrete_flight_number":concrete_flight_number, **values}
            writer.writerow(row)

    airports_fields = [
        "airport_code", "airport_name", "city", "country"
    ]
    with open("csv_files/airports.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=airports_fields)
        writer.writeheader()
        for airport_code, values in airports.items():
            row = {"airport_code":airport_code, **values}
            writer.writerow(row)

    airplane_models_fields = [
        "model", "rows", "seats"
    ]
    with open("csv_files/airplane_models.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=airplane_models_fields)
        writer.writeheader()
        for model, values in airplane_models.items():
            row = {"model":model, **values}
            writer.writerow(row)

    tickets_fields = [
        "ticket_number", "concrete_flight_number", "buyer_username", "passenger_name", "passenger_last_name", "check_in", "seat"
    ]
    with open("csv_files/tickets.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=tickets_fields)
        writer.writeheader()
        for ticket_number, values in tickets.items():
            row = {"ticket_number": ticket_number, **values}
            writer.writerow(row)

concrete_flights_fields = [
        "concrete_flight_number", "flight_number", "departure_airport", "arrival_airport", "departure_date",
        "arrival_date",
        "departure_time", "arrival_time", "next_day_arrival", "airline", "airplane_model", "price", "has_free_seats"
    ]

def concrete_flights_print_header():
    global concrete_flights_fields
    print()
    print(
        f"{concrete_flights_fields[0]:^15} | {concrete_flights_fields[1]:^15} | {concrete_flights_fields[2]:^15} | {concrete_flights_fields[3]:^15} | {concrete_flights_fields[4]:^15} | {concrete_flights_fields[5]:^15} | {concrete_flights_fields[6]:^15} | {concrete_flights_fields[7]:^15} | {concrete_flights_fields[8]:^15} | {concrete_flights_fields[9]:^24} | {concrete_flights_fields[10]:^15} | {concrete_flights_fields[11]:^15}")
    print("-" * 230)


def available_flights():
    today= datetime.datetime.today()
    global concrete_flights_fields
    concrete_flights_print_header()
    for concrete_flight_number, values in concrete_flights.items():                #uzima svaki datum
        departure_date = datetime.datetime.strptime(concrete_flights[concrete_flight_number]["departure_date"],"%d.%m.%Y")   #konvertuje string datuma u datum
        if departure_date >= today:
            print(f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^17} | {values[concrete_flights_fields[3]]:^15} | {values[concrete_flights_fields[4]]:^15} | {values[concrete_flights_fields[5]]:^15} | {values[concrete_flights_fields[6]]:^15} | {values[concrete_flights_fields[7]]:^15} | {values[concrete_flights_fields[8]]:^16} | {values[concrete_flights_fields[9]]:^24} | {values[concrete_flights_fields[10]]:^15} | {values[concrete_flights_fields[11]]:^15}")

def search_by(parameter, value):
    global concrete_flights_fields
    concrete_flights_print_header()
    for concrete_flight_number, values in concrete_flights.items():
            if concrete_flights[concrete_flight_number][parameter]== value:
                print(f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^17} | {values[concrete_flights_fields[3]]:^15} | {values[concrete_flights_fields[4]]:^15} | {values[concrete_flights_fields[5]]:^15} | {values[concrete_flights_fields[6]]:^15} | {values[concrete_flights_fields[7]]:^15} | {values[concrete_flights_fields[8]]:^16} | {values[concrete_flights_fields[9]]:^24} | {values[concrete_flights_fields[10]]:^15} | {values[concrete_flights_fields[11]]:^15}")


def search_by_multiple(concrete_flights_copy, parameter, value):         #prosledjujem recnik zato sto nije dobro brisati kljuc u recniku dok se iterira kroz njega. dodje do greske
    for flight_number in list(concrete_flights_copy.keys()):             #gledamo recnik kao listu
        if concrete_flights_copy[flight_number][parameter] != value:
            del concrete_flights_copy[flight_number]

def print_search_by_multiple(concrete_flights_copy):
    global concrete_flights_fields
    concrete_flights_print_header()

    for flight_number, values in concrete_flights_copy.items():
        print(f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^17} | {values[concrete_flights_fields[3]]:^15} | {values[concrete_flights_fields[4]]:^15} | {values[concrete_flights_fields[5]]:^15} | {values[concrete_flights_fields[6]]:^15} | {values[concrete_flights_fields[7]]:^15} | {values[concrete_flights_fields[8]]:^16} | {values[concrete_flights_fields[9]]:^24} | {values[concrete_flights_fields[10]]:^15} | {values[concrete_flights_fields[11]]:^15}")


def print_ten_cheapest_flights(concrete_flights_copy):
    sorted_flights = dict(                          # sortiramo recnik preko liste pa vracamo u recnik zato sto ne moze da se sortira direktno recnik
        sorted(
            concrete_flights_copy.items(),          #uzimamo 10 najjeftinijih letova
            key=lambda item: int(item[1]["price"])  # item = ("JU01", {"price": "120"}) lambda se koristi kako bi usli u vrednosti recnika, da ga nema sortirali bi samo po nazivima a ne po vrednostima(ceni)
        )[:10]
    )
    cheapest_sorted_flights = dict(
        sorted(
            sorted_flights.items(),                 #sortiramo opadajuce
            key=lambda item: int(item[1]["price"]),
            reverse = True
        )
    )
    global concrete_flights_fields
    concrete_flights_print_header()
    for flight_number, values in cheapest_sorted_flights.items():
        print(f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^17} | {values[concrete_flights_fields[3]]:^15} | {values[concrete_flights_fields[4]]:^15} | {values[concrete_flights_fields[5]]:^15} | {values[concrete_flights_fields[6]]:^15} | {values[concrete_flights_fields[7]]:^15} | {values[concrete_flights_fields[8]]:^16} | {values[concrete_flights_fields[9]]:^24} | {values[concrete_flights_fields[10]]:^15} | {values[concrete_flights_fields[11]]:^15}")

def print_flights_by_search_date(concrete_flights_copy, date, days):
    date_delta = datetime.datetime.strptime(date, "%d.%m.%Y")
    days_delta = datetime.timedelta(days=int(days))

    date_min = date_delta - days_delta
    date_max = date_delta + days_delta

    global concrete_flights_fields
    concrete_flights_print_header()

    for flight_number, values in concrete_flights_copy.items():
        concrete_flight_date = datetime.datetime.strptime(concrete_flights_copy[flight_number]["departure_date"], "%d.%m.%Y")
        if date_min <= concrete_flight_date <= date_max:
            print(f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^17} | {values[concrete_flights_fields[3]]:^15} | {values[concrete_flights_fields[4]]:^15} | {values[concrete_flights_fields[5]]:^15} | {values[concrete_flights_fields[6]]:^15} | {values[concrete_flights_fields[7]]:^15} | {values[concrete_flights_fields[8]]:^16} | {values[concrete_flights_fields[9]]:^24} | {values[concrete_flights_fields[10]]:^15} | {values[concrete_flights_fields[11]]:^15}")

def buy_ticket(concrete_flight_number):
    pass


def has_free_seats(concrete_flight_number):
    airplane_model = concrete_flights[concrete_flight_number]["airplane_model"]
    seats_in_row = len((airplane_models[airplane_model]["seats"]).split("|"))
    total_seats = int(airplane_models[airplane_model]["rows"]) * seats_in_row
    used_seats = 0
    for ticket, values in tickets.items():
        if tickets[ticket]["concrete_flight_number"] == concrete_flight_number:
            used_seats+=1
    free_seats = total_seats - used_seats
    return free_seats

def generate_ticket_number():
    max_ticket = 0
    for ticket in tickets.keys():
        if int(ticket)>max_ticket:
            max_ticket = int(ticket)
    max_ticket+=1
    return max_ticket

def view_connected_flights(flight_number):
    arrival_date = concrete_flights[flight_number]["arrival_date"]
    arrival_time = concrete_flights[flight_number]["arrival_time"]
    date_time = datetime.datetime.strptime(arrival_date, arrival_time)

def print_by_dt_min_max(concrete_flights_copy, arrival_dt, arrival_dt_max):
    global concrete_flights_fields
    concrete_flights_print_header()

    for concrete_flight_number, values in concrete_flights_copy.items():
        departure_date = concrete_flights_copy[concrete_flight_number]["departure_date"]
        departure_time = concrete_flights_copy[concrete_flight_number]["departure_time"]
        current_dt = datetime.datetime.strptime(
            departure_date + " " + departure_time,
            "%d.%m.%Y %H:%M"
        )

        if arrival_dt < current_dt <= arrival_dt_max:
            print(
                f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^17} | {values[concrete_flights_fields[3]]:^15} | {values[concrete_flights_fields[4]]:^15} | {values[concrete_flights_fields[5]]:^15} | {values[concrete_flights_fields[6]]:^15} | {values[concrete_flights_fields[7]]:^15} | {values[concrete_flights_fields[8]]:^16} | {values[concrete_flights_fields[9]]:^24} | {values[concrete_flights_fields[10]]:^15} | {values[concrete_flights_fields[11]]:^15}")

def print_available_tickets_for_user(logged_username):
    tickets_fields = [
        "ticket_number", "concrete_flight_number", "buyer_username", "passenger_name", "passenger_last_name", "seat"
    ]
    print()
    print(f"{tickets_fields[0]:^15} | {tickets_fields[1]:^15} | {tickets_fields[2]:^15} | {tickets_fields[3]:^15} | {tickets_fields[4]:^15} | {tickets_fields[5]:^12}")
    print("-" * 111)
    for ticket_number, values in tickets.items():
        if tickets[ticket_number]["buyer_username"] == logged_username:
            print(f"{values[tickets_fields[0]]:^15} | {values[tickets_fields[1]]:^22} | {values[tickets_fields[2]]:^15} | {values[tickets_fields[3]]:^15} | {values[tickets_fields[4]]:^19} | {values[tickets_fields[5]]:^15}")

def is_ticket_ready_for_checkin(ticket_number, logged_username):
    concrete_flight_number = tickets[ticket_number]["concrete_flight_number"]
    departure_date = concrete_flights[concrete_flight_number]["departure_date"]
    departure_time = concrete_flights[concrete_flight_number]["departure_time"]

    departure_dt = datetime.datetime.strptime(
        departure_date + " " + departure_time,
        "%d.%m.%Y %H:%M"
    )
    current_dt = datetime.datetime.today()
    current_dt_min = departure_dt - datetime.timedelta(hours=48)
    if current_dt_min<=current_dt<=departure_dt:
        if users[logged_username]["passport_number"] == "":
            users[logged_username]["passport_number"] = iu.enter_passport()
        if users[logged_username]["citizenship"] == "":
            users[logged_username]["citizenship"] = iu.enter_name("citizenship")
        if users[logged_username]["gender"] == "":
            users[logged_username]["gender"] = iu.enter_name("gender")
        tickets[ticket_number]["check_in"] = "yes"
        print("Successful check-in!")

    else:
        print("[ERROR] Check-out can only be done 48 hours before flight")


if __name__ == '__main__':
    load_all()
    # print(print_available_tickets_for_user())