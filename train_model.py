"""
Train ML models to predict cyber threat level in supply chain systems.
Models: Logistic Regression, Decision Tree, Random Forest, SVM
"""

import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "cyber_supply_chain_dataset.csv"
MODEL_DIR = ROOT / "models"
OUTPUT_DIR = ROOT / "outputs"
MODEL_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_PATH.exists():
    raise FileNotFoundError("Dataset not found. Run: python src/generate_dataset.py")

df = pd.read_csv(DATA_PATH)
X = df.drop("threat_level", axis=1)
y = df["threat_level"]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ]),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=120, random_state=42),
    "SVM": Pipeline([
        ("scaler", StandardScaler()),
        ("model", SVC(kernel="rbf", probability=True, random_state=42))
    ])
}

results = []
best_model_name = None
best_accuracy = 0
best_model = None

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    results.append({"Model": name, "Accuracy": round(accuracy, 4)})

    print("\n" + "=" * 60)
    print(name)
    print("Accuracy:", round(accuracy, 4))
    print(classification_report(y_test, predictions, target_names=encoder.classes_))
    print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model_name = name
        best_model = model

results_df = pd.DataFrame(results).sort_values(by="Accuracy", ascending=False)
results_df.to_csv(OUTPUT_DIR / "model_results.csv", index=False)

joblib.dump(best_model, MODEL_DIR / "best_model.pkl")
joblib.dump(encoder, MODEL_DIR / "label_encoder.pkl")

print("\nBest Model:", best_model_name)
print("Best Accuracy:", round(best_accuracy, 4))
print("Saved model to models/best_model.pkl")
