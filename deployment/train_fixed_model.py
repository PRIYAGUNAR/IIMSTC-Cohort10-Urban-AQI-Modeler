"""
Fixed XGBoost training script for PM2.5 prediction
"""
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from xgboost import XGBRegressor
import os

# Load data
print("Loading data...")
data = pd.read_csv("../cleaned_air_quality_data (1) (1).csv")

# Define features in correct order  
feature_names = [
    'PM10', 'SO2', 'NO2', 'CO', 'O3',
    'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM',
    'month', 'hour'
]

X = data[feature_names]
y = data['PM2.5']

print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
print(f"Features: {feature_names}")

# Split data
print("\nSplitting data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost
print("Training XGBoost model...")
xgb = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    random_state=42,
    verbosity=1
)

xgb.fit(X_train, y_train)

# Evaluate
print("\nEvaluating model...")
y_pred = xgb.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}")
print(f"MAE:  {mae:.2f}")
print(f"R²:   {r2:.4f}")

# Show sample predictions
print("\nSample predictions (Actual | Predicted):")
for i in range(10):
    print(f"{y_test.iloc[i]:6.2f} | {y_pred[i]:6.2f}")

# Save model
print("\nSaving model...")
model_path = os.path.join(os.path.dirname(__file__), "pm25_xgb_model.pkl")
joblib.dump(xgb, model_path)
print(f"Model saved to: {model_path}")

# Also save feature names for reference
joblib.dump(feature_names, "feature_names.pkl")
print("Feature names saved to: feature_names.pkl")
