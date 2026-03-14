from _typeshed import Incomplete
from wagtail.admin.rich_text.converters.html_to_contentstate import LinkElementHandler as LinkElementHandler
from wagtail.documents import get_document_model as get_document_model

def document_link_entity(props): ...

class DocumentLinkElementHandler(LinkElementHandler):
    def get_attribute_data(self, attrs): ...

ContentstateDocumentLinkConversionRule: Incomplete
