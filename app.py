from flask import Flask, render_template, request
import pickle
from utils.features import extract_features

app = Flask(__name__)
model = pickle.load(open("model/phishing_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        prediction = model.predict([features])[0]

        if prediction == 1:
            result = "⚠️ Phishing Website"
        else:
            result = "✅ Safe Website"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
