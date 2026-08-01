from retriever.retriever import Retriever
from llm.ollama_client import OllamaClient
from prompts.prompt_templates import PromptTemplates
from storage.document_store import DocumentStore


class RAGPipeline:
    """
    Executes the complete Retrieval-Augmented Generation pipeline.
    """

    def __init__(self):

        self.retriever = Retriever()

        self.llm = OllamaClient()

        self.document_store = DocumentStore(
            "storage"
        )

    def run(
        self,
        mode,
        user_input="",
        top_k=3,
    ):

        mode = mode.lower()

        if mode == "ask":

            if len(user_input.strip()) == 0:
                raise ValueError(
                    "Question cannot be empty."
                )

            chunks = self.retriever.retrieve(
                user_input,
                top_k=top_k,
            )

            if not chunks:
                return (
                    "No relevant information found."
                )

            context = "\n\n".join(chunks)

            prompt = PromptTemplates.ask_question(
                context,
                user_input,
            )

        else:

            context = self.document_store.load()

            if mode == "summary":

                prompt = PromptTemplates.summarize(
                    context
                )

            elif mode == "topics":

                prompt = (
                    PromptTemplates.important_topics(
                        context
                    )
                )

            elif mode == "questions":

                prompt = (
                    PromptTemplates.important_questions(
                        context
                    )
                )

            elif mode == "quiz":

                prompt = PromptTemplates.quiz(
                    context
                )

            elif mode == "flashcards":

                prompt = (
                    PromptTemplates.flashcards(
                        context
                    )
                )

            else:

                raise ValueError(
                    f"Unsupported mode: {mode}"
                )

        return self.llm.generate(prompt)