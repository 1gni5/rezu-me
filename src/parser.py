from string import punctuation


class Parser:
    """Parse content and return a list of tags."""

    @staticmethod
    def from_text(text: str) -> set[str]:
        """Parse text and return a list of tags."""
        translation = text.maketrans(punctuation, " " * len(punctuation))
        return set(text.lower().translate(translation).split())
