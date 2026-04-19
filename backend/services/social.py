def get_social_assistance(income, dependents, house_condition, education_level, health, model):
    
    education_map = {
        "no_school": 0,
        "incomplete_elementary": 1,
        "elementary_school": 2,
        "junior_high_school": 3,
        "senior_high_school": 4,
        "university": 5
    }

    edu = education_map.get(education_level, 2)

    X = [[income, dependents, house_condition, edu]]
    pred = model.predict(X)[0]

    health_priority = 1 if health["risk_level"] == "high" else 0
    if health_priority == 1:
        pred = 1

    return {
        "eligible": int(pred),
        "health_priority": health_priority
    }