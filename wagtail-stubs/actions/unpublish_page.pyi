import logging

from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.actions.unpublish import (
    UnpublishAction,
)
from wagtail.actions.unpublish import (
    UnpublishPermissionError as UnpublishPermissionError,
)
from wagtail.models.pages import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy

_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

logger: logging.Logger

class UnpublishPagePermissionError(UnpublishPermissionError): ...

class UnpublishPageAction(UnpublishAction[_PageT]):
    include_descendants: bool
    def __init__(
        self,
        page: _PageT,
        set_expired: bool = False,
        commit: bool = True,
        user: AbstractBaseUser | None = None,
        log_action: bool | str = True,
        include_descendants: bool = False,
    ) -> None: ...
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[_PageT]: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False) -> None: ...
