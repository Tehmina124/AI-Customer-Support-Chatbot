<p align="center">
  <img src="./AI CUSTOMER SUPPORT.png" width="100%" alt="AI Customer Support Chatbot Banner">
</p>

<h1 align="center">🤖 AI Customer Support Chatbot</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Framework-red?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/NLP-TF--IDF-orange?style=for-the-badge" alt="NLP">
  <img src="https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Speech--to--Text-Enabled-purple?style=for-the-badge" alt="Speech to Text">
  <img src="https://img.shields.io/badge/Text--to--Speech-Enabled-green?style=for-the-badge" alt="Text to Speech">
</p>

<p align="center">
  <b>🤖 An AI-powered customer support chatbot for handling orders, refunds, payments, shipping, returns and account-related queries.</b>
</p>

<p align="center">
  Built with Python, NLP, Scikit-learn and Streamlit.
</p>

<p align="center">
  <a href="https://ai-customer-support-chatbot-k2dnldj9mfkkme2eqok7oz.streamlit.app/">
    🚀 <b>View Live Demo</b>
  </a>
</p>

---

## 📌 About The Project

**AI Customer Support Chatbot** is an intelligent web-based customer support application developed using **Python, Natural Language Processing (NLP), Scikit-learn and Streamlit**.

The chatbot is designed to answer frequently asked customer-support questions related to **orders, refunds, payments, shipping, returns and account support**.

The system uses a predefined **FAQ Knowledge Base** and **TF-IDF Vectorization with Cosine Similarity** to find the most relevant answer for a user's question.

It also provides **intent recognition, confidence scoring, conversation history, voice input, speech-to-text and text-to-speech** capabilities.

---

## ✨ Key Features

### 🤖 AI Customer Support

Answers common customer questions related to:

* 📦 Orders
* 💰 Refunds
* 💳 Payments
* 🚚 Shipping
* 🔄 Returns
* 👤 Account and support issues

### 📚 FAQ Knowledge Base

Uses a structured FAQ dataset containing:

* Customer questions
* Intents
* Support answers
* Multiple question variations

### 🧠 Intent Recognition

Automatically identifies the intent behind a customer's question.

Example:

```text
User: Where is my order?

Intent: order_tracking
```

### 📊 Confidence Score

The chatbot calculates a similarity score and displays the confidence percentage for the predicted answer.

Example:

```text
🎯 Intent: order_tracking
📊 Confidence: 87.45%
```

### 💬 Conversation History

Previous user questions and chatbot responses remain visible during the conversation.

### 🔎 NLP-Based Question Matching

The application uses:

* TF-IDF Vectorization
* Cosine Similarity
* Text preprocessing
* Similarity-based FAQ matching

to identify the most relevant response.

### ❓ Unknown Query Handling

If the chatbot does not find a sufficiently similar question, it avoids giving a random answer and politely informs the user that it is designed for customer-support queries.

### 🎤 Voice Input

Users can ask questions using a microphone.

### 📝 Speech-to-Text

Spoken questions are converted into text using speech recognition.

### 🔊 Text-to-Speech

The chatbot can convert its written response into spoken audio.

### 🌐 Web-Based Interface

The application provides a clean and simple interface using **Streamlit**.

### ☁️ Live Deployment

The chatbot is deployed online using **Streamlit Community Cloud**.

---

## 🛠️ Technologies Used

| Technology                   | Purpose                    |
| ---------------------------- | -------------------------- |
| 🐍 Python                    | Application Development    |
| 🎈 Streamlit                 | Web Application Interface  |
| 🧠 NLP                       | Question Understanding     |
| 📊 Scikit-learn              | TF-IDF & Cosine Similarity |
| 📚 JSON                      | FAQ Knowledge Base         |
| 🎤 SpeechRecognition         | Speech-to-Text             |
| 🔊 gTTS                      | Text-to-Speech             |
| 🐙 GitHub                    | Version Control            |
| ☁️ Streamlit Community Cloud | Deployment                 |

---

## 🧠 AI / NLP Techniques

This project demonstrates practical use of several AI and NLP concepts:

* Natural Language Processing
* TF-IDF Vectorization
* Cosine Similarity
* Intent Recognition
* Text Similarity
* Confidence Scoring
* FAQ Retrieval
* Speech Recognition
* Text-to-Speech

### 🔄 How The Chatbot Works

```text
                👤 User
                   │
          ┌────────┴────────┐
          │                 │
       💬 Text           🎤 Voice
          │                 │
          │          📝 Speech-to-Text
          │                 │
          └────────┬────────┘
                   ↓
             🧠 NLP Processing
                   ↓
          🔎 TF-IDF Vectorization
                   ↓
          📐 Cosine Similarity
                   ↓
           🎯 Intent Recognition
                   ↓
             📚 FAQ Matching
                   ↓
          ┌────────┴────────┐
          │                 │
       💬 Response       ❓ Unknown
          │                 │
          ↓                 ↓
      🔊 Text-to-Speech   Polite
          │              Fallback
          ↓
        👤 User
```

---

## 📂 Project Structure

```text
AI-Customer-Support-Chatbot/
│
├── app.py
├── chatbot.py
├── faq_data.json
├── requirements.txt
├── AI-CUSTOMER-SUPPORT.png
└── README.md
```

### 📄 `app.py`

Main Streamlit application containing:

* Chat interface
* Text input
* Voice input
* Conversation history
* Speech-to-text
* Text-to-speech
* Intent and confidence display

### 📄 `chatbot.py`

Contains the chatbot logic, including:

* FAQ loading
* TF-IDF vectorization
* Cosine similarity
* Intent recognition
* Confidence calculation
* Response generation
* Conversation history

### 📄 `faq_data.json`

Contains the customer-support knowledge base with questions, intents and answers.

### 📄 `requirements.txt`

Contains the Python packages required to run the application.

### 📄 `AI-CUSTOMER-SUPPORT.png`

Project banner used in the GitHub README.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Tehmina124/AI-Customer-Support-Chatbot.git
```

### 2️⃣ Open the Project Folder

```bash
cd AI-Customer-Support-Chatbot
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python -m streamlit run app.py
```

### 5️⃣ Open in Browser

Streamlit will provide a local URL, normally:

```text
http://localhost:8501
```

---

## 🌐 Live Demo

🚀 **Try the deployed AI Customer Support Chatbot:**

https://ai-customer-support-chatbot-k2dnldj9mfkkme2eqok7oz.streamlit.app/

The application can be accessed from a web browser without installing the project locally.

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

### Deployment Workflow

```text
Python Development
        ↓
NLP / FAQ Chatbot
        ↓
Streamlit Application
        ↓
GitHub Repository
        ↓
Streamlit Community Cloud
        ↓
🌐 Live Web Application
```

---

## 🎯 Project Objectives

The main objectives of this project were:

* Build a practical AI-powered customer support system.
* Automate frequently asked customer questions.
* Implement an FAQ knowledge base.
* Understand intent recognition.
* Apply TF-IDF and Cosine Similarity.
* Calculate response confidence.
* Maintain conversation history.
* Add voice-based interaction.
* Implement speech-to-text.
* Implement text-to-speech.
* Develop a web application using Streamlit.
* Deploy an AI application online.
* Practice GitHub project management.

---

## 💡 What I Learned

Through this project, I gained practical experience in:

* Python development
* Streamlit application development
* Natural Language Processing
* TF-IDF Vectorization
* Cosine Similarity
* Intent Recognition
* Confidence Scoring
* FAQ-based chatbot development
* Conversation history management
* Speech Recognition
* Text-to-Speech
* JSON-based knowledge bases
* GitHub repository management
* Streamlit deployment
* Debugging and testing AI applications

This project helped me understand how NLP and machine learning concepts can be converted into a practical customer-support application.

---

## 🔮 Future Improvements

Future versions can include:

* 🤖 LLM-powered responses
* 🧠 Context-aware conversations
* 📚 Larger knowledge base
* 🌍 Multi-language support
* 🎤 Improved voice recognition
* 🔊 Multiple voice options
* 📊 Advanced analytics dashboard
* 👤 User authentication
* 🎫 Customer support ticket creation
* 📧 Automated email support
* 🗃️ Customer database integration
* 💾 Persistent conversation storage
* 🔐 Secure API integration

---

## 🧪 Example Questions

Users can ask questions such as:

```text
Where is my order?
```

```text
I want a refund.
```

```text
My payment failed.
```

```text
How long does shipping take?
```

```text
How can I return my order?
```

```text
I forgot my password.
```

The chatbot analyzes the question, identifies the most relevant intent and returns the corresponding support response.

---

## 👩‍💻 About Me

### Tehmina Anwar

**BSAI Student | AI/ML Engineer | Python Developer**

I am a Bachelor of Science in Artificial Intelligence student interested in building practical AI and Machine Learning applications.

My areas of interest include:

* Python
* Machine Learning
* Generative AI
* Large Language Models
* RAG
* Natural Language Processing
* Computer Vision
* AI Application Development

---

## 🔗 Connect With Me

### 💻 GitHub

https://github.com/Tehmina124

### 🔗 LinkedIn

https://www.linkedin.com/in/tehmina-anwar-77b8a8414/

### 🌐 Portfolio

https://tehmina-portfolio-five.vercel.app/

### 🚀 Live Project

https://ai-customer-support-chatbot-k2dnldj9mfkkme2eqok7oz.streamlit.app/

---

## ⭐ Support

If you found this project useful or interesting, please consider giving the repository a ⭐ **Star** on GitHub.

---

<p align="center">
  <b>Built with ❤️ using Python, NLP, Scikit-learn and Streamlit</b>
</p>

<p align="center">
  © 2026 Tehmina Anwar | AI Customer Support Chatbot
</p>
