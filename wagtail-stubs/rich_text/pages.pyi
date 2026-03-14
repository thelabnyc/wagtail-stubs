from _typeshed import Incomplete
from collections.abc import Generator
from django.db.models import Model
from wagtail.models import Page as Page
from wagtail.rich_text import LinkHandler as LinkHandler

class PageLinkHandler(LinkHandler):
    identifier: str
    @staticmethod
    def get_model(): ...
    @classmethod
    def get_many(cls, attrs_list: list[dict]) -> list[Model]: ...
    @classmethod
    def expand_db_attributes(cls, attrs: dict) -> str: ...
    @classmethod
    def expand_db_attributes_many(cls, attrs_list: list[dict]) -> list[str]: ...
    @classmethod
    def extract_references(self, attrs) -> Generator[Incomplete]: ...
