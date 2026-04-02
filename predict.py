import pickle
from utils.features import extract_features

model = pickle.load(open("model/phishing_model.pkl", "rb"))

url = input("Enter URL: ")
features = extract_features(url)

prediction = model.predict([features])[0]

if prediction == 1:
    print("⚠️ Phishing Website")
else:
    print("✅ Safe Website")
