from services.population import get_population
from services.education import get_education
from services.health import get_health
from services.employment import get_employment
from backend.services.economy import get_economi
from services.social import get_social

def get_citizen_data(citizen_id):
    return {
        "citizen_id": citizen_id,
        **get_population(citizen_id),
        **get_education(citizen_id),
        **get_health(citizen_id),
        **get_employment(citizen_id),
        **get_economi(citizen_id),
        **get_social(citizen_id),
    }