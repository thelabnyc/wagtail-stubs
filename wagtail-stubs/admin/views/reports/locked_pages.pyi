from django.contrib.auth.models import AbstractBaseUser
from django.db.models import QuerySet
from wagtail.admin.filters import WagtailFilterSet
from wagtail.models import AbstractPage
import django_filters

from .base import PageReportView

Page: type[AbstractPage]

def get_users_for_filter() -> QuerySet[AbstractBaseUser]: ...

class LockedPagesReportFilterSet(WagtailFilterSet):
    locked_at: django_filters.DateFromToRangeFilter
    locked_by: django_filters.ModelChoiceFilter

class LockedPagesView(PageReportView):
    filterset_class: type[LockedPagesReportFilterSet]
    permission_required: str
    def get_filename(self) -> str: ...
    def get_queryset(self) -> QuerySet[AbstractPage]: ...
