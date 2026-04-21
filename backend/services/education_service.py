import random

education_levels = [
    "no_school",
    "incomplete_elementary",
    "elementary_school",
    "junior_high_school",
    "senior_high_school",
    "university"
]

def get_education(citizen_id: str):
    return {
        "education_level": random.choice(education_levels)
    }