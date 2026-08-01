import pickle

import faiss
import numpy as np

from config import (
    FAISS_DIR,
    FAISS_INDEX_FILE,
    FAISS_CHUNKS_FILE,
)


class FAISSStore:
    """
    Stores and searches embeddings using FAISS.
    """

    def __init__(self):
        self.index = None
        self.chunks = []

    def create_index(self, embeddings):
        """
        Create a FAISS index from embeddings.
        """

        if len(embeddings) == 0:
            raise ValueError(
                "Embeddings cannot be empty."
            )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            embeddings.astype(np.float32)
        )

    def add_chunks(self, chunks):
        """
        Store original text chunks.
        """

        self.chunks = chunks

    def save(self):
        """
        Save FAISS index and chunks.
        """

        if self.index is None:
            raise ValueError(
                "No FAISS index to save."
            )

        # Create directory if it doesn't exist
        FAISS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            str(FAISS_INDEX_FILE)
        )

        with open(
            FAISS_CHUNKS_FILE,
            "wb"
        ) as file:

            pickle.dump(
                self.chunks,
                file
            )

    def load(self):
        """
        Load FAISS index and chunks.
        """

        if not FAISS_INDEX_FILE.exists():
            raise FileNotFoundError(
                "FAISS index not found.\n"
                "Please upload and index a document first."
            )

        if not FAISS_CHUNKS_FILE.exists():
            raise FileNotFoundError(
                "Chunks file not found."
            )

        self.index = faiss.read_index(
            str(FAISS_INDEX_FILE)
        )

        with open(
            FAISS_CHUNKS_FILE,
            "rb"
        ) as file:

            self.chunks = pickle.load(file)

    def search(
        self,
        query_embedding,
        top_k=3,
    ):
        """
        Search most similar chunks.
        """

        if self.index is None:
            raise ValueError(
                "FAISS index is not loaded."
            )

        distances, indices = self.index.search(
            query_embedding.astype(np.float32),
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx != -1:
                results.append(
                    self.chunks[idx]
                )

        return results