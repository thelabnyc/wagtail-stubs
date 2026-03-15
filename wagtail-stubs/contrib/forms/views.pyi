from _typeshed import Incomplete
from django.utils.functional import classproperty
from django.views.generic import TemplateView
from wagtail.admin import messages as messages
from wagtail.admin.filters import (
    DateRangePickerWidget as DateRangePickerWidget,
)
from wagtail.admin.filters import (
    MultipleContentTypeFilter as MultipleContentTypeFilter,
)
from wagtail.admin.filters import (
    WagtailFilterSet as WagtailFilterSet,
)
from wagtail.admin.ui.tables import Column as Column
from wagtail.admin.ui.tables import TitleColumn as TitleColumn
from wagtail.admin.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.admin.views.generic import PermissionCheckedMixin as PermissionCheckedMixin
from wagtail.admin.views.generic.base import BaseListingView as BaseListingView
from wagtail.admin.views.mixins import SpreadsheetExportMixin as SpreadsheetExportMixin
from wagtail.admin.views.pages.listing import PageFilterSet as PageFilterSet
from wagtail.admin.views.pages.listing import PageListingMixin as PageListingMixin
from wagtail.contrib.forms.models import FormMixin as FormMixin
from wagtail.contrib.forms.utils import get_form_types as get_form_types
from wagtail.contrib.forms.utils import get_forms_for_user as get_forms_for_user
from wagtail.models import Page as Page
from wagtail.permissions import page_permission_policy as page_permission_policy

def get_submissions_list_view(request, *args, **kwargs): ...

class ContentTypeColumn(Column):
    edit_url_name: str
    cell_template_name: str
    def get_url(self, instance): ...
    def get_cell_context_data(self, instance, parent_context): ...

class FormPageFilterSet(PageFilterSet):
    content_type: Incomplete

class FormPagesListView(PageListingMixin, PermissionCheckedMixin, BaseListingView):
    permission_policy = page_permission_policy
    any_permission_required: Incomplete
    template_name: str
    results_template_name: str
    context_object_name: str
    paginate_by: int
    page_kwarg: str
    index_url_name: str
    index_results_url_name: str
    page_title: Incomplete
    header_icon: str
    model = Page
    is_searchable: bool
    filterset_class = FormPageFilterSet
    @classproperty
    def columns(self): ...
    def get_breadcrumbs_items(self): ...
    def get_base_queryset(self): ...

class DeleteSubmissionsView(TemplateView):
    template_name: str
    page: Incomplete
    submissions: Incomplete
    success_url_name: str
    def get_queryset(self): ...
    def handle_delete(self, submissions) -> None: ...
    def get_success_url(self): ...
    def dispatch(self, request, *args, **kwargs): ...
    def get_context_data(self, **kwargs): ...

class SubmissionsListFilterSet(WagtailFilterSet):
    date: Incomplete

class SubmissionsListView(SpreadsheetExportMixin, BaseListingView):
    template_name: str
    results_template_name: str
    context_object_name: str
    form_page: Incomplete
    default_ordering: Incomplete
    ordering_csv: Incomplete
    orderable_fields: Incomplete
    page_title: Incomplete
    header_icon: str
    paginate_by: int
    filterset_class = SubmissionsListFilterSet
    forms_index_url_name: str
    index_url_name: str
    index_results_url_name: str
    show_export_buttons: bool
    list_export: Incomplete
    export_headings: Incomplete
    def dispatch(self, request, *args, **kwargs): ...
    def get_filterset_kwargs(self): ...
    def get_base_queryset(self): ...
    def get_validated_ordering(self): ...
    def get_ordering(self): ...
    def get_filename(self): ...
    def render_to_response(self, context, **response_kwargs): ...
    def to_row_dict(self, item): ...
    def get_index_url(self): ...
    def get_index_results_url(self): ...
    def get_page_subtitle(self): ...
    def get_breadcrumbs_items(self): ...
    def get_context_data(self, **kwargs): ...
