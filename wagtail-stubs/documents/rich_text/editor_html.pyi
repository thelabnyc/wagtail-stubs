from collections.abc import Mapping

from wagtail.admin.rich_text.converters.editor_html import LinkTypeRule
from wagtail.documents import get_document_model as get_document_model

class DocumentLinkHandler:
    @staticmethod
    def get_db_attributes(tag: Mapping[str, str]) -> dict[str, str]: ...
    @staticmethod
    def expand_db_attributes(attrs: dict[str, str]) -> str: ...

EditorHTMLDocumentLinkConversionRule: list[LinkTypeRule]
