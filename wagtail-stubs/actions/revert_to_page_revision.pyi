import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied

from wagtail.models import Page, Revision

class RevertToPageRevisionError(RuntimeError): ...
class RevertToPageRevisionPermissionError(PermissionDenied): ...

class RevertToPageRevisionAction:
    page: Page
    revision: Revision
    user: AbstractBaseUser | None
    log_action: str
    approved_go_live_at: datetime.datetime | None
    changed: bool
    clean: bool
    def __init__(
        self,
        page: Page,
        revision: Revision,
        user: AbstractBaseUser | None = None,
        log_action: str = "wagtail.revert",
        approved_go_live_at: datetime.datetime | None = None,
        changed: bool = True,
        clean: bool = True,
    ) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> Revision: ...
