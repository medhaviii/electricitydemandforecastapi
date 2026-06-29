from fastapi import FastAPI

from schemas.request_schema import PredictionRequest
from services.forecast_service import predict
from services.feature_service import create_features

app = FastAPI(
    title="Demand Forecast API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Demand Forecast API is running"
    }


@app.post("/predict")
def forecast(req: PredictionRequest):

    feature_df = create_features(req.datetime)

    prediction = predict(feature_df)

    return {
        "state": req.state,
        "datetime": req.datetime,
        "prediction": prediction
    }