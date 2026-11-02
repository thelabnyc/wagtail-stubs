from typing import Any

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.db.models import Model
from typing_extensions import TypeVar
from wagtail.actions.base import BaseAction

_ModelT = TypeVar("_ModelT", bound=Model, default=Any)

class DeletePermissionError(PermissionDenied): ...

class DeleteAction(BaseAction[_ModelT]):
    log_action: str | bool | None
    def __init__(
        self,
        instance: _ModelT,
        user: AbstractBaseUser | None = None,
        *,
        log_action: str | bool | None = "wagtail.delete",
    ) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> tuple[int, dict[str, int]]: ...
