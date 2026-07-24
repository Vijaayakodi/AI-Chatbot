import streamlit as st
from chatbot import ask_gemini
from memory import clear_history

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI ChatBot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD CSS ---------------- #
with open("assets/style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- SESSION ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ---------------- #
with st.sidebar:

    st.title("🤖 AI ChatBot")

    st.caption("Powered by Google Gemini")

    st.markdown("---")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        clear_history()
        st.rerun()

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        clear_history()
        st.rerun()

    st.markdown("---")

    st.success("🟢 Gemini Connected")

    st.markdown("---")

    st.markdown("### About")

    st.write(
        """
Built using

- Python
- Streamlit
- Google Gemini API
        """
    )

    st.markdown("---")

    st.caption("Made with ❤️ by Vijaayakodi")

# ---------------- HEADER ---------------- #

col1, col2 = st.columns([6, 1])

with col1:
    st.title("🤖 AI ChatBot")
    st.caption("Your Personal AI Assistant")

with col2:
    st.metric("Model", "Gemini")

st.divider()

# ---------------- CHAT HISTORY ---------------- #

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- USER INPUT ---------------- #

prompt = st.chat_input("💬 Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):

            response = ask_gemini(prompt)

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# ---------------- FOOTER ---------------- #

st.divider()

st.caption("🚀 Built with Streamlit + Google Gemini")