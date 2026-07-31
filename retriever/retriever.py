from embeddings.embedder import TextEmbedder
from vectorstore.faiss_store import FAISSStore


class Retriever:
    """
    Retrieves relevant chunks for a user query.
    """

    def __init__(self):
        self.embedder = TextEmbedder()

        self.store = FAISSStore()

        self.store.load()

    def retrieve(
        self,
        query,
        top_k=3,
    ):
        """
        Retrieve relevant chunks.

        Parameters
        ----------
        query : str

        top_k : int

        Returns
        -------
        list[str]
        """

        if not isinstance(query, str):
            raise TypeError(
                "Query must be a string."
            )

        if len(query.strip()) == 0:
            return []

        query_embedding = self.embedder.embed(
            [query]
        )

        chunks = self.store.search(
            query_embedding,
            top_k=top_k,
        )

        return chunks