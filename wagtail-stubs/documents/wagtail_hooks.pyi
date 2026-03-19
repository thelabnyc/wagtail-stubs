from wagtail import hooks as hooks
from wagtail.admin.admin_url_finder import (
    ModelAdminURLFinder as ModelAdminURLFinder,
)
from wagtail.admin.admin_url_finder import (
    register_admin_url_finder as register_admin_url_finder,
)
from wagtail.admin.menu import MenuItem as MenuItem
from wagtail.admin.navigation import get_site_for_user as get_site_for_user
from wagtail.admin.search import SearchArea as SearchArea
from wagtail.admin.site_summary import SummaryItem as SummaryItem
from wagtail.documents import admin_urls as admin_urls
from wagtail.documents import get_document_model as get_document_model
from wagtail.documents.api.admin.views import DocumentsAdminAPIViewSet as DocumentsAdminAPIViewSet
from wagtail.documents.forms import GroupDocumentPermissionFormSet as GroupDocumentPermissionFormSet
from wagtail.documents.permissions import permission_policy as permission_policy
from wagtail.documents.rich_text import DocumentLinkHandler as DocumentLinkHandler
from wagtail.documents.rich_text.contentstate import (
    ContentstateDocumentLinkConversionRule as ContentstateDocumentLinkConversionRule,
)
from wagtail.documents.rich_text.editor_html import (
    EditorHTMLDocumentLinkConversionRule as EditorHTMLDocumentLinkConversionRule,
)
from wagtail.documents.views.bulk_actions import (
    AddTagsBulkAction as AddTagsBulkAction,
)
from wagtail.documents.views.bulk_actions import (
    AddToCollectionBulkAction as AddToCollectionBulkAction,
)
from wagtail.documents.views.bulk_actions import (
    DeleteBulkAction as DeleteBulkAction,
)
from wagtail.models.view_restrictions import BaseViewRestriction as BaseViewRestriction
from wagtail.wagtail_hooks import require_wagtail_login as require_wagtail_login

def register_admin_urls(): ...
def construct_admin_api(router) -> None: ...

class DocumentsMenuItem(MenuItem):
    def is_shown(self, request): ...

def register_documents_menu_item(): ...
def register_document_feature(features) -> None: ...

class DocumentsSummaryItem(SummaryItem):
    order: int
    template_name: str
    def get_context_data(self, parent_context): ...
    def is_shown(self): ...

def add_documents_summary_item(request, items) -> None: ...

class DocsSearchArea(SearchArea):
    def is_shown(self, request): ...

def register_documents_search_area(): ...
def register_document_permissions_panel(): ...
def describe_collection_docs(collection): ...
def check_view_restrictions(document, request): ...

class DocumentAdminURLFinder(ModelAdminURLFinder):
    edit_url_name: str
    permission_policy = permission_policy

def register_document_chooser_viewset(): ...
