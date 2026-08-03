class PromptTemplates:
    """
    Contains prompt templates for different RAG modes.
    """

    @staticmethod
    def ask_question(context, question):
        return f"""
    You are an expert AI assistant.

    You have been provided with context retrieved from the user's uploaded document.

    Your objective is to answer the user's question as accurately and naturally as possible.

    Instructions:

    1. If the answer exists in the document, answer primarily using the document.
    2. If the document partially answers the question, combine the document information with your own knowledge while prioritizing the document.
    3. If the document does not contain relevant information, answer using your own knowledge.
    4. Never say "I could not find the answer" unless absolutely nothing is known.
    5. Explain concepts in a clear and beginner-friendly way.
    6. Use headings, bullet points and examples whenever appropriate.

    ==================== DOCUMENT CONTEXT ====================

    {context}

    ==========================================================

    Question:
    {question}

    Answer:
    """

    @staticmethod
    def summarize(context):
        return f"""
    You are an expert AI assistant.

    Create a comprehensive yet easy-to-understand summary of the uploaded document.

    Instructions:

    1. Preserve the important information.
    2. Use simple language.
    3. Organize the summary using headings.
    4. Use bullet points wherever appropriate.
    5. Include the key ideas, important concepts and conclusions.
    6. If the document is very long, provide:
    - Executive Summary
    - Key Concepts
    - Important Details
    - Final Takeaways
    7. Ignore unnecessary repetition.

    ==================== DOCUMENT ====================

    {context}

    ==================================================

    Summary:
    """

    @staticmethod
   
    def important_questions(context):
        return f"""
    You are an expert AI assistant.

    Read the uploaded document carefully.

    Generate the most important questions that someone should practice after reading this document.

    Requirements:

    • Include easy questions.
    • Include medium questions.
    • Include difficult questions.
    • Include conceptual questions.
    • Include interview-style questions.

    Organize them under headings.

    ==================== DOCUMENT ====================

    {context}

    ==================================================

    Questions:
    """

    @staticmethod
    def quiz(context):
        return f"""
    You are an expert AI assistant.

    Create a quiz based only on the uploaded document.

    Requirements:

    • 5 Easy MCQs
    • 5 Medium MCQs
    • 5 Difficult MCQs

    For every question provide:

    Question

    A)

    B)

    C)

    D)

    Correct Answer

    Explanation

    ==================== DOCUMENT ====================

    {context}

    ==================================================

    Quiz:
    """

    @staticmethod
    def flashcards(context):
        return f"""
    You are an expert AI assistant.

    Generate high-quality flashcards from the uploaded document.

    Requirements:

    • Cover every important concept.
    • Keep each answer concise.
    • Use one concept per flashcard.

    Format:

    Question:

    Answer:

    Difficulty:

    ==================== DOCUMENT ====================

    {context}

    ==================================================

    Flashcards:
    """


    @staticmethod
    def study_notes(context):
        return f"""
    You are an expert teacher.

    Generate comprehensive study notes from the uploaded document.

    Organize the notes as follows:

    # Overview

    # Important Definitions

    # Core Concepts

    # Working Principle

    # Step-by-Step Explanation

    # Examples

    # Advantages

    # Disadvantages

    # Applications

    # Interview Questions

    # Common Mistakes

    # Key Takeaways

    Use tables wherever useful.

    ==================== DOCUMENT ====================

    {context}

    ==================================================

    Study Notes:
    """



    @staticmethod
    def important_topics(context):
        return f"""
    You are an expert AI study assistant.

    The following context comes directly from the uploaded document.

    Your task is to identify ONLY the important topics discussed in the document.

    Instructions:

    - Use ONLY the provided context.
    - Do NOT add information that is not present in the document.
    - Group related topics together.
    - Arrange topics from basic to advanced whenever possible.
    - Give each topic a short 2-3 line explanation.
    - Mention why the topic is important.
    - If there are subtopics, include them as bullet points.
    - Use clear Markdown formatting.

    If the document does not contain enough information, mention only the topics that are available.

    ================ DOCUMENT ================

    {context}

    ==========================================

    Return the output in the following format:

    # Important Topics

    ## 1. Topic Name
    Brief explanation.

    Subtopics:
    - Subtopic 1
    - Subtopic 2
    - Subtopic 3

    Why it is important:
    - ...

    ---

    ## 2. Topic Name
    Brief explanation.

    Subtopics:
    - ...
    - ...

    Why it is important:
    - ...

    Continue until all major topics have been covered.

    Important Topics:
    """