from .oembed import OEmbedFinder as OEmbedFinder
from _typeshed import Incomplete
from wagtail.embeds.exceptions import EmbedException as EmbedException, EmbedNotFoundException as EmbedNotFoundException

class AccessDeniedFacebookOEmbedException(EmbedException): ...

FACEBOOK_PROVIDERS: Incomplete

class FacebookOEmbedFinder(OEmbedFinder):
    app_id: Incomplete
    app_secret: Incomplete
    omitscript: Incomplete
    def __init__(self, omitscript: bool = False, app_id=None, app_secret=None) -> None: ...
    def find_embed(self, url, max_width=None, max_height=None): ...
embed_finder_class = FacebookOEmbedFinder
