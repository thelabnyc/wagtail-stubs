from _typeshed import Incomplete
from collections.abc import Generator
from wagtail.documents import get_document_model as get_document_model
from wagtail.rich_text import LinkHandler as LinkHandler

class DocumentLinkHandler(LinkHandler):
    identifier: str
    @staticmethod
    def get_model(): ...
    @classmethod
    def expand_db_attributes(cls, attrs: dict) -> str: ...
    @classmethod
    def expand_db_attributes_many(cls, attrs_list: list[dict]) -> list[str]: ...
    @classmethod
    def extract_references(cls, attrs) -> Generator[Incomplete]: ...
