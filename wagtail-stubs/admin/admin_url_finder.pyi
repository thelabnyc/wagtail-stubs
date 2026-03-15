from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from wagtail.hooks import search_for_hooks as search_for_hooks
from wagtail.permission_policies.base import BasePermissionPolicy
from wagtail.utils.registry import ObjectTypeRegistry as ObjectTypeRegistry

class ModelAdminURLFinder:
    edit_url_name: str | None
    permission_policy: BasePermissionPolicy | None
    user: AbstractBaseUser | None
    def __init__(self, user: AbstractBaseUser | None = None) -> None: ...
    def construct_edit_url(self, instance: models.Model) -> str: ...
    def get_edit_url(self, instance: models.Model) -> str | None: ...

class NullAdminURLFinder:
    def __init__(self, user: AbstractBaseUser | None = None) -> None: ...
    def get_edit_url(self, instance: models.Model) -> None: ...

finder_classes: ObjectTypeRegistry

def register_admin_url_finder(model: type[models.Model], handler: type[ModelAdminURLFinder]) -> None: ...

class AdminURLFinder:
    user: AbstractBaseUser | None
    finders_by_model: dict[type[models.Model], ModelAdminURLFinder | NullAdminURLFinder]
    def __init__(self, user: AbstractBaseUser | None = None) -> None: ...
    def get_edit_url(self, instance: models.Model) -> str | None: ...
