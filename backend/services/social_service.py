def get_social_assistance(income, dependents, house_condition, education_level, health, model):
    """
    Determine eligibility using ML + rule-based explanation
    """

    # =========================
    # EDUCATION MAPPING
    # =========================
    education_map = {
        "no_school": 0,
        "incomplete_elementary": 1,
        "elementary_school": 2,
        "junior_high_school": 3,
        "senior_high_school": 4,
        "university": 5
    }

    edu = education_map.get(education_level, 2)

    # =========================
    # ML PREDICTION
    # =========================
    X = [[income, dependents, house_condition, edu]]
    pred = model.predict(X)[0]

    # =========================
    # HEALTH PRIORITY
    # =========================
    health_priority = 1 if not health["is_healthy"] else 0

    if health_priority == 1:
        pred = 1  # override kalau sakit

    # =========================
    # EXPLAINABLE AI (REASONS)
    # =========================
    reasons = []

    if income < 3:
        reasons.append("Low income")

    if dependents >= 3:
        reasons.append("Many dependents")

    if house_condition == 3:
        reasons.append("Poor housing")

    if education_level in ["no_school", "incomplete_elementary"]:
        reasons.append("Low education")

    if not health["is_healthy"]:
        reasons.append("Health issues")

    # =========================
    # OUTPUT
    # =========================
    return {
        "eligible": int(pred),
        "health_priority": health_priority,
        "reasons": reasons
    }