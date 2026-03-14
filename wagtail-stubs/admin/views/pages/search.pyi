from _typeshed import Incomplete
from django.db.models.query import QuerySet
from django.utils.functional import classproperty
from typing import Any
from wagtail.admin.ui.tables.pages import NavigateToChildrenColumn as NavigateToChildrenColumn
from wagtail.admin.views.generic.base import BaseListingView as BaseListingView
from wagtail.admin.views.generic.permissions import PermissionCheckedMixin as PermissionCheckedMixin
from wagtail.admin.views.pages.listing import PageListingMixin as PageListingMixin
from wagtail.models import Page as Page
from wagtail.permissions import page_permission_policy as page_permission_policy
from wagtail.search.query import MATCH_ALL as MATCH_ALL
from wagtail.search.utils import parse_query_string as parse_query_string

def page_filter_search(q, pages, all_pages=None, ordering=None): ...

class SearchView(PageListingMixin, PermissionCheckedMixin, BaseListingView):
    permission_policy = page_permission_policy
    any_permission_required: Incomplete
    paginate_by: int
    page_title: Incomplete
    header_icon: str
    index_url_name: str
    index_results_url_name: str
    is_searchable: bool
    is_searching: bool
    filterset_class: Incomplete
    template_name: str
    results_template_name: str
    @classproperty
    def columns(cls): ...
    content_types: Incomplete
    ordering: Incomplete
    selected_content_type: Incomplete
    def get(self, request): ...
    def get_queryset(self) -> QuerySet[Any]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
