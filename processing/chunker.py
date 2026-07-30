from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class TextChunker:
    """
    Splits text into overlapping chunks.
    """

    def chunk_text(self, text):
        """
        Split text into chunks.

        Parameters
        ----------
        text : str

        Returns
        -------
        list[str]
        """

        if not isinstance(text, str):
            raise TypeError(
                "Input text must be a string."
            )

        if len(text.strip()) == 0:
            return []

        chunks = []

        start = 0

        text_length = len(text)

        while start < text_length:

            end = start + CHUNK_SIZE

            chunk = text[start:end].strip()

            if chunk:
                chunks.append(chunk)

            start += CHUNK_SIZE - CHUNK_OVERLAP

        return chunks