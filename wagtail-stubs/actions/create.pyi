from typing import Any, Final

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.db.models import Model
from django.forms import BaseModelForm
from typing_extensions import TypeVar
from wagtail.actions.base import BaseAction
from wagtail.models.revisions import Revision

_ModelT = TypeVar("_ModelT", bound=Model, default=Any)

UNSET: Final[object]

class CreatePermissionError(PermissionDenied): ...

class CreateAction(BaseAction[_ModelT]):
    form: BaseModelForm[_ModelT] | None
    log_action: str | bool | None
    publish: bool
    sort_order_field: str | object | None
    revision_enabled: bool
    draftstate_enabled: bool
    clean: bool
    revision: Revision | None
    def __init__(
        self,
        instance: _ModelT,
        user: AbstractBaseUser | None = None,
        *,
        form: BaseModelForm[_ModelT] | None = None,
        log_action: str | bool | None = "wagtail.create",
        publish: bool = False,
        sort_order_field: str | None = ...,
        clean: bool | None = None,
    ) -> None: ...
    def user_has_permission(self) -> bool: ...
    def check_publish(self) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> _ModelT: ...
