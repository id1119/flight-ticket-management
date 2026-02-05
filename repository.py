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
        "concrete_flight_number","flight_number", "departure_date", "arrival_date",
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
    "concrete_flight_number", "flight_number", "departure_date", "arrival_date",
]

flights_fields = [
    "flight_number", "departure_airport", "arrival_airport", "departure_time",
    "arrival_time", "next_day_arrival", "airline", "days_of_flight", "airplane_model", "price"
]

def concrete_flights_print_header():
    global concrete_flights_fields
    print()
    print(f"{concrete_flights_fields[0]:^15} | {concrete_flights_fields[1]:^15} | {concrete_flights_fields[2]:^17} | {concrete_flights_fields[3]:^15} ")
    print("-" * 79)

def available_flights():
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) #today = današnji datum + trenutno vreme, zbog biblioteke mora ovako
    global concrete_flights_fields
    concrete_flights_print_header()
    for concrete_flight_number, values in concrete_flights.items():                #uzima svaki datum
        departure_date = datetime.datetime.strptime(concrete_flights[concrete_flight_number]["departure_date"],"%d.%m.%Y.")   #konvertuje string datuma u datum
        if departure_date >= today:
            print(f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^17} | {values[concrete_flights_fields[3]]:^15} ")

def flight_info_print_header():
    global concrete_flights_fields
    global flights_fields
    print()
    print(f"{flights_fields[0]:^15} | {flights_fields[1]:^19} | {flights_fields[2]:^15} | {concrete_flights_fields[2]:^17} | {concrete_flights_fields[3]:^15} | {flights_fields[3]:^15} | {flights_fields[4]:^15} | {flights_fields[5]:^16} | {flights_fields[6]:^15} | {flights_fields[7]:^24} | {flights_fields[8]:^15} | {flights_fields[9]:^15}")
    print("-" * 230)

def search_by(parameter, value):
    global concrete_flights_fields
    global flights_fields
    flight_info_print_header()
    if parameter != "departure_date" and parameter != "arrival_date":
        for flight_number, values in flights.items():
            for concrete_flight_number, concrete_values in concrete_flights.items():
                if flights[flight_number][parameter] == value and concrete_flights[concrete_flight_number]["flight_number"] == flight_number:
                    print(f"{values[flights_fields[0]]:^15} | {values[flights_fields[1]]:^19} | {values[flights_fields[2]]:^15} | {concrete_values[concrete_flights_fields[2]]:^17} | {concrete_values[concrete_flights_fields[3]]:^15} | {values[flights_fields[3]]:^15} | {values[flights_fields[4]]:^15} | {values[flights_fields[5]]:^16} | {values[flights_fields[6]]:^15} | {values[flights_fields[7]]:^24} | {values[flights_fields[8]]:^15} | {values[flights_fields[9]]:^15}")
    else:
        for flight_number, values in flights.items():
            for concrete_flight_number, concrete_values in concrete_flights.items():
                if concrete_flights[concrete_flight_number]["flight_number"] == flight_number and concrete_flights[concrete_flight_number][parameter] == value:
                    print(f"{values[flights_fields[0]]:^15} | {values[flights_fields[1]]:^19} | {values[flights_fields[2]]:^15} | {concrete_values[concrete_flights_fields[2]]:^17} | {concrete_values[concrete_flights_fields[3]]:^15} | {values[flights_fields[3]]:^15} | {values[flights_fields[4]]:^15} | {values[flights_fields[5]]:^16} | {values[flights_fields[6]]:^15} | {values[flights_fields[7]]:^24} | {values[flights_fields[8]]:^15} | {values[flights_fields[9]]:^15}")

def search_by_multiple(flights_copy, concrete_flights_copy,  parameter, value):         #prosledjujem recnik zato sto nije dobro brisati kljuc u recniku dok se iterira kroz njega. dodje do greske
    if parameter != "departure_date" and parameter != "arrival_date":
        for flight_number in list(flights_copy.keys()):             #gledamo recnik kao listu
            if flights_copy[flight_number][parameter] != value:
                del flights_copy[flight_number]

    else:
        for concrete_flight_number in list(concrete_flights_copy.keys()):
            if concrete_flights_copy[concrete_flight_number]["flight_number"] not in flights_copy:     #or concrete_flights[concrete_flight_number][parameter] != value:
                del concrete_flights_copy[concrete_flight_number]

def print_search_by_multiple(flights_copy, concrete_flights_copy):
    global concrete_flights_fields
    global flights_fields
    flight_info_print_header()

    for flight_number, values in flights_copy.items():
        for concrete_flight_number, concrete_values in concrete_flights_copy.items():
            if concrete_flights[concrete_flight_number]["flight_number"] == flight_number:
                print(f"{values[flights_fields[0]]:^15} | {values[flights_fields[1]]:^19} | {values[flights_fields[2]]:^15} | {concrete_values[concrete_flights_fields[2]]:^17} | {concrete_values[concrete_flights_fields[3]]:^15} | {values[flights_fields[3]]:^15} | {values[flights_fields[4]]:^15} | {values[flights_fields[5]]:^16} | {values[flights_fields[6]]:^15} | {values[flights_fields[7]]:^24} | {values[flights_fields[8]]:^15} | {values[flights_fields[9]]:^15}")

def print_ten_cheapest_flights(flights_copy):
    sorted_flights = dict(                          # sortiramo recnik preko liste pa vracamo u recnik zato sto ne moze da se sortira direktno recnik
        sorted(
            flights_copy.items(),          #uzimamo 10 najjeftinijih letova
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
    global flights_fields
    global concrete_flights_fields
    flight_info_print_header()

    for flight_number, values in cheapest_sorted_flights.items():
        for concrete_flight_number, concrete_values in concrete_flights.items():
            if concrete_flights[concrete_flight_number]["flight_number"] == flight_number:
                print(f"{values[flights_fields[0]]:^15} | {values[flights_fields[1]]:^19} | {values[flights_fields[2]]:^15} | {concrete_values[concrete_flights_fields[2]]:^17} | {concrete_values[concrete_flights_fields[3]]:^15} | {values[flights_fields[3]]:^15} | {values[flights_fields[4]]:^15} | {values[flights_fields[5]]:^16} | {values[flights_fields[6]]:^15} | {values[flights_fields[7]]:^24} | {values[flights_fields[8]]:^15} | {values[flights_fields[9]]:^15}")

def print_flights_by_search_date(flights_copy, concrete_flights_copy, date, days):
    date_delta = datetime.datetime.strptime(date, "%d.%m.%Y.")
    days_delta = datetime.timedelta(days=int(days))

    date_min = date_delta - days_delta
    date_max = date_delta + days_delta

    global concrete_flights_fields
    global flights_fields
    flight_info_print_header()

    for concrete_flight_number in list(concrete_flights_copy.keys()):
        concrete_flight_date = datetime.datetime.strptime(
            concrete_flights_copy[concrete_flight_number]["departure_date"], "%d.%m.%Y.")
        if not (date_min <= concrete_flight_date <= date_max):
            del concrete_flights_copy[concrete_flight_number]

    for flight_number, values in flights_copy.items():
        for concrete_values in concrete_flights_copy.values():
            flight_number = concrete_values["flight_number"]
            if flight_number in flights_copy:
                print(f"{values[flights_fields[0]]:^15} | {values[flights_fields[1]]:^19} | {values[flights_fields[2]]:^15} | {concrete_values[concrete_flights_fields[2]]:^17} | {concrete_values[concrete_flights_fields[3]]:^15} | {values[flights_fields[3]]:^15} | {values[flights_fields[4]]:^15} | {values[flights_fields[5]]:^16} | {values[flights_fields[6]]:^15} | {values[flights_fields[7]]:^24} | {values[flights_fields[8]]:^15} | {values[flights_fields[9]]:^15}")

def print_search_by_multiple_concrete(flights_copy, concrete_flights_copy):
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    global concrete_flights_fields

    concrete_flights_print_header()

    for flight_number, values in flights_copy.items():
        for concrete_flight_number, values in concrete_flights_copy.items():                #uzima svaki datum
            if concrete_flights[concrete_flight_number]["flight_number"] == flight_number:
                departure_date = datetime.datetime.strptime(concrete_flights_copy[concrete_flight_number]["departure_date"],"%d.%m.%Y.")   #konvertuje string datuma u datum
                if departure_date >= today:
                    print(f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^17} | {values[concrete_flights_fields[3]]:^15} ")

def has_free_seats(concrete_flight_number):
    flight_number = concrete_flights[concrete_flight_number]["flight_number"]

    airplane_model = flights[flight_number]["airplane_model"]

    seats_in_row = len((airplane_models[airplane_model]["seats"]).split("|"))
    total_seats = int(airplane_models[airplane_model]["rows"]) * seats_in_row
    used_seats = 0
    for ticket, values in tickets.items():
        if tickets[ticket]["concrete_flight_number"] == concrete_flight_number:
            used_seats = used_seats + 1
    free_seats = total_seats - used_seats
    if free_seats > 0:
        return free_seats
    else:
        return False
def generate_ticket_number():
    max_ticket = 0
    for ticket in tickets.keys():
        if int(ticket)>max_ticket:
            max_ticket = int(ticket)
    max_ticket+=1
    return max_ticket

def print_by_dt_min_max(flights_copy, concrete_flights_copy, arrival_dt, arrival_dt_max):
    global concrete_flights_fields
    global flights_fields

    concrete_flights_print_header()
    # for flight_number, values in flights_copy.items():
    for concrete_flight_number, values in concrete_flights_copy.items():
        flight_number = values["flight_number"]
        if flight_number not in flights_copy:
            continue
        departure_date = concrete_flights_copy[concrete_flight_number]["departure_date"]
        departure_time = flights_copy[flight_number]["departure_time"]
        current_dt = datetime.datetime.strptime(
            departure_date + " " + departure_time,
            "%d.%m.%Y. %H:%M"
        )

        if arrival_dt < current_dt <= arrival_dt_max:
            print(
                f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^17} | {values[concrete_flights_fields[3]]:^15} ")

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
    flight_number = concrete_flights[concrete_flight_number]["flight_number"]

    departure_date = concrete_flights[concrete_flight_number]["departure_date"]
    departure_time = flights[flight_number]["departure_time"]

    departure_dt = datetime.datetime.strptime(
        departure_date + " " + departure_time,
        "%d.%m.%Y. %H:%M"
    )
    current_dt = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
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
        return True

    else:
        print("[ERROR] Check-out can only be done 48 hours before flight")
        return False

def get_taken_seats(ticket_number):

    concrete_flight_number = tickets[ticket_number]["concrete_flight_number"]

    taken_seats = set()           #skup

    for ticket, values in tickets.items():
        if values["concrete_flight_number"] == concrete_flight_number and values["seat"] != '':
            taken_seats.add(tickets[ticket_number]["seat"])

    return taken_seats

def print_taken_seats(taken_seats, ticket_number):
    concrete_flight_number = tickets[ticket_number]["concrete_flight_number"]

    flight_number = concrete_flights[concrete_flight_number]["flight_number"]

    airplane_model = flights[flight_number]["airplane_model"]

    rows = int(airplane_models[airplane_model]["rows"])

    seats = airplane_models[airplane_model]["seats"].split("|")

    for row in range(1, rows+1):
        print(f"row {row}: ", end="")

        for seat in seats:

            seat_code = f"{row}{seat}"

            if seat_code in taken_seats:
                print("X ", end="")
            else:
                print(f"{seat} ", end="")
        print()
    return rows


if __name__ == '__main__':
    load_all()
    # print(print_available_tickets_for_user())