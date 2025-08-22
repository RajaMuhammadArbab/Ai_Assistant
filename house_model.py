import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
import os

# Create folder
os.makedirs("models", exist_ok=True)

# Generate dummy data
data = pd.DataFrame({
    'area': np.random.randint(500, 4000, 100),
    'rooms': np.random.randint(1, 6, 100),
    'loc_score': np.random.randint(1, 10, 100)
})
data['price'] = (
    data['area'] * 200 +
    data['rooms'] * 50000 +
    data['loc_score'] * 10000 +
    np.random.randint(-20000, 20000, 100)
)

# Train model
X = data[['area', 'rooms', 'loc_score']]
y = data['price']
model = LinearRegression().fit(X, y)

# Save model
joblib.dump(model, 'models/house_model.pkl')
print("✅ House model saved as models/house_model.pkl")
