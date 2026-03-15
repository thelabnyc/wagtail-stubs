import datetime

from wagtail.embeds.exceptions import EmbedException as EmbedException
from wagtail.embeds.exceptions import EmbedNotFoundException as EmbedNotFoundException

from .base import EmbedFinder as EmbedFinder

class EmbedlyException(EmbedException): ...
class AccessDeniedEmbedlyException(EmbedlyException): ...

class EmbedlyFinder(EmbedFinder):
    key: str | None
    def __init__(self, key: str | None = None) -> None: ...
    def get_key(self) -> str | None: ...
    def accept(self, url: str) -> bool: ...
    def find_embed(
        self, url: str, max_width: int | None = None, key: str | None = None
    ) -> dict[str, str | int | datetime.datetime | None]: ...

embed_finder_class = EmbedlyFinder
