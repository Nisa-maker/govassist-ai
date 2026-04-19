from backend.services.population import get_population
from backend.services.education import get_education
from backend.services.health import get_health
from backend.services.employment import get_employment
from backend.services.economy import get_economy
from backend.services.social import get_social_assistance

def get_citizen_data(citizen_id):
    return {
        "citizen_id": citizen_id,
        **get_population(citizen_id),
        **get_education(citizen_id),
        **get_health(citizen_id),
        **get_employment(citizen_id),
        **get_economy(citizen_id),
        **get_social(citizen_id),
    }