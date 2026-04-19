from fastapi import FastAPI
from pydantic import BaseModel

import joblib

model = joblib.load("models/model.pkl")

# import unified citizen service
from backend.services.citizen import get_citizen_data

app = FastAPI(title="GovAssist AI - Integrated Government System")

# =========================
# HOME
# =========================
@app.get("/")
def home():
    return {"message": "GovAssist AI is running 🚀"}


# =========================
# REQUEST MODELS
# =========================

# for citizen-based system (e-Devlet style)
class CitizenRequest(BaseModel):
    citizen_id: str


# for manual prediction (optional)
class PredictionInput(BaseModel):
    income: float
    dependents: int
    house_condition: int


# =========================
# CITIZEN DATA (CORE SYSTEM)
# =========================
@app.post("/citizen")
def get_citizen(request: CitizenRequest):
    """
    Retrieve integrated citizen data across multiple sectors
    (population, education, health, employment, economy, social)
    """
    return get_citizen_data(request.citizen_id)


# =========================
# AI DECISION (AUTO - BY ID)
# =========================
@app.post("/predict/citizen")
def predict_by_citizen(request: CitizenRequest):
    """
    Predict eligibility using integrated citizen data
    (no manual input needed)
    """
    data = get_citizen_data(request.citizen_id)

    # extract features 
    income = data.get("income", 0)
    dependents = data.get("dependents", 1)
    house_condition = data.get("house_condition", 2)

    # simple scoring logic 
    score = income * 0.3 + dependents * 0.5 + house_condition * 0.2

    eligible = 1 if score < 5 else 0

    return {
        "citizen_id": request.citizen_id,
        "eligible": eligible,
        "score": score,
        "data_used": {
            "income": income,
            "dependents": dependents,
            "house_condition": house_condition
        },
        "note": "Decision based on integrated citizen data"
    }


# =========================
# AI DECISION (MANUAL INPUT)
# =========================
@app.post("/predict/manual")
def predict_manual(data: PredictionInput):
    """
    Predict eligibility using manual input
    (for testing / comparison)
    """
    score = (
        data.income * 0.3 +
        data.dependents * 0.5 +
        data.house_condition * 0.2
    )

    eligible = 1 if score < 5 else 0

    return {
        "eligible": eligible,
        "score": score,
        "note": "Manual input prediction"
    }