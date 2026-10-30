import logging

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.actions.base import BaseAction
from wagtail.models.pages import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy

_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

logger: logging.Logger

class MovePagePermissionError(PermissionDenied): ...

class MovePageAction(BaseAction[_PageT]):
    page: _PageT
    target: AbstractPage
    pos: str | None
    def __init__(
        self,
        page: _PageT,
        target: AbstractPage,
        pos: str | None = None,
        user: AbstractBaseUser | None = None,
    ) -> None: ...
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[_PageT]: ...
    def check(  # type: ignore[override]
        self,
        parent_after: AbstractPage,
        skip_permission_checks: bool = False,
    ) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> None: ...
