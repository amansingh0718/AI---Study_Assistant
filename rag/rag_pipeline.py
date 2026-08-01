from retriever.retriever import Retriever
from llm.ollama_client import OllamaClient
from prompts.prompt_templates import PromptTemplates


class RAGPipeline:
    """
    Executes the complete Retrieval-Augmented Generation pipeline.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.llm = OllamaClient()

    def run(
        self,
        mode,
        user_input,
        top_k=3,
    ):
        """
        Execute the RAG pipeline.

        Parameters
        ----------
        mode : str

        user_input : str

        top_k : int

        Returns
        -------
        str
        """

        if not isinstance(user_input, str):
            raise TypeError(
                "User input must be a string."
            )

        if len(user_input.strip()) == 0:
            raise ValueError(
                "User input cannot be empty."
            )

        chunks = self.retriever.retrieve(
            user_input,
            top_k=top_k,
        )

        if not chunks:
            return "No relevant information found."

        context = "\n\n".join(chunks)

        prompt = self._build_prompt(
            mode,
            context,
            user_input,
        )

        answer = self.llm.generate(prompt)

        return answer

    def _build_prompt(
        self,
        mode,
        context,
        user_input,
    ):
        """
        Select the appropriate prompt template.
        """

        mode = mode.lower()

        if mode == "ask":
            return PromptTemplates.ask_question(
                context,
                user_input,
            )

        elif mode == "summary":
            return PromptTemplates.summarize(
                context
            )

        elif mode == "topics":
            return PromptTemplates.important_topics(
                context
            )

        elif mode == "questions":
            return PromptTemplates.important_questions(
                context
            )

        elif mode == "quiz":
            return PromptTemplates.quiz(
                context
            )

        elif mode == "flashcards":
            return PromptTemplates.flashcards(
                context
            )

        else:
            raise ValueError(
                f"Unsupported mode: {mode}"
            )