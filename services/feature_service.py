import pandas as pd

from services.lag_service import build_lag_features


def create_features(datetime_str: str):

    dt = pd.to_datetime(datetime_str)

    # Calendar features
    feature = {

    "temp_weighted":0,

    "hour":dt.hour,

    "minute":dt.minute,

    "dayofweek":dt.dayofweek,

    "month":dt.month

}

    # Add lag features
    feature.update(
        build_lag_features(dt)
    )

    return pd.DataFrame([feature])