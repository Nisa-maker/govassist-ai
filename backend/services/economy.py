import random

def get_economy(citizen_id: str, income: int):
    """
    Generate economic profile based on employment income
    """

    # classify income
    if income < 3:
        income_level = "low"
    elif income < 7:
        income_level = "middle"
    else:
        income_level = "high"

    return {
        "income": income,
        "income_level": income_level
    }
