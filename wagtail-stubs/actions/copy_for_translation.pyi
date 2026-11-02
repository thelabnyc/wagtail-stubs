from collections.abc import Sequence
from typing import Any

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.actions.base import BaseAction
from wagtail.models.i18n import Locale, TranslatableMixin
from wagtail.models.pages import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy

_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)
_TranslatableT = TypeVar("_TranslatableT", bound=TranslatableMixin, default=Any)

class ParentNotTranslatedError(Exception): ...
class CopyForTranslationPermissionError(PermissionDenied): ...
class CopyPageForTranslationPermissionError(CopyForTranslationPermissionError): ...

class CopyPageForTranslationAction(BaseAction[_PageT]):
    page: _PageT
    locale: Locale
    copy_parents: bool
    alias: bool
    exclude_fields: Sequence[str] | None
    include_subtree: bool
    def __init__(
        self,
        page: _PageT,
        locale: Locale,
        copy_parents: bool = False,
        alias: bool = False,
        exclude_fields: Sequence[str] | None = None,
        user: AbstractBaseUser | None = None,
        include_subtree: bool = False,
    ) -> None: ...
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[AbstractPage]: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def walk(self, current_page: AbstractPage) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> _PageT: ...

class CopyForTranslationAction(BaseAction[_TranslatableT]):
    object: _TranslatableT
    locale: Locale
    exclude_fields: Sequence[str] | None
    def __init__(
        self,
        object: _TranslatableT,
        locale: Locale,
        exclude_fields: Sequence[str] | None = None,
        user: AbstractBaseUser | None = None,
    ) -> None: ...
    def user_has_permission(self) -> bool: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> _TranslatableT: ...
