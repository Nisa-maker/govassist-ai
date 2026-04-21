from fastapi import APIRouter
import random

from backend.routers.citizen import get_citizen_data
from backend.services.education import get_education
from backend.services.health import get_health
from backend.services.employment import get_employment
from backend.services.economy import get_economy
from backend.services.social import get_social_assistance
from backend.core.model_loader import get_model

router = APIRouter()

@router.get("/citizen/{citizen_id}")
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