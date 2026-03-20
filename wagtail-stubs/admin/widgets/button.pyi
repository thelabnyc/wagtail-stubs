from typing import Any

from django.contrib.auth.models import AbstractBaseUser
from django.utils.functional import _StrOrPromise, cached_property
from wagtail.admin.ui.components import Component
from wagtail.models.pages import Page, PagePermissionTester

class Button(Component):
    template_name: str
    show: bool
    label: _StrOrPromise
    icon_name: str | None
    url: str | None
    attrs: dict[str, str]
    classname: str
    priority: int
    def __init__(
        self,
        label: _StrOrPromise = "",
        url: str | None = None,
        classname: str = "",
        icon_name: str | None = None,
        attrs: dict[str, str] = ...,
        priority: int = 1000,
    ) -> None: ...
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

class HeaderButton(Button):
    def __init__(
        self,
        label: _StrOrPromise = "",
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
        label: _StrOrPromise = "",
        url: str | None = None,
        classname: str = "",
        *,
        icon_name: str | None = None,
        attrs: dict[str, str] = ...,
        priority: int = 1000,
    ) -> None: ...

class PageListingButton(ListingButton):
    aria_label_format: str | None
    url_name: str | None
    page: Page | None
    user: AbstractBaseUser | None
    next_url: str | None
    def __init__(
        self,
        label: _StrOrPromise = "",
        url: str | None = None,
        classname: str = "",
        *,
        page: Page | None = None,
        next_url: str | None = None,
        attrs: dict[str, str] = ...,
        user: AbstractBaseUser | None = None,
        icon_name: str | None = None,
        priority: int = 1000,
    ) -> None: ...
    @cached_property
    def url(self) -> str | None: ...  # type: ignore[override]
    @cached_property
    def page_perms(self) -> PagePermissionTester | None: ...

class BaseDropdownMenuButton(Button):
    template_name: str
    def __init__(
        self,
        label: _StrOrPromise = "",
        *,
        classname: str = "",
        icon_name: str | None = None,
        attrs: dict[str, str] = ...,
        priority: int = 1000,
    ) -> None: ...
    @cached_property
    def dropdown_buttons(self) -> list[Button]: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class ButtonWithDropdown(BaseDropdownMenuButton):
    def __init__(
        self,
        label: _StrOrPromise = "",
        *,
        buttons: list[Button] = ...,
        classname: str = "",
        icon_name: str | None = None,
        attrs: dict[str, str] = ...,
        priority: int = 1000,
    ) -> None: ...

class ButtonWithDropdownFromHook(BaseDropdownMenuButton):
    hook_name: str
    page: Page
    user: AbstractBaseUser
    next_url: str | None
    def __init__(
        self,
        label: _StrOrPromise,
        hook_name: str,
        page: Page,
        user: AbstractBaseUser,
        next_url: str | None = None,
        *,
        classname: str = "",
        icon_name: str | None = None,
        attrs: dict[str, str] = ...,
        priority: int = 1000,
    ) -> None: ...
    @property
    def show(self) -> bool: ...  # type: ignore[override]
    @cached_property
    def dropdown_buttons(self) -> list[Button]: ...
