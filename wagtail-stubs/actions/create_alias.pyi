import logging

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.actions.base import BaseAction
from wagtail.models.i18n import Locale
from wagtail.models.pages import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy

_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

logger: logging.Logger

class CreatePageAliasIntegrityError(RuntimeError): ...
class CreatePageAliasPermissionError(PermissionDenied): ...

class CreatePageAliasAction(BaseAction[_PageT]):
    page: _PageT
    recursive: bool
    parent: AbstractPage | None
    update_slug: str | None
    update_locale: Locale | None
    log_action: str | None
    reset_translation_key: bool
    def __init__(
        self,
        page: _PageT,
        *,
        recursive: bool = False,
        parent: AbstractPage | None = None,
        update_slug: str | None = None,
        update_locale: Locale | None = None,
        user: AbstractBaseUser | None = None,
        log_action: str | None = "wagtail.create_alias",
        reset_translation_key: bool = True,
        _mpnode_attrs: tuple[str, int] | None = None,
    ) -> None: ...
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[_PageT]: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> _PageT: ...
