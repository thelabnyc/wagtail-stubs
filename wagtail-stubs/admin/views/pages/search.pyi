from typing import Any

from django.contrib.contenttypes.models import ContentType
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.utils.functional import classproperty
from wagtail.admin.ui.tables import BaseColumn
from wagtail.admin.ui.tables.pages import NavigateToChildrenColumn as NavigateToChildrenColumn
from wagtail.admin.views.generic.base import BaseListingView as BaseListingView
from wagtail.admin.views.generic.permissions import PermissionCheckedMixin as PermissionCheckedMixin
from wagtail.admin.views.pages.listing import PageListingMixin as PageListingMixin
from wagtail.models.pages import Page as Page
from wagtail.permissions import page_permission_policy as page_permission_policy
from wagtail.search.query import MATCH_ALL as MATCH_ALL
from wagtail.search.utils import parse_query_string as parse_query_string

def page_filter_search(
    q: str, pages: QuerySet[Page], all_pages: QuerySet[Page] | None = None, ordering: str | None = None
) -> tuple[QuerySet[Page], QuerySet[Page] | None]: ...

class SearchView(PageListingMixin, PermissionCheckedMixin, BaseListingView):
    permission_policy = page_permission_policy
    any_permission_required: set[str]
    paginate_by: int
    page_title: str
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
    ordering: str | None
    selected_content_type: ContentType | None
    def get(self, request: HttpRequest) -> HttpResponse: ...
    def get_queryset(self) -> QuerySet[Page]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
