from typing import Any
import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from typing_extensions import TypeVar
from wagtail.actions.base import BaseAction
from wagtail.models.revisions import Revision, RevisionMixin

_RevisableT = TypeVar("_RevisableT", bound=RevisionMixin, default=Any)

class RevertToRevisionPermissionError(PermissionDenied): ...

class RevertToRevisionAction(BaseAction[_RevisableT]):
    revision: Revision
    log_action: str | bool
    approved_go_live_at: datetime.datetime | None
    changed: bool
    clean: bool
    def __init__(
        self,
        instance: _RevisableT,
        revision: Revision,
        user: AbstractBaseUser | None = None,
        log_action: str | bool = "wagtail.revert",
        approved_go_live_at: datetime.datetime | None = None,
        changed: bool = True,
        clean: bool = True,
    ) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> Revision: ...
