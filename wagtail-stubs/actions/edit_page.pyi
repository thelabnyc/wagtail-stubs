from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.actions.edit import EditAction
from wagtail.models.pages import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy

_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

class EditPageAction(EditAction[_PageT]):
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[_PageT]: ...
    def user_has_permission(self) -> bool: ...
    def check_publish(self) -> None: ...
