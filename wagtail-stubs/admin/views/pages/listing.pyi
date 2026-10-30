from typing import Any, TypedDict

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponseBase
from django.utils.functional import cached_property as cached_property
from django_filters.filters import ChoiceFilter, DateFromToRangeFilter, ModelMultipleChoiceFilter
from wagtail import hooks as hooks
from wagtail.admin.filters import (
    DateRangePickerWidget as DateRangePickerWidget,
)
from wagtail.admin.filters import (
    MultipleContentTypeFilter as MultipleContentTypeFilter,
)
from wagtail.admin.filters import (
    MultipleUserFilter as MultipleUserFilter,
)
from wagtail.admin.filters import (
    WagtailFilterSet as WagtailFilterSet,
)
from wagtail.admin.ui.components import MediaContainer as MediaContainer
from wagtail.admin.ui.side_panels import PageStatusSidePanel as PageStatusSidePanel
from wagtail.admin.ui.tables import BaseColumn
from wagtail.admin.ui.tables import DateColumn as DateColumn
from wagtail.admin.ui.tables.pages import (
    BulkActionsColumn as BulkActionsColumn,
)
from wagtail.admin.ui.tables.pages import (
    NavigateToChildrenColumn as NavigateToChildrenColumn,
)
from wagtail.admin.ui.tables.pages import (
    PageStatusColumn as PageStatusColumn,
)
from wagtail.admin.ui.tables.pages import (
    PageTable as PageTable,
)
from wagtail.admin.ui.tables.pages import (
    PageTitleColumn as PageTitleColumn,
)
from wagtail.admin.ui.tables.pages import (
    PageTypeColumn as PageTypeColumn,
)
from wagtail.admin.ui.tables.pages import (
    ParentPageColumn as ParentPageColumn,
)
from wagtail.admin.views import generic as generic
from wagtail.admin.widgets.button import Button, HeaderButton
from wagtail.models import AbstractPage
from wagtail.models.i18n import Locale as Locale
from wagtail.models.pages import PageLogEntry as PageLogEntry
from wagtail.models.pages import PagePermissionTester as PagePermissionTester
from wagtail.models.pages import get_page_content_types as get_page_content_types
from wagtail.models.sites import Site as Site
from wagtail.permission_policies.pages import PagePermissionPolicy

Page: type[AbstractPage]

class PageTranslation(TypedDict):
    locale: Locale
    url: str

class SiteFilter(ModelMultipleChoiceFilter):
    def get_filter_predicate(self, v: Site) -> dict[str, str]: ...

class HasChildPagesFilter(ChoiceFilter):
    def filter(self, qs: QuerySet[AbstractPage], value: str) -> QuerySet[AbstractPage]: ...

class EditedByFilter(MultipleUserFilter):
    def filter(self, qs: QuerySet[AbstractPage], value: list[Any]) -> QuerySet[AbstractPage]: ...

class PageFilterSet(WagtailFilterSet):
    latest_revision_created_at: DateFromToRangeFilter
    owner: MultipleUserFilter
    edited_by: EditedByFilter
    site: SiteFilter
    has_child_pages: HasChildPagesFilter
    class Meta:
        model: type[AbstractPage]
        fields: list[str]

class GenericPageFilterSet(PageFilterSet):
    content_type: MultipleContentTypeFilter

class PageListingMixin:
    template_name: str
    context_object_name: str
    table_class = PageTable
    default_ordering: str | None
    model: type[AbstractPage]
    is_searchable: bool
    base_columns: list[BaseColumn]
    columns: list[BaseColumn]
    @cached_property
    def i18n_enabled(self) -> bool: ...
    @cached_property
    def show_locale_labels(self) -> bool: ...
    def get_valid_orderings(self) -> list[str]: ...
    def get_ordering(self) -> str | None: ...
    def annotate_queryset(self, pages: QuerySet[AbstractPage]) -> QuerySet[AbstractPage]: ...
    def order_queryset(self, queryset: QuerySet[AbstractPage]) -> QuerySet[AbstractPage]: ...
    def search_queryset(self, queryset: QuerySet[AbstractPage]) -> QuerySet[AbstractPage]: ...
    def get_table_kwargs(self) -> dict[str, Any]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class IndexView(PageListingMixin, generic.IndexView):
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[AbstractPage]: ...
    any_permission_required: set[str]
    template_name: str
    results_template_name: str
    paginate_by: int
    table_classname: str
    base_filterset_class = PageFilterSet
    base_columns: list[BaseColumn]
    @cached_property
    def columns(self) -> list[BaseColumn]: ...
    @cached_property
    def filterset_class(self) -> type[PageFilterSet]: ...
    def get_base_queryset(self) -> QuerySet[AbstractPage]: ...

class ExplorableIndexView(IndexView):
    template_name: str
    results_template_name: str
    index_url_name: str
    index_results_url_name: str
    page_title: str
    base_filterset_class = GenericPageFilterSet
    sort_order_field: str
    add_item_label: str
    add_url_name: str
    reorder_button: None
    base_columns: list[BaseColumn]
    parent_page: AbstractPage
    permissions: PagePermissionTester
    scheduled_page: AbstractPage | None
    @cached_property
    def locale(self) -> Locale | None: ...
    @cached_property
    def translations(self) -> list[PageTranslation]: ...
    @cached_property
    def explorable_columns(self) -> list[BaseColumn]: ...
    def get_table(self, object_list: QuerySet[AbstractPage]) -> PageTable: ...
    def get(self, request: HttpRequest, parent_page_id: int | None = None) -> HttpResponseBase: ...
    @cached_property
    def is_searching_whole_tree(self) -> bool: ...
    @cached_property
    def show_locale_labels(self) -> bool: ...
    @cached_property
    def add_button(self) -> HeaderButton | None: ...
    @cached_property
    def header_more_buttons(self) -> list[Button]: ...
    def get_base_queryset(self) -> QuerySet[AbstractPage]: ...
    def search_queryset(self, queryset: QuerySet[AbstractPage]) -> QuerySet[AbstractPage]: ...
    def get_index_url(self) -> str: ...
    def get_index_results_url(self) -> str: ...
    def get_add_url(self) -> str | None: ...
    def get_history_url(self) -> str | None: ...
    def get_reorder_url(self) -> str: ...
    def get_table_kwargs(self) -> dict[str, Any]: ...
    def get_ordering(self) -> str | None: ...
    def get_page_subtitle(self) -> str: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_side_panels(self) -> MediaContainer: ...
    def get_translations(self) -> list[PageTranslation]: ...
