from wagtail.embeds import format as format
from wagtail.embeds.embeds import get_embed as get_embed
from wagtail.embeds.models import Embed as Embed
from wagtail.rich_text import EmbedHandler as EmbedHandler

class MediaEmbedHandler(EmbedHandler):
    identifier: str
    @staticmethod
    def get_model(): ...
    @staticmethod
    def get_instance(attrs): ...
    @staticmethod
    def expand_db_attributes(attrs: dict) -> str: ...
