import streamlit as st
import requests
from gtts import gTTS
import tempfile
import os

# API endpoint for Docker or local
API_URL = "http://127.0.0.1:8000"  # Use http://127.0.0.1:8000 if running locally without Docker

# Page setup like NotebookLM
st.set_page_config(page_title="NotebookLLM YouTube Assistant", layout="wide")

st.markdown(
    """
    <style>
    .big-font {
        font-size: 32px !important;
        font-weight: bold;
    }
    .small-font {
        font-size: 14px;
        color: grey;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="big-font">🤖NotebookLLM: ▶️YouTube Learning Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="small-font">Chat with your videos & listen to transcripts 📚🎥</div>', unsafe_allow_html=True)

# Initialize session state
if "transcript" not in st.session_state:
    st.session_state.transcript = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "video_url" not in st.session_state:
    st.session_state.video_url = ""

# Sidebar: History & Transcript
with st.sidebar:
    st.header("📜 Notebook Memory")

    if st.session_state.messages:
        st.subheader("Chat History")
        for msg in st.session_state.messages:
            role = "You" if msg["role"] == "user" else "AI"
            preview = msg["content"][:80] + ("..." if len(msg["content"]) > 80 else "")
            st.markdown(f"**{role}:** {preview}")

    if st.session_state.transcript:
        with st.expander("📝 View Transcript"):
            st.text_area("Transcript", st.session_state.transcript, height=300)

    st.markdown("---")
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.session_state.transcript = None
        st.session_state.video_url = ""
        st.experimental_rerun()

# Main input
st.markdown("### 📥 Upload YouTube Link")

youtube_url = st.text_input("Enter YouTube video URL", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Fetch Transcript"):
    if youtube_url:
        try:
            # Save video url in session
            st.session_state.video_url = youtube_url

            # Get video ID
            id_response = requests.post(f"{API_URL}/generate_videoid", json={"url": youtube_url})
            id_response.raise_for_status()
            video_id = id_response.json()["id"]

            # Get transcript
            trans_response = requests.post(f"{API_URL}/generate_transcript", json={"id": video_id})
            trans_response.raise_for_status()
            transcript = trans_response.json()["transcript"]

            st.session_state.transcript = transcript
            st.session_state.messages = []  # Reset chat

            st.success("Transcript loaded. Start chatting below!")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Chat UI
if st.session_state.transcript:
    st.markdown("### 💬 Ask Questions")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_query = st.chat_input("Ask anything about the video...")

    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        with st.spinner("Thinking..."):
            try:
                payload = {"url": st.session_state.video_url, "query": user_query}
                res = requests.post(f"{API_URL}/chat", json=payload)
                res.raise_for_status()
                response = res.json()["response"]

                st.session_state.messages.append({"role": "assistant", "content": response})
                with st.chat_message("assistant"):
                    st.markdown(response)
            except Exception as e:
                st.error(f"API Error: {str(e)}")

    # Audio option
    st.markdown("---")
    st.markdown("### 🎧 Listen to the Transcript")

    if st.button("Convert Transcript to Audio"):
        try:
            tts = gTTS(st.session_state.transcript, lang="en")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                st.audio(fp.name)

                with open(fp.name, "rb") as f:
                    st.download_button(
                        label="Download Audio",
                        data=f,
                        file_name="transcript_audio.mp3",
                        mime="audio/mpeg"
                    )

            os.remove(fp.name)
        except Exception as e:
            st.error(f"Audio conversion error: {str(e)}")
