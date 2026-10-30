from typing import Generic

from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.admin.views.generic import history as history
from wagtail.admin.views.pages.utils import GenericPageBreadcrumbsMixin as GenericPageBreadcrumbsMixin
from wagtail.admin.widgets import BooleanRadioSelect as BooleanRadioSelect
from wagtail.models import AbstractPage
from wagtail.models.pages import PageLogEntry as PageLogEntry
from wagtail.permission_policies.pages import PagePermissionPolicy
import django_filters

Page: type[AbstractPage]
_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

class PageHistoryFilterSet(history.HistoryFilterSet):
    is_commenting_action: django_filters.BooleanFilter
    def filter_is_commenting_action(self, queryset, name, value): ...

class PageWorkflowHistoryViewMixin(Generic[_PageT]):
    model: type[_PageT]
    pk_url_kwarg: str
    edit_url_name: str
    def dispatch(self, request, *args, **kwargs): ...
    def get_context_data(self, **kwargs): ...

class WorkflowHistoryView(
    PageWorkflowHistoryViewMixin[_PageT], GenericPageBreadcrumbsMixin, history.WorkflowHistoryView[_PageT]
):
    header_icon: str
    workflow_history_detail_url_name: str

class WorkflowHistoryDetailView(
    PageWorkflowHistoryViewMixin[_PageT], GenericPageBreadcrumbsMixin, history.WorkflowHistoryDetailView[_PageT]
):
    header_icon: str
    workflow_history_url_name: str
    breadcrumbs_items_to_take: int

class PageHistoryView(GenericPageBreadcrumbsMixin, history.HistoryView[_PageT]):
    template_name: str
    filterset_class = PageHistoryFilterSet
    model: type[_PageT]
    pk_url_kwarg: str
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[AbstractPage]: ...
    any_permission_required: list[str]
    history_url_name: str
    history_results_url_name: str
    edit_url_name: str
    revisions_view_url_name: str
    revisions_revert_url_name: str
    revisions_compare_url_name: str
    revisions_unschedule_url_name: str
    def get_object(self) -> _PageT: ...
    def get_page_subtitle(self): ...
    def user_can_unschedule(self): ...
    def get_base_queryset(self): ...
