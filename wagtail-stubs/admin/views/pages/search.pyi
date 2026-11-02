from typing import Any

from django.contrib.contenttypes.models import ContentType
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.utils.functional import _StrOrPromise, cached_property, classproperty
from wagtail.admin.ui.tables import BaseColumn
from wagtail.admin.ui.tables.pages import NavigateToChildrenColumn as NavigateToChildrenColumn
from wagtail.admin.views.generic.base import BaseListingView as BaseListingView
from wagtail.admin.views.generic.permissions import PermissionCheckedMixin as PermissionCheckedMixin
from wagtail.admin.views.pages.listing import PageListingMixin as PageListingMixin
from wagtail.models import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy
from wagtail.search.query import MATCH_ALL as MATCH_ALL
from wagtail.search.utils import parse_query_string as parse_query_string

Page: type[AbstractPage]

def page_filter_search(
    q: str, pages: QuerySet[AbstractPage], all_pages: QuerySet[AbstractPage] | None = None, ordering: str | None = None
) -> tuple[QuerySet[AbstractPage], QuerySet[AbstractPage] | None]: ...

class SearchView(PageListingMixin[AbstractPage], PermissionCheckedMixin[AbstractPage], BaseListingView[AbstractPage]):
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[AbstractPage]: ...
    any_permission_required: set[str]
    paginate_by: int
    page_title: _StrOrPromise
    header_icon: str
    index_url_name: str
    index_results_url_name: str
    is_searchable: bool
    is_searching: bool
    filterset_class: None
    template_name: str
    results_template_name: str
    @classproperty
    def columns(cls) -> list[BaseColumn]: ...
    content_types: list[tuple[ContentType, int]]
    @cached_property
    def ordering(self) -> str | None: ...
    selected_content_type: ContentType | None
    def get(self, request: HttpRequest) -> HttpResponse: ...
    def get_queryset(self) -> QuerySet[AbstractPage]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
