import joblib

# load ML model
model = joblib.load("models/model.pkl")

# mapping education → numeric (biar cocok sama ML)
education_map = {
    "no_school": 0,
    "incomplete_elementary": 1,
    "elementary_school": 2,
    "junior_high_school": 3,
    "senior_high_school": 4,
    "university": 5
}


def get_social_assistance(income, dependents, house_condition, education_level, health):
    """
    Determine eligibility for social assistance using ML + rules
    """

    # convert education ke angka
    edu = education_map.get(education_level, 2)

    # input ke model
    X = [[income, dependents, house_condition, edu]]
    pred = model.predict(X)[0]

    # =========================
    # HEALTH PRIORITY
    # =========================
    health_priority = 1 if health["risk_level"] == "high" else 0

    # override kalau sakit berat
    if health_priority == 1:
        pred = 1

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

    if health["risk_level"] == "high":
        reasons.append("High health risk")

    # =========================
    # OUTPUT
    # =========================
    return {
        "eligible": int(pred),
        "health_priority": health_priority,
        "reasons": reasons
    }