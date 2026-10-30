from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest
from ninja.pagination import LimitOffsetPagination

class WagtailLimitOffsetPagination(LimitOffsetPagination):
    class Input(LimitOffsetPagination.Input):
        limit: int = ...
        offset: int = ...

    def paginate_queryset(
        self,
        queryset: QuerySet[Any],
        pagination: LimitOffsetPagination.Input,
        request: HttpRequest,
        **params: Any,
    ) -> dict[str, Any]: ...
