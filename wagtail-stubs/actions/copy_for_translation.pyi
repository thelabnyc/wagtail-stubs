from collections.abc import Sequence

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.db import models

from wagtail.models import Locale, Page

class ParentNotTranslatedError(Exception): ...
class CopyForTranslationPermissionError(PermissionDenied): ...
class CopyPageForTranslationPermissionError(CopyForTranslationPermissionError): ...

class CopyPageForTranslationAction:
    page: Page
    locale: Locale
    copy_parents: bool
    alias: bool
    exclude_fields: Sequence[str] | None
    user: AbstractBaseUser | None
    include_subtree: bool
    def __init__(
        self,
        page: Page,
        locale: Locale,
        copy_parents: bool = False,
        alias: bool = False,
        exclude_fields: Sequence[str] | None = None,
        user: AbstractBaseUser | None = None,
        include_subtree: bool = False,
    ) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def walk(self, current_page: Page) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> Page: ...

class CopyForTranslationAction:
    object: models.Model
    locale: Locale
    exclude_fields: Sequence[str] | None
    user: AbstractBaseUser | None
    def __init__(
        self,
        object: models.Model,
        locale: Locale,
        exclude_fields: Sequence[str] | None = None,
        user: AbstractBaseUser | None = None,
    ) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> models.Model: ...
