from .base import EmbedFinder as EmbedFinder
from _typeshed import Incomplete
from wagtail.embeds.exceptions import EmbedNotFoundException as EmbedNotFoundException
from wagtail.embeds.oembed_providers import all_providers as all_providers

class OEmbedFinder(EmbedFinder):
    options: Incomplete
    def __init__(self, providers=None, options=None) -> None: ...
    def accept(self, url): ...
    def find_embed(self, url, max_width=None, max_height=None): ...
embed_finder_class = OEmbedFinder
