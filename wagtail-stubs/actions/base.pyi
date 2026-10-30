from typing import Any, Generic

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.db.models import Model
from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.permission_policies.base import BasePermissionPolicy

_ModelT = TypeVar("_ModelT", bound=Model, default=Any)

class BaseAction(Generic[_ModelT]):
    action_name: str | None
    permission_policy_action: str | None
    permission_error_class: type[PermissionDenied]
    instance: _ModelT
    user: AbstractBaseUser | None
    def __init__(self, instance: _ModelT, user: AbstractBaseUser | None = None) -> None: ...
    @cached_property
    def permission_policy(self) -> BasePermissionPolicy[_ModelT]: ...
    def user_has_permission(self) -> bool: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> Any: ...
