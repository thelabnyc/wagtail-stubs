import logging

from django.contrib.auth.base_user import AbstractBaseUser

from wagtail.actions.unpublish import (
    UnpublishAction,
    UnpublishPermissionError as UnpublishPermissionError,
)
from wagtail.models import Page

logger: logging.Logger

class UnpublishPagePermissionError(UnpublishPermissionError): ...

class UnpublishPageAction(UnpublishAction):
    include_descendants: bool
    def __init__(
        self,
        page: Page,
        set_expired: bool = False,
        commit: bool = True,
        user: AbstractBaseUser | None = None,
        log_action: bool | str = True,
        include_descendants: bool = False,
    ) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> None: ...
