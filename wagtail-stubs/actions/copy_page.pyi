import logging
import uuid
from collections.abc import Callable, Sequence

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied

from wagtail.models import Page

logger: logging.Logger

class CopyPageIntegrityError(RuntimeError): ...
class CopyPagePermissionError(PermissionDenied): ...

class CopyPageAction:
    page: Page
    to: Page | None
    update_attrs: dict[str, object] | None
    exclude_fields: Sequence[str] | None
    recursive: bool
    copy_revisions: bool
    keep_live: bool
    user: AbstractBaseUser | None
    process_child_object: Callable[..., object] | None
    log_action: str | None
    reset_translation_key: bool
    def __init__(
        self,
        page: Page,
        to: Page | None = None,
        update_attrs: dict[str, object] | None = None,
        exclude_fields: Sequence[str] | None = None,
        recursive: bool = False,
        copy_revisions: bool = True,
        keep_live: bool = True,
        user: AbstractBaseUser | None = None,
        process_child_object: Callable[..., object] | None = None,
        log_action: str | None = "wagtail.copy",
        reset_translation_key: bool = True,
    ) -> None: ...
    def generate_translation_key(self, old_uuid: uuid.UUID) -> uuid.UUID: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> Page: ...
