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
    with open("csv_files/test.csv", "w", newline="", encoding="utf-8") as file:  # newline izbegava prazne redove
        writer = csv.DictWriter(file, fieldnames=users_fields)
        writer.writeheader()
        for username, values in users.items():
            row = {"username": username,
                   **values}  # **values koristimo zato sto prosledjujemo kao red samo JEDAN recnik a da
            writer.writerow(row)

    flights_fields = {
        "flight_number", "departure_airport", "arrival_airport", "departure_time", "arrival_time",
        "next_day_arrival", "airline", "days_of_flight", "airplane_model", "price"
    }
    with open("csv_files/flights.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=flights_fields)
        writer.writeheader()
        for flight_number, values in flights.items():
            row = {"flight_number":flight_number, **values}
            writer.writerow(row)

    concrete_flights_fields = {
        "concrete_flight_number", "flight_number", "departure_date", "arrival_date"
    }
    with open("csv_files/concrete_flights.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=concrete_flights_fields)
        for concrete_flight_number, values in concrete_flights.items():
            row = {"concrete_flight_number":concrete_flight_number, **values}
            writer.writerow(row)

    airports_fields = {
        "airport_code", "airport_name", "city", "country"
    }
    with open("csv_files/airports.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=airports_fields)
        for flight_number, values in airports.items():
            row = {"flight_number":flight_number, **values}
            writer.writerow(row)

    airplane_models_fields = {
        "model", "seat_count"
    }
    with open("csv_files/airplane_models.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=airplane_models_fields)
        for flight_number, values in airplane_models.items():
            row = {"flight_number":flight_number, **values}
            writer.writerow(row)

def available_flights():
    today= datetime.date.today()
    concrete_flights_fields = [
        "concrete_flight_number", "flight_number", "departure_date", "arrival_date"
    ]
    print()
    print(f"{concrete_flights_fields[0]:^15} | {concrete_flights_fields[1]:^15} | {concrete_flights_fields[2]:^15} | {concrete_flights_fields[3]:^15}")
    print("-" * 75)
    for concrete_flight_number, values in concrete_flights.items():                #uzima svaki datum
        departure_date = datetime.date.fromisoformat(concrete_flights[concrete_flight_number]["departure_date"])     #konvertuje string datuma u datum
        if departure_date >= today:
            print(f"{values[concrete_flights_fields[0]]:^22} | {values[concrete_flights_fields[1]]:^15} | {values[concrete_flights_fields[2]]:^15} | {values[concrete_flights_fields[3]]:^15}")

def search_by(parameter, value):
    for atribute in flights.values():
        if flights[parameter][value]== value:
            print(atribute)






