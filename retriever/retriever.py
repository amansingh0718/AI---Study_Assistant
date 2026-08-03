from embeddings.embedder import TextEmbedder
from vector_store.faiss_store import FAISSStore


class Retriever:
    """
    Retrieves relevant chunks for a user query.
    """

    def __init__(self):
        self.embedder = TextEmbedder()
        self.store = FAISSStore()

    def retrieve(
        self,
        query,
        top_k=3,
    ):

        self.store.load()

        query_embedding = self.embedder.embed([query])

        print("=" * 80)
        print("QUESTION :", query)

        chunks = self.store.search(
            query_embedding,
            top_k=top_k,
        )

        print("\nRetrieved Chunks:\n")

        for i, chunk in enumerate(chunks):

            print(f"Chunk {i+1}")
            print("-" * 60)
            print(chunk[:500])
            print()

        return chunks