from _typeshed import Incomplete
from django.utils.functional import cached_property as cached_property, classproperty
from typing import Any
from wagtail.admin.views import generic as generic
from wagtail.admin.views.generic.base import BaseListingView as BaseListingView
from wagtail.admin.views.generic.permissions import PermissionCheckedMixin as PermissionCheckedMixin
from wagtail.admin.views.pages.listing import PageFilterSet as PageFilterSet, PageListingMixin as PageListingMixin
from wagtail.admin.views.pages.utils import GenericPageBreadcrumbsMixin as GenericPageBreadcrumbsMixin
from wagtail.models import Page as Page
from wagtail.permissions import page_permission_policy as page_permission_policy

class ContentTypeUseView(PageListingMixin, PermissionCheckedMixin, BaseListingView):
    permission_policy = page_permission_policy
    any_permission_required: Incomplete
    index_url_name: str
    index_results_url_name: str
    page_title: Incomplete
    header_icon: str
    paginate_by: int
    filterset_class = PageFilterSet
    @classproperty
    def columns(cls): ...
    page_class: Incomplete
    def get(self, request, *, content_type_app_name, content_type_model_name): ...
    def get_page_subtitle(self): ...
    @cached_property
    def verbose_name_plural(self): ...
    def get_base_queryset(self): ...
    def get_index_url(self): ...
    def get_index_results_url(self): ...
    def get_breadcrumbs_items(self): ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class UsageView(GenericPageBreadcrumbsMixin, generic.UsageView):
    model = Page
    pk_url_kwarg: str
    header_icon: str
    usage_url_name: str
    edit_url_name: str
    def dispatch(self, request, *args, **kwargs): ...
