from typing import Any

from django.db import models
from django.db.models import QuerySet
from django.http import HttpRequest, JsonResponse
from django.views.generic import View

from .permissions import PermissionCheckedMixin

class ReorderView(PermissionCheckedMixin, View):
    model: type[models.Model] | None
    sort_order_field: str | None
    permission_required: str
    def get_queryset(self) -> QuerySet[models.Model]: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse: ...
