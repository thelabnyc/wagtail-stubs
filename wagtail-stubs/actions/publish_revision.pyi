from typing import Any
import logging

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.db import models
from django.utils.functional import cached_property
from wagtail.actions.base import BaseAction
from wagtail.models.revisions import Revision
from wagtail.permission_policies.base import BasePermissionPolicy

logger: logging.Logger

class PublishPermissionError(PermissionDenied): ...

class PublishRevisionAction(BaseAction[models.Model]):
    revision: Revision
    object: models.Model
    changed: bool
    log_action: bool
    previous_revision: Revision | None
    def __init__(
        self,
        revision: Revision,
        user: AbstractBaseUser | None = None,
        changed: bool = True,
        log_action: bool = True,
        previous_revision: Revision | None = None,
    ) -> None: ...
    @cached_property
    def permission_policy(self) -> BasePermissionPolicy[Any]: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def log_scheduling_action(self) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> None: ...
