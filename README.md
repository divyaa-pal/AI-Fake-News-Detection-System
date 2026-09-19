📰 Fake News Detection App

👩‍💻 Developer: Divya Pal


«An AI/ML application that predicts whether a news article is Real or Fake using NLP and Machine Learning.»

✨ Features

- 📰 Real/Fake news prediction
- 🤖 Machine Learning classification
- 🔤 NLP-based text processing
- 💻 Streamlit interface
- ⚡ Instant local prediction

🛠️ Technologies

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

📊 Dataset

File: "fake_or_real_news.csv"
Columns: "id", "title", "text", "label"

📥 Dataset:
https://drive.google.com/file/d/1p7rLTHIz87dOZzRNpss4rVioVuTuh_OJ/view?usp=sharing

⚙️ Run Locally

pip install -r requirements.txt
python -m streamlit run app.py

Open: "http://localhost:8501"

🖱️ Usage

1. Enter or paste news text.
2. Click Check News.
3. View the result: Real News ✅ / Fake News ❌

🧠 Workflow

News Text → Preprocessing → Feature Extraction → ML Model → Prediction

📁 Project Structure

Fake-News-Detection/
├── app.py
├── requirements.txt
├── fake_or_real_news.csv
├── model/
└── README.md