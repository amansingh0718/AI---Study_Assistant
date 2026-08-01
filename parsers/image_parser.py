from pathlib import Path

from PIL import Image
import pytesseract

from config import TESSERACT_LANGUAGE


class ImageParser:
    """
    Reads image files and extracts text using OCR.
    """

    def extract_text(self, file_path):
        """
        Extract text from an image.

        Parameters
        ----------
        file_path : str or Path
            Path of the image.

        Returns
        -------
        str
            Text extracted from the image.
        """

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        supported_extensions = {
            ".png",
            ".jpg",
            ".jpeg",
        }

        if file_path.suffix.lower() not in supported_extensions:
            raise ValueError(
                f"Unsupported image type: {file_path.suffix}"
            )

        image = Image.open(file_path)

        text = pytesseract.image_to_string(
            image,
            lang=TESSERACT_LANGUAGE,
        )

        image.close()

        return text