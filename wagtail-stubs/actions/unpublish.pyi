import logging

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.db import models

logger: logging.Logger

class UnpublishPermissionError(PermissionDenied): ...

class UnpublishAction:
    object: models.Model
    set_expired: bool
    commit: bool
    user: AbstractBaseUser | None
    log_action: bool | str
    def __init__(
        self,
        object: models.Model,
        set_expired: bool = False,
        commit: bool = True,
        user: AbstractBaseUser | None = None,
        log_action: bool | str = True,
    ) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> None: ...
