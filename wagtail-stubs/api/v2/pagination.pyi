from .utils import BadRequestError as BadRequestError
from _typeshed import Incomplete
from rest_framework.pagination import BasePagination

class WagtailPagination(BasePagination):
    view: Incomplete
    total_count: Incomplete
    def paginate_queryset(self, queryset, request, view=None): ...
    def get_paginated_response(self, data): ...
