from fastapi import FastAPI
import joblib
import pandas as pd
from pathlib import Path

app=FastAPI()

model_path=Path(__file__).resolve().parent.parent/"models"/"churn_model.pkl"
model=joblib.load(model_path)

@app.get("/")
def home():
    return {"message": "Churn prediction API running"}

@app.post("/predict")
def predict(data:dict):
    df=pd.DataFrame([data])

    prediction=model.predict(df)[0]
    probability=model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }