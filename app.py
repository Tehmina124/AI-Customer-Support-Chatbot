
import streamlit as st
import io

# Optional voice libraries
try:
    import speech_recognition as sr
    SPEECH_AVAILABLE = True
except Exception:
    SPEECH_AVAILABLE = False

try:
    from gtts import gTTS
    TTS_AVAILABLE = True
except Exception:
    TTS_AVAILABLE = False

from chatbot import CustomerSupportChatbot


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# MODERN UI
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #f8fbff 0%,
            #eef5ff 50%,
            #f8fbff 100%
        );
    }

    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #0f172a 0%,
            #172554 100%
        );
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {
        color: white !important;
    }

    h1 {
        font-size: 42px !important;
        font-weight: 800 !important;
        color: #0f172a !important;
        letter-spacing: -1px;
    }

    h2 {
        color: #172554 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #1e3a8a !important;
        font-weight: 700 !important;
    }

    div[data-testid="column"] {
        background: rgba(255,255,255,0.85);
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 8px 25px rgba(15,23,42,0.05);
    }

    .stTextInput input {
        border-radius: 12px;
        border: 1px solid #cbd5e1;
        min-height: 48px;
        background: white;
    }

    .stButton > button {
        border-radius: 12px;
        min-height: 45px;
        font-weight: 700;
        border: none;
        background: linear-gradient(
            90deg,
            #2563eb,
            #4f46e5
        );
        color: white;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(37,99,235,0.25);
    }

    [data-testid="stChatMessage"] {
        border-radius: 16px;
        padding: 14px;
        margin-bottom: 12px;
    }

    audio {
        width: 100%;
        border-radius: 10px;
    }

    hr {
        border-color: #dbe4f0;
        margin: 25px 0;
    }

    .footer-text {
        text-align: center;
        color: #64748b;
        font-size: 14px;
        padding: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chatbot" not in st.session_state:

    try:
        st.session_state.chatbot = CustomerSupportChatbot()
        st.session_state.chatbot_error = None

    except Exception as e:
        st.session_state.chatbot = None
        st.session_state.chatbot_error = str(e)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🤖 AI Support")

    st.caption("Intelligent Customer Assistant")

    st.divider()

    st.subheader("⚡ Capabilities")

    st.write("💬 Order Support")
    st.write("💳 Payment Questions")
    st.write("📦 Shipping Information")
    st.write("🔄 Refund Assistance")
    st.write("🧾 Order Status")
    st.write("🎤 Voice Interaction")
    st.write("🔊 AI Voice Responses")

    st.divider()

    st.subheader("📊 Session")

    st.metric(
        "Conversations",
        len(st.session_state.messages)
    )

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


# =========================================================
# HERO
# =========================================================

st.title("🤖 AI Customer Support Assistant")

st.write(
    "Smart • Fast • Voice Enabled • Intent Aware"
)

st.success("🟢 AI Assistant Online")


# =========================================================
# CHATBOT ERROR CHECK
# =========================================================

if st.session_state.chatbot_error:

    st.error(
        "⚠️ The chatbot could not be initialized."
    )

    st.code(
        st.session_state.chatbot_error
    )

    st.stop()


# =========================================================
# FEATURES
# =========================================================

st.header("✨ AI Support Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("🎯 Intent Detection")

    st.write(
        "Automatically identifies what the customer "
        "needs and understands the purpose of the request."
    )


with col2:

    st.subheader("🧠 Smart Responses")

    st.write(
        "Provides relevant answers from your customer "
        "support knowledge base."
    )


with col3:

    st.subheader("🎤 Voice Support")

    st.write(
        "Speak naturally using your microphone and "
        "receive an AI-generated voice response."
    )


# =========================================================
# CONVERSATION
# =========================================================

st.header("💬 Conversation")

st.caption(
    "Ask your AI Customer Support Assistant anything "
    "about orders, payments, refunds, shipping or support."
)


# =========================================================
# EMPTY STATE
# =========================================================

if not st.session_state.messages:

    st.info(
        "👋 Start a conversation by asking a customer "
        "support question below."
    )


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message("user"):

        st.write(message["user"])


    with st.chat_message("assistant"):

        st.write(message["bot"])

        st.caption(
            f"🎯 Intent: {message['intent']}  |  "
            f"📊 Confidence: {message['confidence']}%"
        )

        # -------------------------------------------------
        # TEXT TO SPEECH
        # -------------------------------------------------

        if TTS_AVAILABLE:

            try:

                tts = gTTS(
                    text=str(message["bot"]),
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

                st.caption(
                    "🔊 Voice response unavailable."
                )


# =========================================================
# TEXT CHAT
# =========================================================

st.subheader("💬 Text Chat")

text_input = st.text_input(
    "Type your question:",
    placeholder="Example: Where is my order?",
    key="text_question"
)

send_button = st.button(
    "Send Message  ➜",
    use_container_width=True
)


# =========================================================
# PROCESS TEXT
# =========================================================

if send_button:

    if not text_input.strip():

        st.warning(
            "Please type a question first."
        )

    else:

        try:

            response, intent, confidence = (
                st.session_state.chatbot.get_response(
                    text_input.strip()
                )
            )

            st.session_state.messages.append(
                {
                    "user": text_input.strip(),
                    "bot": response,
                    "intent": intent,
                    "confidence": confidence
                }
            )

            st.rerun()

        except Exception as e:

            st.error(
                "❌ Unable to process your question."
            )

            st.code(str(e))


# =========================================================
# VOICE SUPPORT
# =========================================================

st.divider()

st.header("🎤 Voice Support")

st.write(
    "Talk naturally with your AI Customer Support Assistant."
)


if not SPEECH_AVAILABLE:

    st.warning(
        "🎤 Speech recognition is unavailable. "
        "You can still use Text Chat."
    )

else:

    st.info(
        "🎙️ Click the microphone below and speak your question."
    )

    # -----------------------------------------------------
    # AUDIO INPUT
    # -----------------------------------------------------

    try:

        audio_value = st.audio_input(
            "🎤 Record your question"
        )

    except Exception as e:

        audio_value = None

        st.warning(
            "🎤 Microphone input is currently unavailable."
        )


    # -----------------------------------------------------
    # SPEECH TO TEXT
    # -----------------------------------------------------

    if audio_value is not None:

        try:

            recognizer = sr.Recognizer()

            audio_bytes = audio_value.getvalue()

            audio_file = io.BytesIO(
                audio_bytes
            )

            with sr.AudioFile(audio_file) as source:

                audio_data = recognizer.record(
                    source
                )

            user_input = recognizer.recognize_google(
                audio_data
            )

            st.success(
                f"📝 You said: {user_input}"
            )


            # ---------------------------------------------
            # CHATBOT RESPONSE
            # ---------------------------------------------

            response, intent, confidence = (
                st.session_state.chatbot.get_response(
                    user_input
                )
            )


            st.session_state.messages.append(
                {
                    "user": user_input,
                    "bot": response,
                    "intent": intent,
                    "confidence": confidence
                }
            )

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
                "❌ Voice processing error."
            )

            st.caption(str(e))


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer-text">

        🤖 <strong>AI Customer Support Assistant</strong><br>

        Built with Python • Streamlit • Speech Recognition • gTTS<br>

        Intelligent • Fast • Voice Enabled • Intent Aware

    </div>
    """,
    unsafe_allow_html=True
)
