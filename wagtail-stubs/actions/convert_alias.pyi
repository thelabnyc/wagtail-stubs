from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from wagtail.models.pages import Page

class ConvertAliasPageError(RuntimeError): ...
class ConvertAliasPagePermissionError(PermissionDenied): ...

class ConvertAliasPageAction:
    page: Page
    log_action: str | None
    user: AbstractBaseUser | None
    def __init__(
        self,
        page: Page,
        *,
        log_action: str | None = "wagtail.convert_alias",
        user: AbstractBaseUser | None = None,
    ) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> Page: ...
