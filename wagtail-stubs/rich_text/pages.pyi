from collections.abc import Generator

from django.db.models import Model

from wagtail.models import Page  # type: ignore[import-untyped]
from wagtail.rich_text import LinkHandler

class PageLinkHandler(LinkHandler):
    identifier: str
    @staticmethod
    def get_model() -> type[Page]: ...
    @classmethod
    def get_many(cls, attrs_list: list[dict[str, str]]) -> list[Model | None]: ...
    @classmethod
    def expand_db_attributes(cls, attrs: dict[str, str]) -> str: ...
    @classmethod
    def expand_db_attributes_many(cls, attrs_list: list[dict[str, str]]) -> list[str]: ...
    @classmethod
    def extract_references(cls, attrs: dict[str, str]) -> Generator[tuple[type[Page], str, str, str], None, None]: ...
