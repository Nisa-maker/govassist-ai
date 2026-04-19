from fastapi import FastAPI
import random

# import all services
from backend.services.citizen import get_citizen_data
from backend.services.education import get_education
from backend.services.health import get_health
from backend.services.employment import get_employment
from backend.services.ekonomi import get_economy
from backend.services.social import get_social_assistance

app = FastAPI(title="GovAssist AI - Integrated System")


@app.get("/")
def home():
    return {"message": "GovAssist AI running 🚀"}


@app.get("/citizen/{citizen_id}")
def get_full_profile(citizen_id: str):

    # =========================
    # CORE DATA
    # =========================
    citizen = get_citizen_data(citizen_id)

    # =========================
    # SERVICES
    # =========================
    education = get_education(citizen_id)
    health = get_health(citizen_id)
    employment = get_employment(citizen_id)

    # =========================
    # DERIVED DATA
    # =========================
    economy = get_economy(citizen_id, employment["income"])

    # dependents & house (sementara random)
    dependents = random.randint(0, 5)
    house_condition = random.randint(1, 3)

    # =========================
    # AI DECISION (SOCIAL)
    # =========================
    social = get_social_assistance(
        income=employment["income"],
        dependents=dependents,
        house_condition=house_condition,
        education_level=education["education_level"],
        health=health
    )

    # =========================
    # FINAL RESPONSE
    # =========================
    return {
        "citizen": citizen,
        "education": education,
        "health": health,
        "employment": employment,
        "economy": economy,
        "house_condition": house_condition,
        "dependents": dependents,
        "social_assistance": social
    }