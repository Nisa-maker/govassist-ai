import random

def get_economy(citizen_id):
    """
    Generate economic data for a citizen
    """

    # simulate monthly income (scaled 1–10 for ML)
    income = random.randint(1, 10)

    # simulate employment type
    employment_type = random.choice([
        "unemployed",
        "informal",
        "formal",
        "self-employed"
    ])

    # simulate asset ownership (simple proxy)
    has_vehicle = random.choice([True, False])
    has_house = random.choice([True, False])

    return {
        "income": income,
        "employment_type": employment_type,
        "has_vehicle": has_vehicle,
        "has_house": has_house
    }
