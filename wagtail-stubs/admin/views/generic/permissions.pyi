from collections.abc import Collection
from typing import Any

from django.db.models import Model
from django.http import HttpRequest, HttpResponse
from django.utils.functional import cached_property
from wagtail.permission_policies import BasePermissionPolicy

class PermissionCheckedMixin:
    permission_required: str | None
    any_permission_required: Collection[str] | None
    request: HttpRequest
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    @cached_property
    def permission_policy(self) -> BasePermissionPolicy | None: ...
    def user_has_permission(self, permission: str) -> bool: ...
    def user_has_permission_for_instance(self, permission: str, instance: Model) -> bool: ...
    def user_has_any_permission(self, permissions: list[str]) -> bool: ...
