from pathlib import Path


class TextParser:
    """
    Reads text files and returns their content.
    """

    def extract_text(self, file_path):
        """
        Read a text file and return its contents.

        Parameters
        ----------
        file_path : str or Path
            Path of the text file.

        Returns
        -------
        str
            Text inside the file.
        """

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        if file_path.suffix.lower() != ".txt":
            raise ValueError(
                f"Expected a .txt file, got: {file_path.suffix}"
            )

        with open(
            file_path,
            mode="r",
            encoding="utf-8",
        ) as file:

            text = file.read()

        return text