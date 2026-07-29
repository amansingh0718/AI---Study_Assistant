from pathlib import Path
import shutil

from config import (
    DATA_DIR,
    UPLOAD_DIR,
    FAISS_DIR,
    SUPPORTED_FILE_TYPES,
)


class FileLoader:
    """
    Handles file-related operations such as:

    1. Creating project folders
    2. Validating uploaded files
    3. Saving uploaded files
    """

    def __init__(self):
        self.create_project_folders()

    def create_project_folders(self):
        """
        Create required project folders if they don't already exist.
        """

        DATA_DIR.mkdir(exist_ok=True)

        UPLOAD_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        FAISS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    def is_supported_file(self, filename: str) -> bool:
        """
        Check whether the uploaded file type is supported.
        """

        extension = Path(filename).suffix.lower()

        return extension in SUPPORTED_FILE_TYPES

    def save_uploaded_file(self, uploaded_file):
        """
        Save uploaded Streamlit file into uploads folder.

        Returns
        -------
        Path
            Path of saved file.
        """

        if not self.is_supported_file(uploaded_file.name):
            raise ValueError(
                f"Unsupported file type: {uploaded_file.name}"
            )

        destination = UPLOAD_DIR / uploaded_file.name

        with open(destination, "wb") as file:
            shutil.copyfileobj(uploaded_file, file)

        return destination