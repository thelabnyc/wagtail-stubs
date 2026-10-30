from typing import Any
import logging

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from typing_extensions import TypeVar
from wagtail.actions.base import BaseAction
from wagtail.models.draft_state import DraftStateMixin

_DraftT = TypeVar("_DraftT", bound=DraftStateMixin, default=Any)

logger: logging.Logger

class UnpublishPermissionError(PermissionDenied): ...

class UnpublishAction(BaseAction[_DraftT]):
    object: _DraftT
    set_expired: bool
    commit: bool
    log_action: bool | str
    def __init__(
        self,
        object: _DraftT,
        set_expired: bool = False,
        commit: bool = True,
        user: AbstractBaseUser | None = None,
        log_action: bool | str = True,
    ) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> None: ...
