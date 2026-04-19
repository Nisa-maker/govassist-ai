import random

def get_social(citizen_id):
    """
    Generate social assistance related data for a citizen
    """

    # simulate number of dependents (for ML feature)
    dependents = random.randint(0, 5)

    # simulate whether citizen currently receives aid
    receives_aid = random.choice([True, False])

    # simulate vulnerability status
    vulnerability_level = random.choice(["low", "medium", "high"])

    return {
        "dependents": dependents,
        "receives_aid": receives_aid,
        "vulnerability_level": vulnerability_level
    }