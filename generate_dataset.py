"""
Synthetic Cyber Supply Chain Threat Dataset Generator
Creates a sample dataset for predictive analytics in cyber supply chain systems.
"""

import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)

n = 1000

data = pd.DataFrame({
    "vendor_risk_score": np.random.randint(1, 11, n),
    "software_update_frequency": np.random.randint(1, 31, n),
    "known_vulnerabilities": np.random.randint(0, 20, n),
    "patch_delay_days": np.random.randint(0, 90, n),
    "third_party_access_level": np.random.randint(1, 6, n),
    "network_exposure_score": np.random.randint(1, 11, n),
    "past_incidents": np.random.randint(0, 8, n),
    "threat_actor_activity": np.random.randint(1, 11, n),
    "security_audit_score": np.random.randint(1, 101, n),
    "employee_security_training": np.random.randint(0, 2, n),
})

risk = (
    data["vendor_risk_score"] * 0.20
    + data["known_vulnerabilities"] * 0.18
    + data["patch_delay_days"] * 0.05
    + data["third_party_access_level"] * 0.35
    + data["network_exposure_score"] * 0.22
    + data["past_incidents"] * 0.30
    + data["threat_actor_activity"] * 0.25
    - data["security_audit_score"] * 0.04
    - data["employee_security_training"] * 1.2
)

data["threat_level"] = np.where(risk > 7.5, "High", np.where(risk > 4.5, "Medium", "Low"))

output_path = DATA_DIR / "cyber_supply_chain_dataset.csv"
data.to_csv(output_path, index=False)
print(f"Dataset created at: {output_path}")
print(data.head())
