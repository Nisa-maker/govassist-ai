import os
import joblib

model = None

def get_model():
    global model
    if model is None:
        try:
            BASE_DIR = os.path.dirname(os.path.dirname(__file__))
            path = os.getenv("MODEL_PATH", os.path.join(BASE_DIR, "models", "model.pkl"))
            model = joblib.load(path)
        except Exception as e:
            print("Model load failed:", e)
            model = None
    return model