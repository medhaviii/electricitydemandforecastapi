from fastapi import FastAPI
import pandas as pd

from schemas.request_schema import PredictionRequest
from services.forecast_service import predict

app = FastAPI(
    title="NTPC Demand Forecast API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "NTPC Demand Forecast API is running"
    }


@app.post("/predict")
def forecast(req: PredictionRequest):

    # Dummy feature values for testing
    feature_df = pd.DataFrame([{
        "temp_weighted": 35.0,
        "hour": 14,
        "minute": 30,
        "dayofweek": 3,
        "month": 6,
        "y_lag_1": 6000,
        "y_lag_2": 5995,
        "y_lag_4": 5985,
        "y_lag_24h": 5940,
        "y_lag_96": 5900,
        "y_lag_192": 5850,
        "y_lag_7d": 5800,
        "rolling_mean_4": 5990,
        "rolling_mean_96": 5925,
        "rolling_std_96": 32
    }])

    prediction = predict(feature_df)

    return {
        "requested_datetime": req.datetime,
        "predicted_demand": prediction
    }