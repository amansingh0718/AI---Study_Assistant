from pathlib import Path

import fitz


class PDFParser:
    """
    Reads PDF files and extracts text from all pages.
    """

    def extract_text(self, file_path):
        """
        Extract text from a PDF file.

        Parameters
        ----------
        file_path : str or Path
            Path of the PDF.

        Returns
        -------
        str
            Complete text from all pages.
        """

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        if file_path.suffix.lower() != ".pdf":
            raise ValueError(
                f"Expected a .pdf file, got: {file_path.suffix}"
            )

        document = fitz.open(file_path)

        pages = []

        for page in document:
            pages.append(page.get_text())

        document.close()

        return "\n".join(pages)