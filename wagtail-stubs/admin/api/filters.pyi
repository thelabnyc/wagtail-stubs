from rest_framework.filters import BaseFilterBackend
from wagtail import hooks as hooks
from wagtail.api.v2.utils import BadRequestError as BadRequestError
from wagtail.api.v2.utils import parse_boolean as parse_boolean
from wagtail.models import AbstractPage
from wagtail.permissions import policy_registry as policy_registry

Page: type[AbstractPage]

class HasChildrenFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...

class ForExplorerFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): ...
