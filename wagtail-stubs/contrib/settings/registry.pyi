from typing import Any, Protocol, overload

from django.db import models
from django.http import HttpRequest
from wagtail.admin.admin_url_finder import ModelAdminURLFinder
from wagtail.admin.menu import MenuItem
from wagtail.permissions import policy_registry as policy_registry
from wagtail.permissions import register_permission_policy as register_permission_policy

from .models import BaseGenericSetting, BaseSiteSetting

class SettingMenuItem(MenuItem):
    model: type[models.Model]
    def __init__(self, model: type[models.Model], icon: str = "cog", classname: str = "", **kwargs: Any) -> None: ...
    def is_shown(self, request: HttpRequest) -> bool: ...

class SiteSettingAdminURLFinder(ModelAdminURLFinder):
    def construct_edit_url(self, instance: models.Model) -> str: ...

class GenericSettingAdminURLFinder(ModelAdminURLFinder):
    def construct_edit_url(self, instance: models.Model) -> str: ...

class _SettingDecorator(Protocol):
    def __call__[T: BaseSiteSetting | BaseGenericSetting](self, model: type[T]) -> type[T]: ...

class Registry(list[type[models.Model]]):
    def __init__(self) -> None: ...
    def register[T: BaseSiteSetting | BaseGenericSetting](
        self, model: type[T], icon: str = "cog", **kwargs: Any
    ) -> type[T]: ...
    @overload
    def register_decorator[T: BaseSiteSetting | BaseGenericSetting](
        self, model: type[T], icon: str = "cog", **kwargs: Any
    ) -> type[T]: ...
    @overload
    def register_decorator(self, model: None = None, icon: str = "cog", **kwargs: Any) -> _SettingDecorator: ...
    def get_by_natural_key(self, app_label: str, model_name: str) -> type[models.Model] | None: ...

registry: Registry

@overload
def register_setting[T: BaseSiteSetting | BaseGenericSetting](
    model: type[T], icon: str = "cog", **kwargs: Any
) -> type[T]: ...
@overload
def register_setting(model: None = None, icon: str = "cog", **kwargs: Any) -> _SettingDecorator: ...
