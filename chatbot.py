import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CustomerSupportChatbot:

    def __init__(self, faq_file="faq_data.json"):

        # =====================================================
        # FIND FAQ FILE
        # =====================================================

        base_dir = Path(__file__).resolve().parent
        faq_path = base_dir / faq_file

        # Check if FAQ file exists
        if not faq_path.exists():
            raise FileNotFoundError(
                f"FAQ file not found: {faq_path}"
            )

        # =====================================================
        # LOAD FAQ KNOWLEDGE BASE
        # =====================================================

        with open(
            faq_path,
            "r",
            encoding="utf-8"
        ) as file:

            self.faq_data = json.load(file)

        # =====================================================
        # PREPARE FAQ DATA
        # =====================================================

        self.questions = []
        self.intents = []
        self.answers = []

        for item in self.faq_data:

            intent = item.get(
                "intent",
                "unknown"
            )

            answer = item.get(
                "answer",
                "Sorry, I don't have an answer for that."
            )

            questions = item.get(
                "questions",
                []
            )

            for question in questions:

                self.questions.append(
                    question
                )

                self.intents.append(
                    intent
                )

                self.answers.append(
                    answer
                )

        # =====================================================
        # CHECK FAQ DATA
        # =====================================================

        if not self.questions:

            raise ValueError(
                "No questions were found in faq_data.json."
            )

        # =====================================================
        # CREATE TF-IDF MODEL
        # =====================================================

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english"
        )

        # =====================================================
        # CONVERT FAQ QUESTIONS INTO VECTORS
        # =====================================================

        self.question_vectors = (
            self.vectorizer.fit_transform(
                self.questions
            )
        )

        # =====================================================
        # CONVERSATION HISTORY
        # =====================================================

        self.conversation_history = []

    # =========================================================
    # GET CHATBOT RESPONSE
    # =========================================================

    def get_response(self, user_message):

        # Clean user input
        user_message = str(
            user_message
        ).strip()

        # Empty message protection
        if not user_message:

            return (
                "Please enter a question so I can help you.",
                "unknown",
                0.0
            )

        # =====================================================
        # CONVERT USER MESSAGE INTO VECTOR
        # =====================================================

        user_vector = (
            self.vectorizer.transform(
                [user_message]
            )
        )

        # =====================================================
        # CALCULATE COSINE SIMILARITY
        # =====================================================

        similarities = cosine_similarity(
            user_vector,
            self.question_vectors
        )[0]

        # =====================================================
        # FIND BEST MATCH
        # =====================================================

        best_index = similarities.argmax()

        confidence = similarities[
            best_index
        ]

        # =====================================================
        # CONFIDENCE SCORE
        # =====================================================

        confidence_score = round(
            float(confidence) * 100,
            2
        )

        # =====================================================
        # MINIMUM CONFIDENCE THRESHOLD
        # =====================================================

        if confidence < 0.25:

            response = (
                "I'm sorry, I don't fully understand "
                "your question. Could you please "
                "provide more details?"
            )

            intent = "unknown"

        else:

            response = self.answers[
                best_index
            ]

            intent = self.intents[
                best_index
            ]

        # =====================================================
        # SAVE CONVERSATION
        # =====================================================

        self.conversation_history.append(
            {
                "user": user_message,
                "bot": response,
                "intent": intent,
                "confidence": confidence_score
            }
        )

        # =====================================================
        # RETURN RESULT
        # =====================================================

        return (
            response,
            intent,
            confidence_score
        )

    # =========================================================
    # GET CONVERSATION HISTORY
    # =========================================================

    def get_history(self):

        return self.conversation_history

    # =========================================================
    # CLEAR CONVERSATION HISTORY
    # =========================================================

    def clear_history(self):

        self.conversation_history = []
