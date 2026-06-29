import pandas as pd
from datetime import timedelta

from services.state_service import (
    get_history_path,
    get_prediction_log_path
)

# Load historical data
history = pd.read_csv(get_history_path())
history["datetime"] = pd.to_datetime(history["datetime"])

# Load prediction log
prediction_log = pd.read_csv(get_prediction_log_path())

if not prediction_log.empty:
    prediction_log["datetime"] = pd.to_datetime(
        prediction_log["datetime"]
    )


def get_history():
    return history


def get_historical_value(target_datetime):
    """
    Returns the historical demand for the exact datetime.
    """

    row = history[history["datetime"] == target_datetime]

    if row.empty:
        return None

    return float(row.iloc[0]["hourly_demand_met_mw"])

def get_value(target_datetime):
    """
    Returns demand for a datetime.

    Priority:
    1. prediction_log.csv
    2. historical average
    """

    # -----------------------------
    # Check prediction log
    # -----------------------------
    if not prediction_log.empty:

        row = prediction_log[
            prediction_log["datetime"] == target_datetime
        ]

        if not row.empty:
            return float(row.iloc[0]["actual_demand"])

    # -----------------------------
    # Historical fallback
    # -----------------------------
    values = []

    for year in [2024, 2025]:

        try:
            historical_time = target_datetime.replace(year=year)

        except ValueError:
            continue

        row = history[
            history["datetime"] == historical_time
        ]

        if not row.empty:
            values.append(
                float(row.iloc[0]["hourly_demand_met_mw"])
            )

    if len(values) == 0:
        return None

    return sum(values) / len(values)

from datetime import timedelta


from datetime import timedelta
import pandas as pd


def build_lag_features(target_datetime):

    features = {}

    # --------------------------
    # Lag Features
    # --------------------------

    features["y_lag_1"] = get_value(
        target_datetime - timedelta(minutes=15)
    )

    features["y_lag_2"] = get_value(
        target_datetime - timedelta(minutes=30)
    )

    features["y_lag_4"] = get_value(
        target_datetime - timedelta(hours=1)
    )

    features["y_lag_24h"] = get_value(
        target_datetime - timedelta(days=1)
    )

    features["y_lag_96"] = get_value(
        target_datetime - timedelta(days=1)
    )

    features["y_lag_192"] = get_value(
        target_datetime - timedelta(days=2)
    )

    features["y_lag_7d"] = get_value(
        target_datetime - timedelta(days=7)
    )

    # --------------------------
    # Rolling Features
    # --------------------------

    last_4 = []

    for i in range(4):
        value = get_value(
            target_datetime - timedelta(minutes=15 * (i + 1))
        )
        last_4.append(value)

    features["rolling_mean_4"] = sum(last_4) / len(last_4)

    # --------------------------

    last_96 = []

    for i in range(96):
        value = get_value(
            target_datetime - timedelta(minutes=15 * (i + 1))
        )

        last_96.append(value)

    series = pd.Series(last_96)

    features["rolling_mean_96"] = series.mean()

    features["rolling_std_96"] = series.std()

    return features