from typing import Any

from wagtail.admin.rich_text.converters import editor_html as editor_html
from wagtail.documents import get_document_model as get_document_model

class DocumentLinkHandler:
    @staticmethod
    def get_db_attributes(tag: Any) -> dict[str, Any]: ...
    @staticmethod
    def expand_db_attributes(attrs: dict[str, Any]) -> str: ...

EditorHTMLDocumentLinkConversionRule: list[Any]
