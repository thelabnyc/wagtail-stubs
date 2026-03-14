import logging

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied

from wagtail.models import Page

logger: logging.Logger

class MovePagePermissionError(PermissionDenied): ...

class MovePageAction:
    page: Page
    target: Page
    pos: str | None
    user: AbstractBaseUser | None
    def __init__(
        self,
        page: Page,
        target: Page,
        pos: str | None = None,
        user: AbstractBaseUser | None = None,
    ) -> None: ...
    def check(
        self,
        parent_after: Page,
        skip_permission_checks: bool = False,
    ) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> None: ...
