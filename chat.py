import streamlit as st
from bot import simple_chatbot

st.set_page_config(page_title="Simple NLP Chatbot 💬", layout="centered")

st.title("🤖 Simple Chatbot with NLP")

st.markdown("Type a mesage below and let's chat!")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.messages.append(("You", user_input))

    response = simple_chatbot(user_input)
    st.session_state.messages.append(("Bot", response))

for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**👦 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")