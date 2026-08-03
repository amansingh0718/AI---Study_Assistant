import requests

from config import (
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
)


class OllamaClient:
    """
    Sends prompts to Ollama and returns responses.
    """

    def generate(self, prompt):
        """
        Generate a response from Ollama.

        Parameters
        ----------
        prompt : str

        Returns
        -------
        str
        """

        if not isinstance(prompt, str):
            raise TypeError(
                "Prompt must be a string."
            )

        if len(prompt.strip()) == 0:
            raise ValueError(
                "Prompt cannot be empty."
            )

        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
            },
            timeout=300,
        )

        print("=" * 100)
        print(response)
        print("=" * 100)

        response.raise_for_status()

        data = response.json()

        return data["response"]