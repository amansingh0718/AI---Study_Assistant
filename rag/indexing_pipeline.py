from pathlib import Path

from loaders.file_loader import FileLoader

from parsers.pdf_parser import PDFParser
from parsers.image_parser import ImageParser
from parsers.txt_parser import TextParser

from processing.cleaner import TextCleaner
from processing.chunker import TextChunker

from embeddings.embedder import TextEmbedder

from vectorstore.faiss_store import FAISSStore


class IndexingPipeline:
    """
    Creates a searchable FAISS index from a document.
    """

    def __init__(self):

        self.loader = FileLoader()

        self.pdf_parser = PDFParser()

        self.image_parser = ImageParser()

        self.text_parser = TextParser()

        self.cleaner = TextCleaner()

        self.chunker = TextChunker()

        self.embedder = TextEmbedder()

        self.store = FAISSStore()

    def index_document(
        self,
        file_path,
    ):
        path = Path(file_path)

        suffix = path.suffix.lower()

        if suffix == ".pdf":

            text = self.pdf_parser.extract_text(
                file_path
            )

        elif suffix in [
            ".png",
            ".jpg",
            ".jpeg",
        ]:

            text = self.image_parser.extract_text(
                file_path
            )

        elif suffix == ".txt":

            text = self.text_parser.extract_text(
                file_path
            )

        else:

            raise ValueError(
                "Unsupported file type."
            )

        clean_text = self.cleaner.clean(
            text
        )

        chunks = self.chunker.chunk_text(
            clean_text
        )

        embeddings = self.embedder.embed(
            chunks
        )

        self.store.add_chunks(
            chunks
        )

        self.store.create_index(
            embeddings
        )

        self.store.save()

        return len(chunks)