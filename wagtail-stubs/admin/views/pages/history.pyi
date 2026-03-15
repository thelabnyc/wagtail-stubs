from wagtail.admin.views.generic import history as history
from wagtail.admin.views.pages.utils import GenericPageBreadcrumbsMixin as GenericPageBreadcrumbsMixin
from wagtail.admin.widgets import BooleanRadioSelect as BooleanRadioSelect
from wagtail.models import Page as Page
from wagtail.models import PageLogEntry as PageLogEntry
from wagtail.permissions import page_permission_policy as page_permission_policy
import django_filters

class PageHistoryFilterSet(history.HistoryFilterSet):
    is_commenting_action: django_filters.BooleanFilter
    def filter_is_commenting_action(self, queryset, name, value): ...

class PageWorkflowHistoryViewMixin:
    model = Page
    pk_url_kwarg: str
    edit_url_name: str
    def dispatch(self, request, *args, **kwargs): ...
    def get_context_data(self, **kwargs): ...

class WorkflowHistoryView(PageWorkflowHistoryViewMixin, GenericPageBreadcrumbsMixin, history.WorkflowHistoryView):
    header_icon: str
    workflow_history_detail_url_name: str

class WorkflowHistoryDetailView(
    PageWorkflowHistoryViewMixin, GenericPageBreadcrumbsMixin, history.WorkflowHistoryDetailView
):
    header_icon: str
    workflow_history_url_name: str
    breadcrumbs_items_to_take: int

class PageHistoryView(GenericPageBreadcrumbsMixin, history.HistoryView):
    template_name: str
    filterset_class = PageHistoryFilterSet
    model = Page
    pk_url_kwarg: str
    permission_policy = page_permission_policy
    any_permission_required: set[str]
    history_url_name: str
    history_results_url_name: str
    edit_url_name: str
    revisions_view_url_name: str
    revisions_revert_url_name: str
    revisions_compare_url_name: str
    revisions_unschedule_url_name: str
    def get_object(self): ...
    def get_page_subtitle(self): ...
    def user_can_unschedule(self): ...
    def get_base_queryset(self): ...
