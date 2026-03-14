from typing import Any

from django.http import HttpRequest
from django.utils.functional import cached_property

from wagtail.admin.ui.components import Component
from wagtail.models import Page

class Button(Component):
    template_name: str
    show: bool
    label: str
    icon_name: str | None
    url: str | None
    attrs: dict[str, str]
    classname: str
    priority: int
    def __init__(
        self,
        label: str = "",
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
    def __repr__(self) -> str: ...
    def __lt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class HeaderButton(Button):
    def __init__(
        self,
        label: str = "",
        url: str | None = None,
        classname: str = "",
        icon_name: str | None = None,
        attrs: dict[str, str] = ...,
        icon_only: bool = False,
        **kwargs: Any,
    ) -> None: ...

class ListingButton(Button):
    def __init__(self, label: str = "", url: str | None = None, classname: str = "", **kwargs: Any) -> None: ...

class PageListingButton(ListingButton):
    aria_label_format: str | None
    url_name: str | None
    page: Page | None
    user: Any
    next_url: str | None
    def __init__(self, *args: Any, page: Page | None = None, next_url: str | None = None, attrs: dict[str, str] = ..., user: Any = None, **kwargs: Any) -> None: ...
    @cached_property
    def url(self) -> str | None: ...  # type: ignore[override]
    @cached_property
    def page_perms(self) -> Any: ...

class BaseDropdownMenuButton(Button):
    template_name: str
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @cached_property
    def dropdown_buttons(self) -> list[Button]: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class ButtonWithDropdown(BaseDropdownMenuButton):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class ButtonWithDropdownFromHook(BaseDropdownMenuButton):
    hook_name: str
    page: Page
    user: Any
    next_url: str | None
    def __init__(
        self,
        label: str,
        hook_name: str,
        page: Page,
        user: Any,
        next_url: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    @property
    def show(self) -> bool: ...  # type: ignore[override]
    @cached_property
    def dropdown_buttons(self) -> list[Button]: ...
