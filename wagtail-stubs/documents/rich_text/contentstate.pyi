from typing import Any

from wagtail.admin.rich_text.converters.html_to_contentstate import LinkElementHandler as LinkElementHandler
from wagtail.documents import get_document_model as get_document_model

def document_link_entity(props: dict[str, Any]) -> Any: ...

class DocumentLinkElementHandler(LinkElementHandler):
    def get_attribute_data(self, attrs: dict[str, str]) -> dict[str, Any]: ...

ContentstateDocumentLinkConversionRule: dict[str, dict[str, Any]]
