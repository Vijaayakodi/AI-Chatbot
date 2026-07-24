import streamlit as st

from chatbot import ask_gemini
from memory import clear_history

st.set_page_config(
    page_title="AI ChatBot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask me anything...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = ask_gemini(question)

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

st.divider()

if st.button("🗑 Clear Chat"):

    st.session_state.messages = []

    clear_history()

    st.rerun()