from urllib.parse import urlparse


class Url:
    """
    A URL path and its parsed result.
    """

    def __init__(self, url: str | None) -> None:
        if not isinstance(url, str):
            raise TypeError("URL must be a string.")

        self._url = url
        self.parse = urlparse(url)  # ParseResult

    def __str__(self) -> str:
        return self._url

    def __repr__(self) -> str:
        return self._url

    @property
    def stem(self) -> str:
        """
        The final path element of the URL, excluding the extension.
        """

        s = self.__str__()
        parts: list[str] = s.split("/")
        stem = parts[-1]
        stem_parts: list[str] = stem.split(".")
        stem_final = stem_parts[0]
        return stem_final
