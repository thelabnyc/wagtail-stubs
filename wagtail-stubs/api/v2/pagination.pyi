from typing import Any

from django.db.models import QuerySet
from rest_framework.pagination import BasePagination
from rest_framework.request import Request
from rest_framework.response import Response

from .utils import BadRequestError as BadRequestError

class WagtailPagination(BasePagination):
    view: Any
    total_count: int
    def paginate_queryset(self, queryset: QuerySet[Any], request: Request, view: Any = None) -> QuerySet[Any]: ...
    def get_paginated_response(self, data: Any) -> Response: ...
