from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseBase
from django.utils.functional import cached_property as cached_property, classproperty
from wagtail.admin.ui.tables import BaseColumn
from wagtail.admin.views import generic as generic
from wagtail.admin.views.generic.base import BaseListingView as BaseListingView
from wagtail.admin.views.generic.permissions import PermissionCheckedMixin as PermissionCheckedMixin
from wagtail.admin.views.pages.listing import PageFilterSet as PageFilterSet, PageListingMixin as PageListingMixin
from wagtail.admin.views.pages.utils import GenericPageBreadcrumbsMixin as GenericPageBreadcrumbsMixin
from wagtail.models import Page as Page
from wagtail.permissions import page_permission_policy as page_permission_policy

class ContentTypeUseView(PageListingMixin, PermissionCheckedMixin, BaseListingView):
    permission_policy = page_permission_policy
    any_permission_required: set[str]
    index_url_name: str
    index_results_url_name: str
    page_title: str
    header_icon: str
    paginate_by: int
    filterset_class = PageFilterSet
    @classproperty
    def columns(cls) -> list[BaseColumn]: ...
    page_class: type[Page]
    def get(self, request: HttpRequest, *, content_type_app_name: str, content_type_model_name: str) -> HttpResponse: ...
    def get_page_subtitle(self) -> str: ...
    @cached_property
    def verbose_name_plural(self) -> str: ...
    def get_base_queryset(self) -> QuerySet[Page]: ...
    def get_index_url(self) -> str: ...
    def get_index_results_url(self) -> str: ...
    def get_breadcrumbs_items(self) -> list[dict[str, str]]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class UsageView(GenericPageBreadcrumbsMixin, generic.UsageView):
    model = Page
    pk_url_kwarg: str
    header_icon: str
    usage_url_name: str
    edit_url_name: str
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
