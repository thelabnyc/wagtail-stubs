from typing_extensions import TypeVar
from wagtail.admin import messages as messages
from wagtail.admin.action_menu import PageActionMenu as PageActionMenu
from wagtail.admin.auth import (
    user_has_any_page_permission as user_has_any_page_permission,
)
from wagtail.admin.auth import (
    user_passes_test as user_passes_test,
)
from wagtail.admin.views.generic.models import (
    RevisionsCompareView as GenericRevisionsCompareView,
)
from wagtail.admin.views.generic.models import (
    RevisionsUnscheduleView as GenericRevisionsUnscheduleView,
)
from wagtail.admin.views.generic.preview import PreviewRevision as PreviewRevision
from wagtail.admin.views.pages.edit import EditView as EditView
from wagtail.admin.views.pages.utils import GenericPageBreadcrumbsMixin as GenericPageBreadcrumbsMixin
from wagtail.models import AbstractPage
from wagtail.utils.timestamps import render_timestamp as render_timestamp

Page: type[AbstractPage]
_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

def revisions_index(request, page_id): ...

class RevisionsRevertView(EditView[_PageT]):
    revisions_revert_url_name: str
    def get_action_menu(self): ...
    def get(self, request, *args, **kwargs): ...
    def get_object(self) -> _PageT: ...
    def get_revisions_revert_url(self): ...
    def get_warning_message(self): ...
    def get_context_data(self, **kwargs): ...

class RevisionsView(PreviewRevision[_PageT]):
    model: type[_PageT]
    def setup(self, request, page_id, revision_id, *args, **kwargs): ...
    def get_object(self) -> _PageT: ...

class RevisionsCompareView(GenericPageBreadcrumbsMixin, GenericRevisionsCompareView[_PageT]):
    history_url_name: str
    edit_url_name: str
    header_icon: str
    breadcrumbs_items_to_take: int
    def dispatch(self, request, *args, **kwargs): ...
    def get_object(self, queryset=None) -> _PageT: ...
    def get_edit_handler(self): ...
    def get_page_subtitle(self): ...

class RevisionsUnscheduleView(GenericRevisionsUnscheduleView[_PageT]):
    model: type[_PageT]
    edit_url_name: str
    history_url_name: str
    revisions_unschedule_url_name: str
    header_icon: str
    def setup(self, request, page_id, revision_id, *args, **kwargs): ...
    def get_object(self, queryset=None) -> _PageT: ...
    def get_object_display_title(self): ...
