from fastapi import FastAPI
import random
import os
import joblib

# =========================
# LOAD MODEL (SAFE PATH)
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "models", "model.pkl")

model = joblib.load(model_path)

# =========================
# IMPORT SERVICES
# =========================
from backend.services.citizen import get_citizen_data
from backend.services.education import get_education
from backend.services.health import get_health
from backend.services.employment import get_employment
from backend.services.economy import get_economy   # ⚠️ pastikan namanya economy.py
from backend.services.social import get_social_assistance

# =========================
# APP INIT
# =========================
app = FastAPI(title="GovAssist AI - Integrated Government System")


# =========================
# HOME
# =========================
@app.get("/")
def home():
    return {"message": "GovAssist AI running 🚀"}


# =========================
# FULL PROFILE ENDPOINT
# =========================
@app.get("/citizen/{citizen_id}")
def get_full_profile(citizen_id: str):

    # -------------------------
    # CORE DATA
    # -------------------------
    citizen = get_citizen_data(citizen_id)

    # -------------------------
    # SERVICES
    # -------------------------
    education = get_education(citizen_id)
    health = get_health(citizen_id)
    employment = get_employment(citizen_id)

    # -------------------------
    # DERIVED DATA
    # -------------------------
    economy = get_economy(citizen_id, employment["income"])

    dependents = random.randint(0, 5)
    house_condition = random.randint(1, 3)

    # -------------------------
    # AI DECISION
    # -------------------------
    social = get_social_assistance(
        income=employment["income"],
        dependents=dependents,
        house_condition=house_condition,
        education_level=education["education_level"],
        health=health,
        model=model   # 🔥 penting
    )

    # -------------------------
    # RESPONSE
    # -------------------------
    return {
        "citizen": citizen,
        "education": education,
        "health": health,
        "employment": employment,
        "economy": economy,
        "dependents": dependents,
        "house_condition": house_condition,
        "social_assistance": social
    }