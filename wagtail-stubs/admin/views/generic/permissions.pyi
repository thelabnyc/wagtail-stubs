from collections.abc import Collection
from typing import Any, Generic

from django.db.models import Model
from django.http import HttpRequest, HttpResponse
from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.permission_policies import BasePermissionPolicy

_ModelT = TypeVar("_ModelT", bound=Model, default=Model)

class PermissionCheckedMixin(Generic[_ModelT]):
    permission_required: str | None
    any_permission_required: Collection[str] | None
    request: HttpRequest
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    @cached_property
    def permission_policy(self) -> BasePermissionPolicy[Any] | None: ...
    def user_has_permission(self, permission: str) -> bool: ...
    def user_has_permission_for_instance(self, permission: str, instance: _ModelT) -> bool: ...
    def user_has_any_permission(self, permissions: list[str]) -> bool: ...
