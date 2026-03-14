from rest_framework.filters import BaseFilterBackend
from wagtail import hooks as hooks
from wagtail.api.v2.utils import BadRequestError as BadRequestError, parse_boolean as parse_boolean
from wagtail.permissions import page_permission_policy as page_permission_policy

class HasChildrenFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...

class ForExplorerFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...
