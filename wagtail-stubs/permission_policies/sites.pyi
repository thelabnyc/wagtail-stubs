from collections.abc import Iterable
from typing import Any

from django.contrib.auth.models import AbstractBaseUser
from django.db.models import Model, QuerySet
from typing_extensions import TypeVar
from wagtail.models.sites import Site
from wagtail.permission_policies.base import BaseDjangoAuthPermissionPolicy

_ModelT = TypeVar("_ModelT", bound=Model, default=Any)

class SitePermissionPolicy(BaseDjangoAuthPermissionPolicy[_ModelT]):
    permission_cache_name: str
    site_field_name: str
    site_fk_field_name: str

    def __init__(
        self,
        model: type[_ModelT] | str,
        auth_model: type[Model] | str | None = None,
        site_field_name: str = "site",
    ) -> None: ...
    def user_has_permission(self, user: AbstractBaseUser, action: str) -> bool: ...
    def user_has_any_permission(self, user: AbstractBaseUser, actions: Iterable[str]) -> bool: ...
    def users_with_any_permission(self, actions: Iterable[str]) -> QuerySet[AbstractBaseUser]: ...
    def user_has_any_permission_for_instance(
        self, user: AbstractBaseUser, actions: Iterable[str], instance: _ModelT
    ) -> bool: ...
    def user_has_permission_for_instance(self, user: AbstractBaseUser, action: str, instance: _ModelT) -> bool: ...
    def sites_user_has_any_permission_for(self, user: AbstractBaseUser, actions: Iterable[str]) -> QuerySet[Site]: ...
    def sites_user_has_permission_for(self, user: AbstractBaseUser, action: str) -> QuerySet[Site]: ...
    def instances_user_has_any_permission_for(
        self, user: AbstractBaseUser, actions: Iterable[str]
    ) -> QuerySet[_ModelT]: ...
    def users_with_any_permission_for_instance(
        self, actions: Iterable[str], instance: _ModelT
    ) -> QuerySet[AbstractBaseUser]: ...
