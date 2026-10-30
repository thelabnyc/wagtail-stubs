from django.contrib.auth.base_user import AbstractBaseUser
from django.forms import BaseModelForm
from django.utils.functional import cached_property
from typing_extensions import TypeVar
from wagtail.actions.create import CreateAction
from wagtail.models.pages import AbstractPage
from wagtail.permission_policies.pages import PagePermissionPolicy

_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

class CreatePageAction(CreateAction[_PageT]):
    parent: AbstractPage
    def __init__(
        self,
        instance: _PageT,
        parent: AbstractPage,
        user: AbstractBaseUser | None = None,
        *,
        form: BaseModelForm[_PageT] | None = None,
        publish: bool = False,
        sort_order_field: str | None = ...,
        clean: bool | None = None,
    ) -> None: ...
    @cached_property
    def permission_policy(self) -> PagePermissionPolicy[_PageT]: ...
    def user_has_permission(self) -> bool: ...
    def check_publish(self) -> None: ...
