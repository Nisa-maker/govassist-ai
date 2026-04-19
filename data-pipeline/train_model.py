import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# =========================
# 1. Generate synthetic data
# =========================
data = []

for _ in range(500):
    income = random.randint(1, 10)
    dependents = random.randint(0, 5)
    house_condition = random.randint(1, 3)

    # simple rule for label (ground truth)
    eligible = 1 if (income < 5 and dependents >= 2) else 0

    data.append([income, dependents, house_condition, eligible])

df = pd.DataFrame(data, columns=[
    "income", "dependents", "house_condition", "eligible"
])

# =========================
# 2. Train model
# =========================
X = df[["income", "dependents", "house_condition"]]
y = df["eligible"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# =========================
# 3. Evaluate
# =========================
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# =========================
# 4. Save model
# =========================
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")

print("Model saved to models/model.pkl")