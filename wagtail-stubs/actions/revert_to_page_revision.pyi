from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.actions.revert_to_revision import (
    RevertToRevisionAction,
    RevertToRevisionPermissionError,
)
from wagtail.models.pages import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy

_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

class RevertToPageRevisionError(RuntimeError): ...
class RevertToPageRevisionPermissionError(RevertToRevisionPermissionError): ...

class RevertToPageRevisionAction(RevertToRevisionAction[_PageT]):
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[_PageT]: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
