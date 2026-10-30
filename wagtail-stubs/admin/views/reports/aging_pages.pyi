from typing import Any

from django.db.models import QuerySet
from wagtail.admin.filters import ContentTypeFilter, WagtailFilterSet
from wagtail.models import AbstractPage
import django_filters

from .base import PageReportView

Page: type[AbstractPage]

class AgingPagesReportFilterSet(WagtailFilterSet):
    last_published_at: django_filters.DateTimeFilter
    content_type: ContentTypeFilter

class AgingPagesView(PageReportView):
    filterset_class: type[AgingPagesReportFilterSet]
    any_permission_required: list[str]
    def __init__(self, **kwargs: Any) -> None: ...
    def user_id_to_python(self, user_id: Any) -> Any: ...
    def add_last_publisher_name_to_page(self, username_mapping: dict[Any, str], page: AbstractPage) -> None: ...
    def decorate_paginated_queryset(self, queryset: Any) -> Any: ...
    def get_queryset(self) -> QuerySet[AbstractPage]: ...
