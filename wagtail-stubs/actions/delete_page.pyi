from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied

from wagtail.models import Page

class DeletePagePermissionError(PermissionDenied): ...

class DeletePageAction:
    page: Page
    user: AbstractBaseUser
    def __init__(self, page: Page, user: AbstractBaseUser) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(
        self,
        *args: object,
        skip_permission_checks: bool = False,
        **kwargs: object,
    ) -> tuple[int, dict[str, int]]: ...
    def log_deletion(self, page: Page) -> None: ...
