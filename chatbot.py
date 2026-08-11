import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CustomerSupportChatbot:

    def __init__(self, faq_file="faq_data.json"):

        # Load FAQ knowledge base
        with open(faq_file, "r", encoding="utf-8") as file:
            self.faq_data = json.load(file)

        # Prepare questions and answers
        self.questions = []
        self.intents = []
        self.answers = []

        for item in self.faq_data:

            for question in item["questions"]:
                self.questions.append(question)
                self.intents.append(item["intent"])
                self.answers.append(item["answer"])

        # Create TF-IDF model
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english"
        )

        # Convert FAQ questions into vectors
        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

        # Conversation history
        self.conversation_history = []

    def get_response(self, user_message):

        # Convert user message into vector
        user_vector = self.vectorizer.transform(
            [user_message]
        )

        # Calculate similarity
        similarities = cosine_similarity(
            user_vector,
            self.question_vectors
        )[0]

        # Find best matching question
        best_index = similarities.argmax()

        confidence = similarities[best_index]

        # Convert confidence to percentage
        confidence_score = round(
            confidence * 100,
            2
        )

        # Minimum confidence threshold
        if confidence < 0.25:

            response = (
                "I'm sorry, I don't fully understand your question. "
                "Could you please provide more details?"
            )

            intent = "unknown"

        else:

            response = self.answers[best_index]
            intent = self.intents[best_index]

        # Save conversation
        self.conversation_history.append({
            "user": user_message,
            "bot": response,
            "intent": intent,
            "confidence": confidence_score
        })

        return (
            response,
            intent,
            confidence_score
        )

    def get_history(self):

        return self.conversation_history