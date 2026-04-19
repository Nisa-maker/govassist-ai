import random

def get_health(citizen_id: str):
    """
    Generate basic health profile
    """

    has_insurance = random.choices(
        [True, False],
        weights=[0.7, 0.3]  # majority has health insurrance
    )[0]

    diseases = ["none", "diabetes", "hypertension", "asthma"]

    disease = random.choices(
        diseases,
        weights=[0.6, 0.15, 0.15, 0.1]
    )[0]

    return {
        "has_insurance": has_insurance,
        "disease": disease,
        "is_healthy": disease == "none"
    }