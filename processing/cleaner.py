import re


class TextCleaner:
    """
    Cleans extracted text while preserving its meaning.
    """

    def clean(self, text):
        """
        Clean extracted text.

        Parameters
        ----------
        text : str

        Returns
        -------
        str
        """

        if not isinstance(text, str):
            raise TypeError(
                "Input text must be a string."
            )

        text = self.remove_extra_spaces(text)

        text = self.remove_extra_blank_lines(text)

        text = text.strip()

        return text

    def remove_extra_spaces(self, text):
        """
        Replace multiple spaces/tabs with a single space.
        """

        text = re.sub(
            r"[ \t]+",
            " ",
            text,
        )

        return text

    def remove_extra_blank_lines(self, text):
        """
        Replace multiple blank lines with a single blank line.
        """

        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text,
        )

        return text