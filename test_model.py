import joblib

print("Loading model...")

model = joblib.load("models/xgb_model.pkl")

print("Loaded!")
print(type(model))
