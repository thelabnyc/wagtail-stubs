from collections.abc import Generator

from wagtail.models import AbstractPage
from wagtail.rich_text import LinkHandler

Page: type[AbstractPage]

class PageLinkHandler(LinkHandler):
    identifier: str
    @staticmethod
    def get_model() -> type[AbstractPage]: ...
    @classmethod
    def get_many(cls, attrs_list: list[dict[str, str]]) -> list[AbstractPage | None]: ...
    @classmethod
    def expand_db_attributes(cls, attrs: dict[str, str]) -> str: ...
    @classmethod
    def expand_db_attributes_many(cls, attrs_list: list[dict[str, str]]) -> list[str]: ...
    @classmethod
    def extract_references(cls, attrs: dict[str, str]) -> Generator[tuple[type[AbstractPage], str, str, str]]: ...
