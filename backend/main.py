from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import random
import os
import joblib

# =========================
# APP INIT
# =========================
app = FastAPI(title="GovAssist AI - Integrated Government System")

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# SAFE MODEL LOADING (LAZY)
# =========================
model = None

def get_model():
    global model
    if model is None:
        try:
            BASE_DIR = os.path.dirname(__file__)
            model_path = os.getenv("MODEL_PATH", os.path.join(BASE_DIR, "models", "model.pkl"))
            model = joblib.load(model_path)
        except Exception as e:
            print("Model load failed:", e)
            model = None
    return model

# =========================
# IMPORT SERVICES
# =========================
from backend.services.citizen import get_citizen_data
from backend.services.education import get_education
from backend.services.health import get_health
from backend.services.employment import get_employment
from backend.services.economy import get_economy
from backend.services.social import get_social_assistance

# =========================
# HOME
# =========================
@app.get("/")
def home():
    return {"status": "OK 🚀"}

# =========================
# DETAIL CITIZEN
# =========================
@app.get("/citizen/{citizen_id}")
def full_system(citizen_id: str):

    try:
        citizen = get_citizen_data(citizen_id)
        education = get_education(citizen_id)
        health = get_health(citizen_id)
        employment = get_employment(citizen_id)

        economy = get_economy(citizen_id, employment["income"])

        dependents = random.randint(0, 5)
        house_condition = random.randint(1, 3)

        model = get_model()

        try:
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

# =========================
# RANKING LOGIC
# =========================
def rank_citizens(min_score=0, city=None):

    results = []
    model = get_model()  # ⬅️ FIX: jangan load berulang di loop

    for i in range(1, 101):
        citizen_id = f"ID{i:03d}"

        try:
            citizen = get_citizen_data(citizen_id)
            education = get_education(citizen_id)
            health = get_health(citizen_id)
            employment = get_employment(citizen_id)

            dependents = random.randint(0, 5)
            house_condition = random.randint(1, 3)

            social = get_social_assistance(
                income=employment["income"],
                dependents=dependents,
                house_condition=house_condition,
                education_level=education["education_level"],
                health=health,
                model=model
            )

            # FILTER CITY (case-insensitive)
            if city and citizen.get("address", "").lower() != city.lower():
                continue

            # =========================
            # SCORING SYSTEM 🔥
            # =========================
            score = 0

            if social.get("eligible") == 1:
                score += 3

            if social.get("health_priority") == 1:
                score += 2

            score += (5 - employment["income"])
            score += dependents

            results.append({
                "citizen_id": citizen_id,
                "name": citizen.get("name"),
                "income": employment["income"],
                "dependents": dependents,
                "score": score,
                "eligible": social.get("eligible", 0),
                "health_priority": social.get("health_priority", 0),
                "reasons": social.get("reasons", [])
            })

        except Exception as e:
            continue

    # SORT
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    # FILTER MIN SCORE
    results = [r for r in results if r["score"] >= min_score]

    return results[:20]

# =========================
# RANK ENDPOINT
# =========================
@app.get("/rank")
def get_rank(
    min_score: int = Query(0),
    city: str = Query(None)
):
    return rank_citizens(min_score, city)