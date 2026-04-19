import random

random.seed(42)

# list nama dummy
first_names = ["Anisa", "Budi", "Andi", "Rina", "Dewi", "Agus", "Putri", "Rizky"]
last_names = ["Santoso", "Wijaya", "Saputra", "Lestari", "Pratama", "Hidayat"]

cities = ["Bandung", "Jakarta", "Surabaya", "Yogyakarta", "Medan"]
marital_statuses = ["single", "married"]


# automatic generate 100 population
citizens_db = {}

for i in range(1, 101):
    citizen_id = f"ID{i:03d}"

    citizens_db[citizen_id] = {
        "name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "age": random.randint(18, 70),
        "gender": random.choice(["male", "female"]),
        "address": random.choice(cities),
        "marital_status": random.choice(marital_statuses)
    }


def get_population(citizen_id):
    return citizens_db.get(citizen_id, {
        "name": "Unknown",
        "age": 0,
        "gender": "unknown",
        "address": "unknown",
        "marital_status": "unknown"
    })