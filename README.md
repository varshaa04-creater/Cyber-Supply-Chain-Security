# Cyber Threat Predictive Analytics for Protecting Cyber Supply Chain Systems

This project uses Python and Machine Learning to predict cyber threat levels in a cyber supply chain system. It helps identify whether a vendor, software component, or third-party service has **Low**, **Medium**, or **High** cyber risk.

## Project Objective

Cyber supply chains are vulnerable because organizations depend on third-party vendors, software updates, cloud services, and external integrations. A weakness in one vendor can affect the entire system.

This project predicts cyber threat levels using risk factors such as vendor risk, known vulnerabilities, patch delay, network exposure, third-party access, past incidents, threat actor activity, audit score, and employee security training.

## Features

- Synthetic cyber supply chain dataset generation
- Threat level prediction: Low, Medium, High
- Machine Learning model comparison
- Algorithms used:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Support Vector Machine
- Best model saved automatically
- Prediction script for new vendor/system risk
- GitHub-ready project structure

## Project Structure

```text
cyber-threat-predictive-analytics/
│
├── data/
│   └── cyber_supply_chain_dataset.csv
│
├── models/
│   ├── best_model.pkl
│   └── label_encoder.pkl
│
├── outputs/
│   └── model_results.csv
│
├── src/
│   ├── generate_dataset.py
│   ├── train_model.py
│   └── predict_threat.py
│
├── notebooks/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset Features

| Feature | Description |
|---|---|
| vendor_risk_score | Risk score of vendor from 1 to 10 |
| software_update_frequency | Number of days between software updates |
| known_vulnerabilities | Number of known vulnerabilities |
| patch_delay_days | Delay in applying security patches |
| third_party_access_level | External access level from 1 to 5 |
| network_exposure_score | Internet/network exposure score |
| past_incidents | Previous security incidents |
| threat_actor_activity | Threat actor activity level |
| security_audit_score | Security audit score out of 100 |
| employee_security_training | 1 if trained, 0 if not trained |
| threat_level | Target value: Low, Medium, High |

## How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cyber-threat-predictive-analytics.git
cd cyber-threat-predictive-analytics
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate dataset

```bash
python src/generate_dataset.py
```

### 4. Train ML models

```bash
python src/train_model.py
```

### 5. Predict threat level for a sample vendor/system

```bash
python src/predict_threat.py
```

## Sample Output

```text
Best Model: Random Forest
Best Accuracy: 0.98
Predicted Cyber Threat Level: High
```

Accuracy may change slightly depending on the generated data and model training.

## Machine Learning Workflow

1. Collect cyber supply chain risk data
2. Preprocess the dataset
3. Split data into training and testing sets
4. Train multiple ML models
5. Compare model accuracy
6. Save the best model
7. Predict threat level for new data

## Real-World Use Case

This project can help organizations identify high-risk vendors or software components before they cause security incidents. It can support cyber supply chain risk management, vendor assessment, vulnerability prioritization, and early threat detection.

## Future Enhancements

- Use real cyber threat intelligence datasets
- Add IoC-based threat detection
- Build a Streamlit dashboard
- Add email or WhatsApp alerts for high-risk vendors
- Integrate with SIEM tools
- Add explainable AI using SHAP or LIME

## Author

**Varshaa Valaboju**  
B.Tech Computer Science and Design  
GitHub: https://github.com/varshaa04-creater
