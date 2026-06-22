"""
Predict cyber threat level for a new supply chain vendor/system.
"""

import joblib
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "best_model.pkl"
ENCODER_PATH = ROOT / "models" / "label_encoder.pkl"

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

sample = pd.DataFrame([{
    "vendor_risk_score": 8,
    "software_update_frequency": 12,
    "known_vulnerabilities": 11,
    "patch_delay_days": 45,
    "third_party_access_level": 4,
    "network_exposure_score": 8,
    "past_incidents": 3,
    "threat_actor_activity": 7,
    "security_audit_score": 52,
    "employee_security_training": 0
}])

prediction = model.predict(sample)
threat_level = encoder.inverse_transform(prediction)[0]

print("Input Data:")
print(sample)
print("\nPredicted Cyber Threat Level:", threat_level)
