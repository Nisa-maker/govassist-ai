import random
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

education_map = {
    "no_school": 0,
    "incomplete_elementary": 1,
    "elementary_school": 2,
    "junior_high_school": 3,
    "senior_high_school": 4,
    "university": 5
}

# generate dummy dataset (realistic-ish)
data = []

for _ in range(1000):
    income = random.randint(0, 10)
    dependents = random.randint(0, 5)
    house = random.randint(1, 3)
    education = random.choice(list(education_map.keys()))

    edu_score = education_map[education]

    # logic eligibility (rule-based → jadi label ML)
    score = (income * 0.4) + (dependents * 0.3) + (house * 0.2) - (edu_score * 0.2)
    eligible = 1 if score < 5 else 0

    data.append([income, dependents, house, edu_score, eligible])

df = pd.DataFrame(data, columns=[
    "income", "dependents", "house_condition", "education", "eligible"
])

X = df.drop("eligible", axis=1)
y = df["eligible"]

model = RandomForestClassifier()
model.fit(X, y)

# save model
joblib.dump(model, "models/model.pkl")

print("Model trained & saved!")