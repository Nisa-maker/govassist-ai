from fastapi import FastAPI
import random

# =========================
# SAFE MODEL LOADING (LAZY)
# =========================
model = None

def get_model():
    global model
    if model is None:
        import os
        import joblib
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        model_path = os.path.join(BASE_DIR, "models", "model.pkl")
        model = joblib.load(model_path)
    return model


# =========================
# IMPORT SERVICES
# =========================
from backend.services.citizen import get_citizen_data
from backend.services.education import get_education
from backend.services.health import get_health
from backend.services.employment import get_employment
from backend.services.economy import get_economy   # pastikan economy.py
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
    return {"status": "OK 🚀"}


# =========================
# FULL SYSTEM ENDPOINT
# =========================
@app.get("/citizen/{citizen_id}")
def full_system(citizen_id: str):

    try:
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
        # DERIVED
        # -------------------------
        economy = get_economy(citizen_id, employment["income"])

        dependents = random.randint(0, 5)
        house_condition = random.randint(1, 3)

        # -------------------------
        # ML (SAFE)
        # -------------------------
        try:
            model = get_model()

            social = get_social_assistance(
                income=employment["income"],
                dependents=dependents,
                house_condition=house_condition,
                education_level=education["education_level"],
                health=health,
                model=model
            )

        except Exception as e:
            social = {
                "error": "ML failed",
                "detail": str(e)
            }

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

    except Exception as e:
        return {
            "error": "SYSTEM FAILED",
            "detail": str(e)
        }