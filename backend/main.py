from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

from backend.crop_stress import predict_stress
from backend.chatbot import chatbot_response
from backend.explain import explain_prediction


app = FastAPI(title="AgriMind+ Crop Stress Early-Warning System")

# Add CORS settings to allow frontend requests
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SensorData(BaseModel):
    ph: float
    moisture: float
    temperature: float
    weather_forecast: Optional[str] = None  # e.g., "rainy", "sunny"
    image_url: Optional[str] = None

class ChatQuery(BaseModel):
    question: str
    language: Optional[str] = "en"

@app.get("/")
def root():
    return {"message": "Welcome to AgriMind+ API"}

@app.post("/api/predict_stress")
def get_stress_prediction(data: SensorData):
    try:
        prediction, csi = predict_stress(data)
        explanation = explain_prediction(data, csi)
        return {"stress_risk": prediction, "crop_stress_index": csi, "explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chatbot")
def ask_chatbot(query: ChatQuery):
    try:
        response = chatbot_response(query.question, query.language)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
