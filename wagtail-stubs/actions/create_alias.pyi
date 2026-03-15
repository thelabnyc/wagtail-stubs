import logging

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from wagtail.models import Locale, Page

logger: logging.Logger

class CreatePageAliasIntegrityError(RuntimeError): ...
class CreatePageAliasPermissionError(PermissionDenied): ...

class CreatePageAliasAction:
    page: Page
    recursive: bool
    parent: Page | None
    update_slug: str | None
    update_locale: Locale | None
    user: AbstractBaseUser | None
    log_action: str | None
    reset_translation_key: bool
    def __init__(
        self,
        page: Page,
        *,
        recursive: bool = False,
        parent: Page | None = None,
        update_slug: str | None = None,
        update_locale: Locale | None = None,
        user: AbstractBaseUser | None = None,
        log_action: str | None = "wagtail.create_alias",
        reset_translation_key: bool = True,
        _mpnode_attrs: tuple[str, int] | None = None,
    ) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> Page: ...
