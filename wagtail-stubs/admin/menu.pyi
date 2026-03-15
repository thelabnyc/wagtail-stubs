from django.forms import Media, MediaDefiningClass
from django.http import HttpRequest
from django.utils.functional import cached_property as cached_property
from wagtail.admin.ui.sidebar import LinkMenuItem as LinkMenuItemComponent
from wagtail.admin.ui.sidebar import SubMenuItem as SubMenuItemComponent

class MenuItem(metaclass=MediaDefiningClass):
    label: str
    url: str
    classname: str
    icon_name: str
    name: str
    attrs: dict[str, str]
    order: int
    def __init__(
        self,
        label: str,
        url: str,
        name: str | None = None,
        classname: str = "",
        icon_name: str = "",
        attrs: dict[str, str] | None = None,
        order: int = 1000,
    ) -> None: ...
    def is_shown(self, request: HttpRequest) -> bool: ...
    def render_component(self, request: HttpRequest) -> LinkMenuItemComponent: ...

class DismissibleMenuItemMixin:
    def __init__(
        self,
        *args: str | Menu,
        name: str | None = None,
        classname: str = "",
        icon_name: str = "",
        attrs: dict[str, str] | None = None,
        order: int = 1000,
    ) -> None: ...
    def render_component(self, request: HttpRequest) -> LinkMenuItemComponent: ...

class DismissibleMenuItem(DismissibleMenuItemMixin, MenuItem): ...

class Menu:
    register_hook_name: str | None
    construct_hook_name: str | None
    initial_menu_items: list[MenuItem] | None
    def __init__(
        self,
        register_hook_name: str | None = None,
        construct_hook_name: str | None = None,
        items: list[MenuItem] | None = None,
    ) -> None: ...
    @cached_property
    def registered_menu_items(self) -> list[MenuItem]: ...
    def menu_items_for_request(self, request: HttpRequest) -> list[MenuItem]: ...
    @property
    def media(self) -> Media: ...
    def render_component(self, request: HttpRequest) -> list[LinkMenuItemComponent | SubMenuItemComponent]: ...

class SubmenuMenuItem(MenuItem):
    menu: Menu
    def __init__(
        self,
        label: str,
        menu: Menu,
        *,
        name: str | None = None,
        classname: str = "",
        icon_name: str = "",
        attrs: dict[str, str] | None = None,
        order: int = 1000,
    ) -> None: ...
    def is_shown(self, request: HttpRequest) -> bool: ...
    def render_component(self, request: HttpRequest) -> SubMenuItemComponent: ...  # type: ignore[override]

class DismissibleSubmenuMenuItem(DismissibleMenuItemMixin, SubmenuMenuItem): ...

class AdminOnlyMenuItem(MenuItem):
    def is_shown(self, request: HttpRequest) -> bool: ...

class WagtailMenuRegisterable:
    menu_icon: str
    menu_label: str
    menu_name: str
    menu_order: int
    menu_url: str | None
    add_to_admin_menu: bool
    add_to_settings_menu: bool
    @cached_property
    def menu_item_class(self) -> type[MenuItem]: ...
    def get_menu_item(self, order: int | None = None) -> MenuItem: ...
    @cached_property
    def menu_hook(self) -> str | None: ...
    def register_menu_item(self) -> None: ...

class WagtailMenuRegisterableGroup(WagtailMenuRegisterable):
    items: tuple[type[WagtailMenuRegisterable] | WagtailMenuRegisterable, ...]
    menu_icon: str
    add_to_admin_menu: bool
    registerables: list[WagtailMenuRegisterable]
    def __init__(self) -> None: ...
    def get_submenu_items(self) -> list[MenuItem]: ...
    def get_menu_item(self, order: int | None = None) -> SubmenuMenuItem: ...  # type: ignore[override]

admin_menu: Menu
settings_menu: Menu
reports_menu: Menu
help_menu: Menu
