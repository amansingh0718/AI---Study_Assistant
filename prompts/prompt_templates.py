class PromptTemplates:
    """
    Contains prompt templates for different RAG modes.
    """

    @staticmethod
    def ask_question(context, question):
        return f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say:

"I could not find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    @staticmethod
    def summarize(context):
        return f"""
You are a helpful AI assistant.

Summarize the following document in simple language.

Context:
{context}

Summary:
"""

    @staticmethod
    def important_topics(context):
        return f"""
You are a helpful AI assistant.

Extract the most important topics from the document.

Return them as bullet points.

Context:
{context}

Topics:
"""

    @staticmethod
    def important_questions(context):
        return f"""
You are a helpful AI assistant.

Generate important questions that can be asked from the document.

Context:
{context}

Questions:
"""

    @staticmethod
    def quiz(context):
        return f"""
You are a helpful AI assistant.

Create a quiz based only on the document.

Include answers.

Context:
{context}

Quiz:
"""

    @staticmethod
    def flashcards(context):
        return f"""
You are a helpful AI assistant.

Create flashcards from the document.

Format:

Question:
Answer:

Context:
{context}

Flashcards:
"""