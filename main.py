from fastapi import FastAPI, HTTPException
from schemas import InputData, PredictionResult
import model_loader

app = FastAPI(title="API Datamine")

@app.get("/")
def read_root():
    return {"message": "API de predicción funcionando"}

@app.post("/predict", response_model=PredictionResult)
def predict(data: InputData):
    try:
        # Convertimos los datos del esquema en la lista que espera nuestro "modelo"
        features = [data.feature1, data.feature2, data.feature3]
        
        # Llamamos a la lógica que definimos en model_loader.py
        prediction = model_loader.predict_dummy(features)
        
        return {"prediction": prediction, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
