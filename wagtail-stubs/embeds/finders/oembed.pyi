from typing import Any

from .base import EmbedFinder as EmbedFinder
from wagtail.embeds.exceptions import EmbedNotFoundException as EmbedNotFoundException
from wagtail.embeds.oembed_providers import all_providers as all_providers

class OEmbedFinder(EmbedFinder):
    options: dict[str, Any]
    def __init__(self, providers: list[dict[str, Any]] | None = None, options: dict[str, Any] | None = None) -> None: ...
    def accept(self, url: str) -> bool: ...
    def find_embed(self, url: str, max_width: int | None = None, max_height: int | None = None) -> dict[str, Any]: ...
embed_finder_class = OEmbedFinder
