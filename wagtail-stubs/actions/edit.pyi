from typing import Any

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.db.models import Model
from django.forms import BaseModelForm
from typing_extensions import TypeVar
from wagtail.actions.base import BaseAction
from wagtail.models.revisions import Revision

_ModelT = TypeVar("_ModelT", bound=Model, default=Any)

class EditPermissionError(PermissionDenied): ...

class EditAction(BaseAction[_ModelT]):
    form: BaseModelForm[_ModelT] | None
    log_action: str | bool | None
    publish: bool
    previous_revision: Revision | None
    overwrite_revision: Revision | None
    revision_enabled: bool
    draftstate_enabled: bool
    content_changed: bool
    clean: bool
    revision: Revision | None
    def __init__(
        self,
        instance: _ModelT,
        user: AbstractBaseUser | None = None,
        *,
        form: BaseModelForm[_ModelT] | None = None,
        log_action: str | bool | None = "wagtail.edit",
        publish: bool = False,
        previous_revision: Revision | None = None,
        overwrite_revision: Revision | None = None,
        clean: bool | None = None,
    ) -> None: ...
    def check_lock(self) -> None: ...
    def check_publish(self) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> _ModelT: ...
