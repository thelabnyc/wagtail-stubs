from typing import Any

from django.forms import Media
from django.http import HttpRequest
from django.utils.functional import _StrOrPromise
from django.utils.functional import cached_property as cached_property
from wagtail import hooks as hooks
from wagtail.admin.ui.components import Component as Component
from wagtail.models.pages import PagePermissionTester

class ActionMenuItem(Component):
    order: int
    template_name: str
    label: _StrOrPromise
    name: str | None
    classname: str
    icon_name: str
    def __init__(self, order: int | None = None) -> None: ...
    def get_user_page_permissions_tester(self, context: dict[str, Any]) -> PagePermissionTester: ...
    def is_shown(self, context: dict[str, Any]) -> bool: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    def get_url(self, parent_context: dict[str, Any]) -> str | None: ...

class PublishMenuItem(ActionMenuItem):
    label: _StrOrPromise
    name: str
    template_name: str
    icon_name: str
    def is_shown(self, context: dict[str, Any]) -> bool: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class SubmitForModerationMenuItem(ActionMenuItem):
    label: _StrOrPromise
    name: str
    icon_name: str
    def is_shown(self, context: dict[str, Any]) -> bool: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class WorkflowMenuItem(ActionMenuItem):
    template_name: str
    name: str
    label: _StrOrPromise
    launch_modal: bool
    icon_name: str
    def __init__(self, name: str, label: _StrOrPromise, launch_modal: bool, *args: Any, **kwargs: Any) -> None: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    def is_shown(self, context: dict[str, Any]) -> bool | None: ...

class RestartWorkflowMenuItem(ActionMenuItem):
    label: _StrOrPromise
    name: str
    classname: str
    icon_name: str
    def is_shown(self, context: dict[str, Any]) -> bool: ...

class CancelWorkflowMenuItem(ActionMenuItem):
    label: _StrOrPromise
    name: str
    icon_name: str
    def is_shown(self, context: dict[str, Any]) -> bool: ...

class UnpublishMenuItem(ActionMenuItem):
    label: _StrOrPromise
    name: str
    icon_name: str
    def is_shown(self, context: dict[str, Any]) -> bool | None: ...
    def get_url(self, context: dict[str, Any]) -> str: ...

class SaveDraftMenuItem(ActionMenuItem):
    name: str
    label: _StrOrPromise
    template_name: str
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class PageLockedMenuItem(ActionMenuItem):
    name: str
    label: _StrOrPromise
    template_name: str
    def is_shown(self, context: dict[str, Any]) -> bool: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

BASE_PAGE_ACTION_MENU_ITEMS: list[ActionMenuItem] | None

class PageActionMenu:
    template: str
    request: HttpRequest
    context: dict[str, Any]
    menu_items: list[ActionMenuItem]
    default_item: ActionMenuItem | None
    def __init__(self, request: HttpRequest, **kwargs: Any) -> None: ...
    def render_html(self) -> str: ...
    @cached_property
    def media(self) -> Media: ...
