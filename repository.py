import csv
import datetime

users = {}
flights = {}
concrete_flights = {}
airports = {}
airplane_models = {}



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

if __name__=="__main__":
 pass


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

def available_flights():
    today= datetime.date.today()
    concrete_flights_fields = [
        "concrete_flight_number","flight_number", "departure_airport", "arrival_airport", "departure_date", "arrival_date",
        "departure_time", "arrival_time", "next_day_arrival", "airline", "airplane_model", "price"
    ]
    print()
    print(f"{concrete_flights_fields[0]:^15} | {concrete_flights_fields[1]:^15} | {concrete_flights_fields[2]:^15} | {concrete_flights_fields[3]:^15} | {concrete_flights_fields[4]:^15} | {concrete_flights_fields[5]:^15} | {concrete_flights_fields[6]:^15} | {concrete_flights_fields[7]:^15} | {concrete_flights_fields[8]:^15} | {concrete_flights_fields[9]:^24} | {concrete_flights_fields[10]:^15} | {concrete_flights_fields[11]:^15}")
    print("-" * 230)
    for concrete_flight_number, values in concrete_flights.items():                #uzima svaki datum
        departure_date = datetime.date.fromisoformat(concrete_flights[concrete_flight_number]["departure_date"])     #konvertuje string datuma u datum
        if departure_date >= today:
            print(f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^17} | {values[concrete_flights_fields[3]]:^15} | {values[concrete_flights_fields[4]]:^15} | {values[concrete_flights_fields[5]]:^15} | {values[concrete_flights_fields[6]]:^15} | {values[concrete_flights_fields[7]]:^15} | {values[concrete_flights_fields[8]]:^16} | {values[concrete_flights_fields[9]]:^24} | {values[concrete_flights_fields[10]]:^15} | {values[concrete_flights_fields[11]]:^15}")

def search_by(parameter, value):s
    flights_fields = [
        "flight_number", "departure_airport", "arrival_airport", "departure_date", "arrival_date",
        "departure_time", "arrival_time", "next_day_arrival", "airline", "days_of_flight", "airplane_model", "price"
    ]
    print()
    print(f"{flights_fields[0]:^15} | {flights_fields[1]:^15} | {flights_fields[2]:^15} | {flights_fields[3]:^15} | {flights_fields[4]:^15} | {flights_fields[5]:^15} | {flights_fields[6]:^15} | {flights_fields[7]:^15} | {flights_fields[8]:^23} | {flights_fields[9]:^15} | {flights_fields[10]:^15} | {flights_fields[11]:^15} ")
    print("-" * 220)

    for flight_number, values in flights.items():
            if flights[flight_number][parameter]== value:
                print(f"{values[flights_fields[0]]:^15} | {values[flights_fields[1]]:^17} | {values[flights_fields[2]]:^15} | {values[flights_fields[3]]:^15} | {values[flights_fields[4]]:^15} | {values[flights_fields[5]]:^15} | {values[flights_fields[6]]:^15} | {values[flights_fields[7]]:^16} | {values[flights_fields[8]]:^23} | {values[flights_fields[9]]:^15} | {values[flights_fields[10]]:^15} | {values[flights_fields[11]]:^15}")


def search_by_multiple(flights_copy, parameter, value):         #prosledjujem recnik zato sto nije dobro brisati kljuc u recniku dok se iterira kroz njega. dodje do greske
    for flight_number in list(flights_copy.keys()):             #gledamo recnik kao listu
        if flights_copy[flight_number][parameter] != value:
            del flights_copy[flight_number]

def print_search_by_multiple(flights_copy):
    flights_fields = [
        "flight_number", "departure_airport", "arrival_airport", "departure_date", "arrival_date",
        "departure_time", "arrival_time", "next_day_arrival", "airline", "days_of_flight", "airplane_model", "price"
    ]
    print()
    print(f"{flights_fields[0]:^15} | {flights_fields[1]:^15} | {flights_fields[2]:^15} | {flights_fields[3]:^15} | {flights_fields[4]:^15} | {flights_fields[5]:^15} | {flights_fields[6]:^15} | {flights_fields[7]:^15} | {flights_fields[8]:^23} | {flights_fields[9]:^15} | {flights_fields[10]:^15} | {flights_fields[11]:^15} ")
    print("-" * 220)
    for flight_number, values in flights_copy.items():
        print(f"{values[flights_fields[0]]:^15} | {values[flights_fields[1]]:^17} | {values[flights_fields[2]]:^15} | {values[flights_fields[3]]:^15} | {values[flights_fields[4]]:^15} | {values[flights_fields[5]]:^15} | {values[flights_fields[6]]:^15} | {values[flights_fields[7]]:^16} | {values[flights_fields[8]]:^23} | {values[flights_fields[9]]:^15} | {values[flights_fields[10]]:^15} | {values[flights_fields[11]]:^15}")


def print_ten_cheapest_flights(flights_copy):
    flights_fields = [
        "flight_number", "departure_airport", "arrival_airport", "departure_date", "arrival_date",
        "departure_time", "arrival_time", "next_day_arrival", "airline", "days_of_flight", "airplane_model", "price"
    ]
    sorted_flights = dict(                          # sortiramo recnik preko liste pa vracamo u recnik zato sto ne moze da se sortira direktno recnik
        sorted(
            flights_copy.items(),
            key=lambda item: int(item[1]["price"])  # item = ("JU01", {"price": "120"}) lambda se koristi kako bi usli u vrednosti recnika, da ga nema sortirali bi samo po nazivima a ne po vrednostima(ceni)
        )[:10]
    )
    cheapest_sorted_flights = dict(
        sorted(
            sorted_flights.items(),
            key=lambda item: int(item[1]["price"])
        )
    )
    print()
    print(f"{flights_fields[0]:^15} | {flights_fields[1]:^15} | {flights_fields[2]:^15} | {flights_fields[3]:^15} | {flights_fields[4]:^15} | {flights_fields[5]:^15} | {flights_fields[6]:^15} | {flights_fields[7]:^15} | {flights_fields[8]:^23} | {flights_fields[9]:^15} | {flights_fields[10]:^15} | {flights_fields[11]:^15} ")
    print("-" * 220)
    for flight_number, values in cheapest_sorted_flights.items():
        print(f"{values[flights_fields[0]]:^15} | {values[flights_fields[1]]:^17} | {values[flights_fields[2]]:^15} | {values[flights_fields[3]]:^15} | {values[flights_fields[4]]:^15} | {values[flights_fields[5]]:^15} | {values[flights_fields[6]]:^15} | {values[flights_fields[7]]:^16} | {values[flights_fields[8]]:^23} | {values[flights_fields[9]]:^15} | {values[flights_fields[10]]:^15} | {values[flights_fields[11]]:^15}")

def print_flights_by_search_date(flights_copy, date, days):
    date_min= datetime.date-days
    print(date_min)