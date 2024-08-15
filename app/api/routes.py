from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.model import ForecastModel
from app.utils.preprocess import preprocess_input

router = APIRouter()

model = ForecastModel(model_path="notebooks/model.pkl")

class PredictionInput(BaseModel):
    date: str
    store: int
    item: int

@router.post("/predict")
def predict(input_data: PredictionInput):
    try:
        features = preprocess_input(input_data)
        prediction = model.predict(features)
        return {"sales": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/status")
def status():
    return {"status": "API is running"}
