from typing import Any

from django.contrib.auth.models import AbstractBaseUser
from django.utils.functional import cached_property
from wagtail.admin.ui.components import Component
from wagtail.admin.ui.menus import MenuItem
from wagtail.models import Page

class BaseButton(Component):
    template_name: str
    show: bool
    label: str
    icon_name: str | None
    url: str | None
    attrs: dict[str, str]
    allow_in_dropdown: bool
    def __init__(
        self,
        label: str = "",
        url: str | None = None,
        classname: str = "",
        icon_name: str | None = None,
        attrs: dict[str, str] = ...,
        priority: int = 1000,
    ) -> None: ...
    @classmethod
    def from_menu_item(cls, menu_item: MenuItem) -> BaseButton: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
    @property
    def base_attrs_string(self) -> str: ...
    @property
    def aria_label(self) -> str: ...
    def __lt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class Button(BaseButton):
    allow_in_dropdown: bool
    classname: str
    priority: int

class HeaderButton(Button):
    def __init__(
        self,
        label: str = "",
        url: str | None = None,
        classname: str = "",
        icon_name: str | None = None,
        attrs: dict[str, str] = ...,
        icon_only: bool = False,
        *,
        priority: int = 1000,
    ) -> None: ...

class ListingButton(Button):
    def __init__(
        self,
        label: str = "",
        url: str | None = None,
        classname: str = "",
        *,
        icon_name: str | None = None,
        attrs: dict[str, str] | None = None,
        priority: int = 1000,
    ) -> None: ...

class PageListingButton(ListingButton):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class BaseDropdownMenuButton(Button):
    template_name: str
    def __init__(
        self,
        label: str = "",
        *,
        classname: str = "",
        icon_name: str | None = None,
        attrs: dict[str, str] | None = None,
        priority: int = 1000,
    ) -> None: ...
    @cached_property
    def dropdown_buttons(self) -> list[Button]: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class ButtonWithDropdown(BaseDropdownMenuButton):
    def __init__(
        self,
        label: str = "",
        *,
        buttons: list[Button] = ...,
        classname: str = "",
        icon_name: str | None = None,
        attrs: dict[str, str] | None = None,
        priority: int = 1000,
    ) -> None: ...

class ButtonWithDropdownFromHook(BaseDropdownMenuButton):
    hook_name: str
    page: Page
    user: AbstractBaseUser
    next_url: str | None
    def __init__(
        self,
        label: str,
        hook_name: str,
        page: Page,
        user: AbstractBaseUser,
        next_url: str | None = None,
        *,
        classname: str = "",
        icon_name: str | None = None,
        attrs: dict[str, str] | None = None,
        priority: int = 1000,
    ) -> None: ...
    @property
    def show(self) -> bool: ...  # type: ignore[override]
    @cached_property
    def dropdown_buttons(self) -> list[Button]: ...
