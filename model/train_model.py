import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("data/dataset.csv")

X = df[['url_length', 'has_https', 'dots']]
y = df['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model/phishing_model.pkl", "wb"))

print("✅ Model trained successfully!")
