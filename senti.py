import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")
st.title("🧠 Sentiment Analysis App (NLTK + Streamlit)")
st.write("Enter some text to see if it's Positive, Negative or Neutral.")
user_input =st.text_area("📝 Your Text", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("please enter some text.")
    else:
        sentiment = sia.polarity_scores(user_input)
        score = sentiment['compound']

        if score >= 0.05:
            st.success("Sentiment: **Positive**😊")
        elif score <= 0.05:
            st.error("Sentiment: **Negative** 😤")
        else:
            st.info("Sentiment: **Neutral**😑")

        st.write("## Detailed Scores:")
        st.json(sentiment)