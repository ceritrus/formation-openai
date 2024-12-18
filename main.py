import streamlit as st

pg = st.navigation([
    st.Page("pages/chatbot.py", title="Chatbot", icon="🤖"),
    st.Page("pages/whisper.py", title="Whisper", icon="🎵"),
    st.Page("pages/tts.py", title="Text to Speech", icon="📢"),
])
pg.run()
