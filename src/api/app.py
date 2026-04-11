from fastapi import FastAPI
import joblib

app = FastAPI()

# Load models
traffic_model = joblib.load("src/models/traffic_model.pkl")
risk_model = joblib.load("src/models/risk_model.pkl")

@app.get("/")
def home():
    return {"message": "Traffic Intelligence API Running 🚀"}

@app.post("/predict")
def predict(data: dict):

    features = data["features"]

    traffic_pred = traffic_model.predict([features])[0]
    risk_pred = risk_model.predict([features[:3]])[0]

    return {
        "traffic_prediction": float(traffic_pred),
        "risk_level": int(risk_pred)
    }