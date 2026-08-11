import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import io

from chatbot import CustomerSupportChatbot


# ==============================
# PAGE CONFIGURATION
# ==============================

st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="🤖",
    layout="centered"
)


# ==============================
# TITLE
# ==============================

st.title("🤖 AI Customer Support Chatbot")

st.write(
    "Ask me anything about orders, refunds, payments, shipping, and support."
)


# ==============================
# CREATE CHATBOT
# ==============================

if "chatbot" not in st.session_state:
    st.session_state.chatbot = CustomerSupportChatbot()


# ==============================
# CONVERSATION HISTORY
# ==============================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==============================
# DISPLAY CONVERSATION
# ==============================

for message in st.session_state.messages:

    with st.chat_message("user"):
        st.write(message["user"])

    with st.chat_message("assistant"):

        st.write(message["bot"])

        st.caption(
            f"🎯 Intent: {message['intent']} | "
            f"📊 Confidence: {message['confidence']}%"
        )

        # ==============================
        # TEXT TO SPEECH
        # ==============================

        try:

            tts = gTTS(
                text=message["bot"],
                lang="en"
            )

            audio_buffer = io.BytesIO()

            tts.write_to_fp(audio_buffer)

            audio_buffer.seek(0)

            st.audio(
                audio_buffer,
                format="audio/mp3"
            )

        except Exception:

            st.warning(
                "🔊 Audio response is currently unavailable."
            )


# ==============================
# TEXT INPUT
# ==============================

st.subheader("💬 Text Chat")

text_input = st.text_input(
    "Type your question here:",
    placeholder="Example: Where is my order?"
)

send_button = st.button("Send 💬")


# ==============================
# PROCESS TEXT INPUT
# ==============================

if send_button and text_input:

    response, intent, confidence = (
        st.session_state.chatbot.get_response(
            text_input
        )
    )

    st.session_state.messages.append({
        "user": text_input,
        "bot": response,
        "intent": intent,
        "confidence": confidence
    })

    st.rerun()


# ==============================
# VOICE INPUT
# ==============================

st.divider()

st.subheader("🎤 Voice Input")

st.write(
    "Use your microphone to ask a question by voice."
)


try:

    audio_value = st.audio_input(
        "Click the microphone and speak"
    )

except Exception:

    audio_value = None

    st.warning(
        "🎤 Microphone is not available on this device. "
        "Connect a microphone or headset to use voice input."
    )


# ==============================
# SPEECH TO TEXT
# ==============================

if audio_value is not None:

    try:

        recognizer = sr.Recognizer()

        # Get recorded audio
        audio_bytes = audio_value.getvalue()

        audio_file = io.BytesIO(audio_bytes)

        # Read recorded audio
        with sr.AudioFile(audio_file) as source:

            audio_data = recognizer.record(source)

        # Convert Speech → Text
        user_input = recognizer.recognize_google(
            audio_data
        )

        st.success(
            f"📝 You said: {user_input}"
        )

        # ==============================
        # CHATBOT RESPONSE
        # ==============================

        response, intent, confidence = (
            st.session_state.chatbot.get_response(
                user_input
            )
        )

        # Save conversation
        st.session_state.messages.append({
            "user": user_input,
            "bot": response,
            "intent": intent,
            "confidence": confidence
        })

        st.rerun()

    except sr.UnknownValueError:

        st.error(
            "❌ I could not understand your voice. "
            "Please speak clearly and try again."
        )

    except sr.RequestError:

        st.error(
            "❌ Speech recognition service is unavailable. "
            "Please check your internet connection."
        )

    except Exception as e:

        st.error(
            f"❌ Voice processing error: {e}"
        )