import datetime

from wagtail.embeds.exceptions import EmbedNotFoundException as EmbedNotFoundException
from wagtail.embeds.oembed_providers import all_providers as all_providers

from .base import EmbedFinder as EmbedFinder

class OEmbedFinder(EmbedFinder):
    options: dict[str, str | int]
    def __init__(
        self, providers: list[dict[str, str | list[str]]] | None = None, options: dict[str, str | int] | None = None
    ) -> None: ...
    def accept(self, url: str) -> bool: ...
    def find_embed(
        self, url: str, max_width: int | None = None, max_height: int | None = None
    ) -> dict[str, str | int | datetime.datetime | None]: ...

embed_finder_class = OEmbedFinder
