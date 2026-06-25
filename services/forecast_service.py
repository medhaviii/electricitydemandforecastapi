import joblib
import pandas as pd

# Load model once when the server starts
model = joblib.load("models/xgb_model.pkl")

# Exact feature order used during training
FEATURES = [
    "temp_weighted",
    "hour",
    "minute",
    "dayofweek",
    "month",
    "y_lag_1",
    "y_lag_2",
    "y_lag_4",
    "y_lag_24h",
    "y_lag_96",
    "y_lag_192",
    "y_lag_7d",
    "rolling_mean_4",
    "rolling_mean_96",
    "rolling_std_96"
]


def predict(feature_df: pd.DataFrame) -> float:
    """
    Predict demand from a dataframe containing one row
    of features.
    """

    X = feature_df[FEATURES]

    prediction = model.predict(X)[0]

    return float(prediction)