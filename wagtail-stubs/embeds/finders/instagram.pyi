from wagtail.embeds.exceptions import EmbedException as EmbedException
from wagtail.embeds.exceptions import EmbedNotFoundException as EmbedNotFoundException

from .oembed import OEmbedFinder as OEmbedFinder

class AccessDeniedInstagramOEmbedException(EmbedException): ...

INSTAGRAM_PROVIDER: dict[str, str | list[str]]

class InstagramOEmbedFinder(OEmbedFinder):
    app_id: str | None
    app_secret: str | None
    omitscript: bool
    def __init__(self, omitscript: bool = False, app_id: str | None = None, app_secret: str | None = None) -> None: ...
    def find_embed(self, url, max_width=None, max_height=None): ...

embed_finder_class = InstagramOEmbedFinder
