# app.py
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# -----------------------
# Title and Description
# -----------------------
st.set_page_config(page_title="📰 Fake News Detection", layout="centered")
st.title("📰 Fake News Detection App")
st.markdown("""
Enter any news text below and check whether it is **Real** or **Fake**.
Developed by **Divya Pal**
""")

# -----------------------
# Load Dataset
# -----------------------
try:
    df = pd.read_csv("fake_or_real_news.csv")
    st.success("✅ Dataset loaded successfully!")
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# -----------------------
# Prepare Model
# -----------------------
# Convert labels to numeric if not already
df['label'] = df['label'].map({'FAKE': 0, 'REAL': 1}).fillna(df['label'])

# Use TF-IDF to vectorize text
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train simple Naive Bayes classifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# -----------------------
# Input Text from User
# -----------------------
user_input = st.text_area("Enter news text:")

if st.button("Check News"):
    if user_input.strip() == "":
        st.warning("Please enter some text to check!")
    else:
        # Vectorize user input and predict
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]

        # Map numeric label back to text
        result = "Real News ✅" if prediction == 1 else "Fake News ❌"
        st.markdown(f"### Prediction: {result}")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.markdown("Developed with ❤️ by Divya Pal")