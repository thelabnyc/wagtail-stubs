from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseBase
from wagtail.admin.ui.tables.pages import PageTable
from wagtail.admin.views import generic as generic
from wagtail.admin.views.pages.listing import IndexView as IndexView
from wagtail.admin.views.pages.utils import GenericPageBreadcrumbsMixin as GenericPageBreadcrumbsMixin
from wagtail.models.pages import Page as Page

class ContentTypeUseView(IndexView):
    index_url_name: str
    index_results_url_name: str
    page_title: str
    header_icon: str
    def get_table(self, object_list: QuerySet[Page]) -> PageTable: ...
    def get(
        self, request: HttpRequest, *, content_type_app_name: str, content_type_model_name: str
    ) -> HttpResponse: ...
    def get_page_subtitle(self) -> str: ...
    def get_add_url(self) -> str: ...
    def get_index_url(self) -> str: ...
    def get_index_results_url(self) -> str: ...
    def get_breadcrumbs_items(self) -> list[dict[str, str]]: ...

class UsageView(GenericPageBreadcrumbsMixin, generic.UsageView):
    model = Page
    pk_url_kwarg: str
    header_icon: str
    usage_url_name: str
    edit_url_name: str
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
