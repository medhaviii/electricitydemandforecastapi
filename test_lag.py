from services.lag_service import get_historical_value
import pandas as pd

dt = pd.Timestamp("2024-01-08 00:15:00")

print(get_historical_value(dt))