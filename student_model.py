import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Create folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Dummy training data
data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "attendance": [60, 65, 70, 75, 80, 85, 90, 95, 100],
    "score": [55, 60, 65, 70, 75, 80, 85, 90, 95]
}
df = pd.DataFrame(data)

# Train model
X = df[["hours", "attendance"]]
y = df["score"]

model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "models/student_model.pkl")
print("✅ Student model saved as models/student_model.pkl")
