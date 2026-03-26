📰 Fake News Detection App
👩‍💻 Developer: Divya Pal
📝 Project Description
The Fake News Detection App allows users to check whether a news article is real or fake.
Users enter news text, and the app predicts its authenticity using a trained machine learning model.
This project demonstrates practical applications of AI and ML concepts, including:
Text preprocessing
Feature extraction
Classification
✨ Features
📰 Enter news text to check if it is real or fake
💻 User-friendly interface built with Streamlit
⚡ Provides immediate prediction results locally
📂 Dataset included for training and testing
📊 Dataset
The app uses the Fake or Real News Dataset
📄 File name: fake_or_real_news.csv
🏷 Columns: id, title, text, label
🔗 Download link: Dataset⁠�
⚠️ Note: The dataset is large, so it is hosted externally
⚙️ How to Run the App Locally
Clone the repository or download the project folder.
Ensure Python 3.x is installed.
Install dependencies using the requirements file:
Bash
pip install -r requirements.txt
Run the Streamlit app:
Bash
python -m streamlit run app.py
Open the link shown in the console (usually http://localhost:8501) in your browser.
📦 Requirements
streamlit
pandas
scikit-learn
joblib
These packages are included in requirements.txt for easy installation.
🖱 Usage
Open the app in a web browser.
Enter the news text in the provided input field.
Click Check News.
View the prediction:
Real News ✅
Fake News ❌
👩‍💻 Developer
Name: Divya Pal
Course Project: Fundamentals of AI and ML
Note: This app runs locally. Deployment to the web was not done.
