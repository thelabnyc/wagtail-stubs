from typing import Any

from django.db import models
from django.db.models import QuerySet
from django.http import HttpRequest, JsonResponse
from django.views.generic import View
from typing_extensions import TypeVar

from .permissions import PermissionCheckedMixin

_ModelT = TypeVar("_ModelT", bound=models.Model, default=models.Model)

class ReorderView(PermissionCheckedMixin[_ModelT], View):
    model: type[_ModelT] | None
    sort_order_field: str | None
    permission_required: str
    def get_queryset(self) -> QuerySet[_ModelT]: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse: ...
