from _typeshed import Incomplete
from wagtail.admin.rich_text.converters import editor_html as editor_html
from wagtail.documents import get_document_model as get_document_model

class DocumentLinkHandler:
    @staticmethod
    def get_db_attributes(tag): ...
    @staticmethod
    def expand_db_attributes(attrs): ...

EditorHTMLDocumentLinkConversionRule: Incomplete
