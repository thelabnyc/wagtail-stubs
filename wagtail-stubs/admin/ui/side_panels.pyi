from _typeshed import Incomplete
from wagtail.admin.ui.components import Component as Component
from wagtail.admin.userbar import AccessibilityItem as AccessibilityItem, apply_userbar_hooks as apply_userbar_hooks
from wagtail.models import DraftStateMixin as DraftStateMixin, LockableMixin as LockableMixin, Page as Page, ReferenceIndex as ReferenceIndex
from wagtail.models.view_restrictions import BaseViewRestriction as BaseViewRestriction

class BaseSidePanel(Component):
    class SidePanelToggle(Component):
        template_name: str
        aria_label: str
        icon_name: str
        has_counter: bool
        counter_classname: str
        keyboard_shortcut: Incomplete
        panel: Incomplete
        def __init__(self, panel) -> None: ...
        def get_context_data(self, parent_context): ...
    object: Incomplete
    request: Incomplete
    model: Incomplete
    toggle: Incomplete
    def __init__(self, object, request) -> None: ...
    def get_context_data(self, parent_context): ...

class StatusSidePanel(BaseSidePanel):
    class SidePanelToggle(BaseSidePanel.SidePanelToggle):
        aria_label: Incomplete
        icon_name: str
        counter_classname: str
        def get_context_data(self, parent_context): ...
    name: str
    title: Incomplete
    template_name: str
    order: int
    show_schedule_publishing_toggle: Incomplete
    live_object: Incomplete
    scheduled_object: Incomplete
    locale: Incomplete
    translations: Incomplete
    usage_url: Incomplete
    history_url: Incomplete
    last_updated_info: Incomplete
    locking_enabled: Incomplete
    def __init__(self, *args, show_schedule_publishing_toggle=None, live_object=None, scheduled_object=None, locale=None, translations=None, usage_url=None, history_url=None, last_updated_info=None, **kwargs) -> None: ...
    def get_status_templates(self, context): ...
    def get_scheduled_publishing_context(self, parent_context): ...
    lock: Incomplete
    def get_lock_context(self, parent_context): ...
    def get_usage_context(self): ...
    def get_context_data(self, parent_context): ...

class PageStatusSidePanel(StatusSidePanel):
    parent_page: Incomplete
    usage_url: str
    history_url: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_status_templates(self, context): ...
    def get_usage_context(self): ...
    def get_context_data(self, parent_context): ...

class CommentsSidePanel(BaseSidePanel):
    class SidePanelToggle(BaseSidePanel.SidePanelToggle):
        aria_label: Incomplete
        icon_name: str
    name: str
    title: Incomplete
    template_name: str
    order: int
    def get_context_data(self, parent_context): ...

class ChecksSidePanel(BaseSidePanel):
    class SidePanelToggle(BaseSidePanel.SidePanelToggle):
        aria_label: Incomplete
        icon_name: str
    name: str
    title: Incomplete
    template_name: str
    order: int
    def get_axe_configuration(self): ...
    def get_context_data(self, parent_context): ...

class PreviewSidePanel(BaseSidePanel):
    class SidePanelToggle(BaseSidePanel.SidePanelToggle):
        aria_label: Incomplete
        icon_name: str
        has_counter: bool
        keyboard_shortcut: str
    name: str
    title: Incomplete
    template_name: str
    order: int
    preview_url: Incomplete
    def __init__(self, object, request, *, preview_url) -> None: ...
    @property
    def auto_update_interval(self): ...
    def get_context_data(self, parent_context): ...
