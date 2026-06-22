from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load trained model and label encoder
model = joblib.load("models/best_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")


class ThreatInput(BaseModel):
    vendor_risk_score: int
    software_update_frequency: int
    known_vulnerabilities: int
    patch_delay_days: int
    third_party_access_level: int
    network_exposure_score: int
    past_incidents: int
    threat_actor_activity: int
    security_audit_score: int
    employee_security_training: int


@app.get("/")
def home():
    return {"message": "Cyber Threat Predictive Analytics API is running"}


@app.post("/predict")
def predict(data: ThreatInput):
    values = [[
        data.vendor_risk_score,
        data.software_update_frequency,
        data.known_vulnerabilities,
        data.patch_delay_days,
        data.third_party_access_level,
        data.network_exposure_score,
        data.past_incidents,
        data.threat_actor_activity,
        data.security_audit_score,
        data.employee_security_training
    ]]

    prediction = model.predict(values)[0]
    threat_level = label_encoder.inverse_transform([prediction])[0]

    return {"predicted_threat_level": threat_level}
