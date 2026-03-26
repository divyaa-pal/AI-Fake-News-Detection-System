📰 Fake News Detection App
👩‍💻 Developer: Divya Pal
📝 Project Description
The Fake News Detection App allows users to check whether a news article is real or fake. Users enter news text, and the app predicts its authenticity using a trained machine learning model.
This project demonstrates practical applications of AI and ML concepts, including text preprocessing, feature extraction, and classification.
✨ Features
📰 Enter news text to check if it is real or fake
💻 User-friendly interface with Streamlit
⚡ Provides immediate prediction results locally
📂 Dataset included for training and testing
📊 Dataset
The app uses the Fake or Real News Dataset:
📄 File: fake_or_real_news.csv
🏷 Columns: id, title, text, label
🔗 Download Link (Google Drive): Dataset⁠�
⚠️ Note: The dataset is large, so it is hosted externally.
⚙️ How to Run the App Locally
1.Clone the repository or download the project folder.
2.Make sure Python 3.x is installed.
3.Install dependencies using the requirements file:
Bash
pip install -r requirements.txt
4.Run the Streamlit app:
Bash
python -m streamlit run app.py
5.Open the link shown in the console (usually http://localhost:8501) in your browser.
📦 Requirements
streamlit
pandas
scikit-learn
joblib
These are included in the requirements.txt for easy installation.
🖱 Usage
1️⃣ Open the app in a browser.
2️⃣ Enter news text in the provided field.
3️⃣ Click Check News.
4️⃣ View the prediction: Real News ✅ or Fake News ❌.
👩‍💻 Developer
Name: Divya Pal
Course Project: Fundamentals of AI and ML
Note: This app runs locally. Deployment to the web was not done.