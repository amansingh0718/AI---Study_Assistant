from pathlib import Path


class DocumentStore:
    """
    Saves and loads the cleaned document.
    """

    def __init__(self, storage_dir):
        self.file_path = Path(storage_dir) / "document.txt"

    def save(self, text):
        """
        Save the cleaned document.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(text)

    def load(self):
        """
        Load the cleaned document.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(
                "Document not found."
            )

        with open(
            self.file_path,
            "r",
            encoding="utf-8",
        ) as file:

            return file.read()