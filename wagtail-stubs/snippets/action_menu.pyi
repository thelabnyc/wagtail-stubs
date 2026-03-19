from typing import Any

from django.http import HttpRequest
from django.utils.functional import cached_property as cached_property
from wagtail import hooks as hooks
from wagtail.admin.ui.components import Component as Component
from wagtail.models.draft_state import DraftStateMixin as DraftStateMixin
from wagtail.models.locking import LockableMixin as LockableMixin
from wagtail.models.workflows import WorkflowMixin as WorkflowMixin
from wagtail.snippets.permissions import get_permission_name as get_permission_name

class ActionMenuItem(Component):
    order: int
    template_name: str
    label: str
    name: str | None
    classname: str
    icon_name: str
    def __init__(self, order=None) -> None: ...
    def is_shown(self, context): ...
    def get_context_data(self, parent_context): ...
    def get_url(self, parent_context) -> None: ...

class PublishMenuItem(ActionMenuItem):
    name: str
    label: str
    icon_name: str
    template_name: str
    def is_shown(self, context): ...

class SubmitForModerationMenuItem(ActionMenuItem):
    name: str
    label: str
    icon_name: str
    def is_shown(self, context): ...
    def get_context_data(self, parent_context): ...

class WorkflowMenuItem(ActionMenuItem):
    template_name: str
    name: str
    label: str
    launch_modal: bool
    icon_name: str
    def __init__(self, name, label, launch_modal, *args, **kwargs) -> None: ...
    def get_context_data(self, parent_context): ...
    def is_shown(self, context): ...
    def get_url(self, parent_context): ...

class RestartWorkflowMenuItem(ActionMenuItem):
    label: str
    name: str
    classname: str
    icon_name: str
    def is_shown(self, context): ...

class CancelWorkflowMenuItem(ActionMenuItem):
    label: str
    name: str
    icon_name: str
    def is_shown(self, context): ...

class UnpublishMenuItem(ActionMenuItem):
    label: str
    name: str
    icon_name: str
    def is_shown(self, context): ...
    def get_url(self, context): ...

class SaveMenuItem(ActionMenuItem):
    name: str
    label: str
    icon_name: str
    template_name: str

class LockedMenuItem(ActionMenuItem):
    name: str
    label: str
    template_name: str
    def is_shown(self, context): ...

def get_base_snippet_action_menu_items(model): ...

class SnippetActionMenu:
    template: str
    request: HttpRequest
    context: dict[str, Any]
    menu_items: list[ActionMenuItem]
    default_item: ActionMenuItem | None
    def __init__(self, request, **kwargs) -> None: ...
    def render_html(self): ...
    @cached_property
    def media(self): ...
