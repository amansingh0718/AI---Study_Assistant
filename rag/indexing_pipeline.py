from pathlib import Path

from parsers.pdf_parser import PDFParser
from parsers.image_parser import ImageParser
from parsers.text_parser import TextParser

from processing.cleaner import TextCleaner
from processing.chunker import TextChunker

from embeddings.embedder import TextEmbedder

from vector_store.faiss_store import FAISSStore

from storage.document_store import DocumentStore


class IndexingPipeline:
    """
    Creates a searchable FAISS index from a document.
    """

    def __init__(self):

        self.pdf_parser = PDFParser()

        self.image_parser = ImageParser()

        self.text_parser = TextParser()

        self.cleaner = TextCleaner()

        self.chunker = TextChunker()

        self.embedder = TextEmbedder()

        self.store = FAISSStore()

        self.document_store = DocumentStore("storage")

    def index_document(
        self,
        file_path,
    ):
        path = Path(file_path)

        suffix = path.suffix.lower()

        print("\n" + "=" * 60)
        print("STEP 1 : Detect File Type")
        print("=" * 60)

        if suffix == ".pdf":

            print("PDF detected")

            text = self.pdf_parser.extract_text(
                file_path
            )

        elif suffix in [
            ".png",
            ".jpg",
            ".jpeg",
        ]:

            print("Image detected")

            text = self.image_parser.extract_text(
                file_path
            )

        elif suffix == ".txt":

            print("Text file detected")

            text = self.text_parser.extract_text(
                file_path
            )

        else:

            raise ValueError(
                "Unsupported file type."
            )

        print("\nSTEP 2 : Extracted Text")
        print("-" * 40)
        print("Length :", len(text))
        print("Preview:")
        print(repr(text[:300]))

        clean_text = self.cleaner.clean(text)

        print("\nSTEP 3 : Cleaned Text")
        print("-" * 40)
        print("Length :", len(clean_text))
        print("Preview:")
        print(repr(clean_text[:300]))

        self.document_store.save(clean_text)

        chunks = self.chunker.chunk_text(
            clean_text
        )

        print("\nSTEP 4 : Chunking")
        print("-" * 40)
        print("Total Chunks :", len(chunks))

        if len(chunks) > 0:
            print("\nFirst Chunk:")
            print(chunks[0][:300])

        embeddings = self.embedder.embed(
            chunks
        )

        print("\nSTEP 5 : Embeddings")
        print("-" * 40)
        print("Type :", type(embeddings))

        try:
            print("Shape :", embeddings.shape)
        except Exception as e:
            print("Shape Error :", e)

        self.store.add_chunks(
            chunks
        )

        print("\nSTEP 6 : Creating FAISS Index")

        self.store.create_index(
            embeddings
        )

        print("FAISS Index Created Successfully")

        self.store.save()

        print("FAISS Index Saved Successfully")

        print("=" * 60)
        print("INDEXING COMPLETED")
        print("=" * 60)

        return len(chunks)