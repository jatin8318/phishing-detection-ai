# 🔐 Phishing Detection System (AI-Based)

## 🚀 Overview
This project is an AI-based phishing detection system that analyzes URLs and predicts whether they are **safe or phishing** using machine learning.

It uses simple URL-based features such as:
- URL length
- HTTPS presence
- Number of dots

The system includes:
- Machine Learning model (Random Forest)
- Feature extraction module
- Web application (Flask)
- Real-time prediction

---

## 📂 Project Structure
phishing-detection-ai/
│
├── data/
│ └── dataset.csv
│
├── model/
│ ├── train_model.py
│ └── phishing_model.pkl
│
├── utils/
│ └── features.py
│
├── templates/
│ └── index.html
│
├── app.py
├── predict.py
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Installation

### 1. Clone the Repository

---

### 2. Install Dependencies
pip install -r requirements.txt

---

## 🧠 Train the Model

Run the following command to train the machine learning model:
python model/train_model.py
python model/train_model.py
model/phishing_model.pkl

---

## ▶️ Run the Application

Start the Flask web app:
python app.py
Open your browser and go to:
http://127.0.0.1:5000/

---

## 🔍 How It Works

1. User enters a URL  
2. System extracts features:
   - URL length
   - HTTPS usage
   - Number of dots  
3. Model predicts:
   - ✅ Safe Website  
   - ⚠️ Phishing Website  

---

## 🧪 Example Test

Try entering:

- Safe URL:

  
Columns:
- `url_length`
- `has_https`
- `dots`
- `label` (0 = safe, 1 = phishing)

---

## 🧰 Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- HTML/CSS

---


---

## 🎯 Future Improvements

- Add more features (domain age, IP detection)
- Integrate VirusTotal API
- Build Chrome extension
- Improve model accuracy with larger dataset

---

## 👨‍💻 Author

Your Name  
(Your GitHub Profile Link)

---

## 📜 License

This project is for educational purposes.
