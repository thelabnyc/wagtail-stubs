from typing import Any

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import PermissionDenied
from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.actions.base import BaseAction
from wagtail.models.pages import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy

_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

class DeletePagePermissionError(PermissionDenied): ...

class DeletePageAction(BaseAction[_PageT]):
    page: _PageT
    def __init__(self, page: _PageT, user: AbstractBaseUser | None = None) -> None: ...
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[AbstractPage]: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(
        self,
        *args: Any,
        skip_permission_checks: bool = False,
        **kwargs: Any,
    ) -> tuple[int, dict[str, int]]: ...
    def log_deletion(self, page: AbstractPage) -> None: ...
