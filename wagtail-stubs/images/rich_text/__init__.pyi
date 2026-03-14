from collections.abc import Generator
from wagtail.images import get_image_model as get_image_model
from wagtail.images.formats import get_image_format as get_image_format
from wagtail.rich_text import EmbedHandler as EmbedHandler

class ImageEmbedHandler(EmbedHandler):
    identifier: str
    @staticmethod
    def get_model(): ...
    @classmethod
    def expand_db_attributes(cls, attrs: dict) -> str: ...
    @classmethod
    def expand_db_attributes_many(cls, attrs_list: list[dict]) -> list[str]: ...
    @classmethod
    def extract_references(cls, attrs) -> Generator[tuple[type, str, str, str]]: ...
