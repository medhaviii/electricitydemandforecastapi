from services.feature_service import create_features

df = create_features("2025-06-29 12:30:00")

print(df)
print(df.columns)