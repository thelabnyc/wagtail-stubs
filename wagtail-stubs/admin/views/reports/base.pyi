from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.utils.functional import _StrOrPromise, cached_property
from wagtail.admin.views.generic import BaseListingView, PermissionCheckedMixin
from wagtail.admin.views.mixins import SpreadsheetExportMixin
from wagtail.models import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy

Page: type[AbstractPage]

class ReportView(SpreadsheetExportMixin, PermissionCheckedMixin, BaseListingView):
    template_name: str | list[str] | tuple[str, ...]
    results_template_name: str | list[str] | tuple[str, ...]
    title: _StrOrPromise
    paginate_by: int
    def get_filtered_queryset(self) -> QuerySet[Any]: ...
    def decorate_paginated_queryset(self, object_list: Any) -> Any: ...
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse: ...

class PageReportView(ReportView):
    export_headings: dict[str, _StrOrPromise]
    list_export: list[str]
    context_object_name: str
    model: type[AbstractPage]
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[AbstractPage]: ...
