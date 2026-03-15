from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponseBase
from django.utils.functional import cached_property as cached_property
from django.utils.functional import classproperty
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
from wagtail.models import (
    Locale,
)
from wagtail.models import (
    Page as Page,
)
from wagtail.models import (
    PageLogEntry as PageLogEntry,
)
from wagtail.models import (
    Site as Site,
)
from wagtail.models import (
    get_page_content_types as get_page_content_types,
)
from wagtail.permissions import page_permission_policy as page_permission_policy

class SiteFilter(ModelMultipleChoiceFilter):
    def get_filter_predicate(self, v: Site) -> dict[str, str]: ...

class HasChildPagesFilter(ChoiceFilter):
    def filter(self, qs: QuerySet[Page], value: str) -> QuerySet[Page]: ...

class EditedByFilter(MultipleUserFilter):
    def filter(self, qs: QuerySet[Page], value: list[Any]) -> QuerySet[Page]: ...

class PageFilterSet(WagtailFilterSet):
    latest_revision_created_at: DateFromToRangeFilter
    owner: MultipleUserFilter
    edited_by: EditedByFilter
    site: SiteFilter
    has_child_pages: HasChildPagesFilter
    class Meta:
        model = Page
        fields: list[str]

class GenericPageFilterSet(PageFilterSet):
    content_type: MultipleContentTypeFilter

class PageListingMixin:
    template_name: str
    context_object_name: str
    table_class = PageTable
    filterset_class = GenericPageFilterSet
    default_ordering: str
    model = Page
    is_searchable: bool
    columns: list[BaseColumn]
    @cached_property
    def i18n_enabled(self) -> bool: ...
    @cached_property
    def show_locale_labels(self) -> bool: ...
    def get_valid_orderings(self) -> list[str]: ...
    def get_ordering(self) -> str | None: ...
    def annotate_queryset(self, pages: QuerySet[Page]) -> QuerySet[Page]: ...
    def order_queryset(self, queryset: QuerySet[Page]) -> QuerySet[Page]: ...
    def search_queryset(self, queryset: QuerySet[Page]) -> QuerySet[Page]: ...
    def get_table_kwargs(self) -> dict[str, Any]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class IndexView(PageListingMixin, generic.IndexView):
    permission_policy = page_permission_policy
    any_permission_required: set[str]
    template_name: str
    results_template_name: str
    paginate_by: int
    table_classname: str
    filterset_class = PageFilterSet
    @classproperty
    def columns(cls) -> list[BaseColumn]: ...
    def get_base_queryset(self) -> QuerySet[Page]: ...

class ExplorableIndexView(IndexView):
    template_name: str
    results_template_name: str
    index_url_name: str
    index_results_url_name: str
    page_title: str
    filterset_class = GenericPageFilterSet
    sort_order_field: str
    @classproperty
    def columns(cls) -> list[BaseColumn]: ...
    parent_page: Page
    scheduled_page: Page | None
    locale: Locale | None
    translations: list[dict[str, Any]]
    def get(self, request: HttpRequest, parent_page_id: int | None = None) -> HttpResponseBase: ...
    @cached_property
    def is_searching_whole_tree(self) -> bool: ...
    @cached_property
    def show_locale_labels(self) -> bool: ...
    def get_base_queryset(self) -> QuerySet[Page]: ...
    def search_queryset(self, queryset: QuerySet[Page]) -> QuerySet[Page]: ...
    def get_index_url(self) -> str: ...
    def get_index_results_url(self) -> str: ...
    def get_history_url(self) -> str | None: ...
    def get_reorder_url(self) -> str: ...
    def get_table_kwargs(self) -> dict[str, Any]: ...
    def get_ordering(self) -> str | None: ...
    def get_page_subtitle(self) -> str: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_side_panels(self) -> MediaContainer: ...
    def get_translations(self) -> list[dict[str, Any]]: ...
