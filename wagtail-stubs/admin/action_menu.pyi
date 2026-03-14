from _typeshed import Incomplete
from django.utils.functional import cached_property as cached_property
from wagtail import hooks as hooks
from wagtail.admin.ui.components import Component as Component

class ActionMenuItem(Component):
    order: int
    template_name: str
    label: str
    name: Incomplete
    classname: str
    icon_name: str
    def __init__(self, order=None) -> None: ...
    def get_user_page_permissions_tester(self, context): ...
    def is_shown(self, context): ...
    def get_context_data(self, parent_context): ...
    def get_url(self, parent_context) -> None: ...

class PublishMenuItem(ActionMenuItem):
    label: Incomplete
    name: str
    template_name: str
    icon_name: str
    def is_shown(self, context): ...
    def get_context_data(self, parent_context): ...

class SubmitForModerationMenuItem(ActionMenuItem):
    label: Incomplete
    name: str
    icon_name: str
    def is_shown(self, context): ...
    def get_context_data(self, parent_context): ...

class WorkflowMenuItem(ActionMenuItem):
    template_name: str
    name: Incomplete
    label: Incomplete
    launch_modal: Incomplete
    icon_name: Incomplete
    def __init__(self, name, label, launch_modal, *args, **kwargs) -> None: ...
    def get_context_data(self, parent_context): ...
    def is_shown(self, context): ...

class RestartWorkflowMenuItem(ActionMenuItem):
    label: Incomplete
    name: str
    classname: str
    icon_name: str
    def is_shown(self, context): ...

class CancelWorkflowMenuItem(ActionMenuItem):
    label: Incomplete
    name: str
    icon_name: str
    def is_shown(self, context): ...

class UnpublishMenuItem(ActionMenuItem):
    label: Incomplete
    name: str
    icon_name: str
    def is_shown(self, context): ...
    def get_url(self, context): ...

class SaveDraftMenuItem(ActionMenuItem):
    name: str
    label: Incomplete
    template_name: str
    def get_context_data(self, parent_context): ...

class PageLockedMenuItem(ActionMenuItem):
    name: str
    label: Incomplete
    template_name: str
    def is_shown(self, context): ...
    def get_context_data(self, parent_context): ...

BASE_PAGE_ACTION_MENU_ITEMS: Incomplete

class PageActionMenu:
    template: str
    request: Incomplete
    context: Incomplete
    menu_items: Incomplete
    default_item: Incomplete
    def __init__(self, request, **kwargs) -> None: ...
    def render_html(self): ...
    @cached_property
    def media(self): ...
