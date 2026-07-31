from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL


class TextEmbedder:
    """
    Generates embeddings for text chunks.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    def embed(self, texts):
        """
        Generate embeddings.

        Parameters
        ----------
        texts : list[str]

        Returns
        -------
        numpy.ndarray
        """

        if not isinstance(texts, list):
            raise TypeError(
                "Input must be a list of strings."
            )

        if len(texts) == 0:
            return []

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=False,
        )

        return embeddings