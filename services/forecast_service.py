import joblib
import pandas as pd

from services.state_service import get_model_path

# Load Sikkim model once
model = joblib.load(get_model_path())

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


def predict(feature_df: pd.DataFrame):

    X = feature_df[FEATURES]

    prediction = model.predict(X)[0]

    return float(prediction)