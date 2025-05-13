from fastapi import FastAPI
from ai_model import suggest_treatment

app = FastAPI()

@app.get("/predict")
async def predict(symptoms: str):
    result = suggest_treatment(symptoms)
    return result