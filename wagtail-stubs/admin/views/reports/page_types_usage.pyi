from typing import Any

from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet
from django.utils.functional import cached_property
from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.views.reports import ReportView
from wagtail.models import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy
import django_filters

Page: type[AbstractPage]

class LocaleFilter(django_filters.ChoiceFilter):
    def filter(self, qs: QuerySet[ContentType], language_code: str | None) -> QuerySet[ContentType]: ...

class SiteFilter(django_filters.ChoiceFilter):
    def filter(self, qs: QuerySet[ContentType], site_root_path: str | None) -> QuerySet[ContentType]: ...

class PageTypesUsageReportFilterSet(WagtailFilterSet):
    page_locale: LocaleFilter
    site: SiteFilter
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class PageTypesUsageReportView(ReportView):
    filterset_class: type[PageTypesUsageReportFilterSet]
    any_permission_required: list[str]
    page_models: list[str]
    i18n_enabled: bool
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[AbstractPage]: ...
    def __init__(self, **kwargs: Any) -> None: ...
    def decorate_paginated_queryset(self, page_types: Any) -> Any: ...
    def get_queryset(self) -> QuerySet[ContentType]: ...
