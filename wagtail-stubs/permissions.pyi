from typing import Literal, overload

from django.db.models import Model
from wagtail.models import AbstractPage, Locale, Site, Task, Workflow
from wagtail.permission_policies import BasePermissionPolicy as BasePermissionPolicy
from wagtail.permission_policies import ModelPermissionPolicy as ModelPermissionPolicy
from wagtail.permission_policies.collections import CollectionManagementPermissionPolicy
from wagtail.permission_policies.pages import PagePermissionPolicy
from wagtail.utils.registry import ObjectTypeRegistry

class PolicyRegistry(ObjectTypeRegistry):
    fallback_policies: dict[type[Model], BasePermissionPolicy]
    def __init__(self) -> None: ...
    def get_fallback_policy[M: Model](self, cls: type[M]) -> BasePermissionPolicy[M] | None: ...
    @overload
    def get_by_type[P: AbstractPage](self, cls: type[P], fallback: Literal[True] = True) -> PagePermissionPolicy[P]: ...
    @overload
    def get_by_type[M: Model](self, cls: type[M], fallback: Literal[True] = True) -> BasePermissionPolicy[M]: ...
    @overload
    def get_by_type[M: Model](self, cls: type[M], fallback: bool) -> BasePermissionPolicy[M] | None: ...
    @overload
    def get[P: AbstractPage](self, obj: P) -> PagePermissionPolicy[P]: ...
    @overload
    def get[M: Model](self, obj: M) -> BasePermissionPolicy[M]: ...
    def register[M: Model](
        self, cls: type[M], value: BasePermissionPolicy[M] | None = None, exact_class: bool = False
    ) -> None: ...

policy_registry: PolicyRegistry

def register_permission_policy[M: Model](
    model: type[M], policy: BasePermissionPolicy[M] | None = None, exact_class: bool = False
) -> None: ...

page_permission_policy: PagePermissionPolicy[AbstractPage]
site_permission_policy: ModelPermissionPolicy[Site]
collection_permission_policy: CollectionManagementPermissionPolicy
task_permission_policy: ModelPermissionPolicy[Task]
workflow_permission_policy: ModelPermissionPolicy[Workflow]
locale_permission_policy: ModelPermissionPolicy[Locale]
