from typing import Any

from django.db.models import Model
from django.http import HttpRequest
from wagtail.admin.ui.components import Component as Component
from wagtail.admin.userbar import AccessibilityItem as AccessibilityItem
from wagtail.admin.userbar import apply_userbar_hooks as apply_userbar_hooks
from wagtail.locks import BaseLock
from wagtail.models import (
    DraftStateMixin as DraftStateMixin,
)
from wagtail.models import (
    Locale,
)
from wagtail.models import (
    LockableMixin as LockableMixin,
)
from wagtail.models import (
    Page as Page,
)
from wagtail.models import (
    ReferenceIndex as ReferenceIndex,
)
from wagtail.models.view_restrictions import BaseViewRestriction as BaseViewRestriction

class BaseSidePanel(Component):
    class SidePanelToggle(Component):
        template_name: str
        aria_label: str
        icon_name: str
        has_counter: bool
        counter_classname: str
        keyboard_shortcut: str | None
        panel: BaseSidePanel
        def __init__(self, panel: BaseSidePanel) -> None: ...
        def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

    object: Model
    request: HttpRequest
    model: type[Model]
    toggle: BaseSidePanel.SidePanelToggle
    def __init__(self, object: Model, request: HttpRequest) -> None: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class StatusSidePanel(BaseSidePanel):
    class SidePanelToggle(BaseSidePanel.SidePanelToggle):
        aria_label: str
        icon_name: str
        counter_classname: str
        def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

    name: str
    title: str
    template_name: str
    order: int
    show_schedule_publishing_toggle: bool | None
    live_object: Model | None
    scheduled_object: Model | None
    locale: Locale | None
    translations: list[dict[str, Any]] | None
    usage_url: str | None
    history_url: str | None
    last_updated_info: dict[str, Any] | None
    locking_enabled: bool
    def __init__(
        self,
        *args: Any,
        show_schedule_publishing_toggle: bool | None = None,
        live_object: Model | None = None,
        scheduled_object: Model | None = None,
        locale: Locale | None = None,
        translations: list[dict[str, Any]] | None = None,
        usage_url: str | None = None,
        history_url: str | None = None,
        last_updated_info: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None: ...
    def get_status_templates(self, context: dict[str, Any]) -> list[str]: ...
    def get_scheduled_publishing_context(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    lock: BaseLock | None
    def get_lock_context(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    def get_usage_context(self) -> dict[str, Any]: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class PageStatusSidePanel(StatusSidePanel):
    parent_page: Page | None
    usage_url: str
    history_url: str | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_status_templates(self, context: dict[str, Any]) -> list[str]: ...
    def get_usage_context(self) -> dict[str, Any]: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class CommentsSidePanel(BaseSidePanel):
    class SidePanelToggle(BaseSidePanel.SidePanelToggle):
        aria_label: str
        icon_name: str

    name: str
    title: str
    template_name: str
    order: int
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class ChecksSidePanel(BaseSidePanel):
    class SidePanelToggle(BaseSidePanel.SidePanelToggle):
        aria_label: str
        icon_name: str

    name: str
    title: str
    template_name: str
    order: int
    def get_axe_configuration(self) -> dict[str, Any] | None: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class PreviewSidePanel(BaseSidePanel):
    class SidePanelToggle(BaseSidePanel.SidePanelToggle):
        aria_label: str
        icon_name: str
        has_counter: bool
        keyboard_shortcut: str

    name: str
    title: str
    template_name: str
    order: int
    preview_url: str
    def __init__(self, object: Model, request: HttpRequest, *, preview_url: str) -> None: ...
    @property
    def auto_update_interval(self) -> int: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
