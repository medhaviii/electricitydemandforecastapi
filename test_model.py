from services.feature_service import create_features
from services.forecast_service import predict

df = create_features("2025-06-29 12:30:00")

print("Features:")
print(df)

prediction = predict(df)

print("\nPrediction:")
print(prediction)