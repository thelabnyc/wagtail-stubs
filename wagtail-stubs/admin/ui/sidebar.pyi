from collections.abc import Mapping
from typing import Any

from django import forms
from django.contrib.auth.models import AbstractBaseUser
from django.utils.functional import _StrOrPromise
from django.utils.functional import cached_property as cached_property
from wagtail.admin.search import SearchArea
from wagtail.admin.staticfiles import versioned_static as versioned_static
from wagtail.telepath import Adapter as Adapter
from wagtail.telepath import adapter as adapter

class BaseSidebarAdapter(Adapter):
    @cached_property
    def media(self) -> forms.Media: ...

class MenuItem:
    name: str
    label: _StrOrPromise
    icon_name: str
    classname: str
    attrs: Mapping[str, Any]
    def __init__(
        self, name: str, label: _StrOrPromise, icon_name: str = "", classname: str = "", attrs: Mapping[str, Any] = None
    ) -> None: ...
    def js_args(self) -> list[dict[str, Any]]: ...

class LinkMenuItem(MenuItem):
    url: str
    def __init__(
        self,
        name: str,
        label: _StrOrPromise,
        url: str,
        icon_name: str = "",
        classname: str = "",
        attrs: Mapping[str, Any] = None,
    ) -> None: ...
    def js_args(self) -> list[dict[str, Any]]: ...
    def __eq__(self, other: object) -> bool: ...

class ActionMenuItem(MenuItem):
    action: str
    method: str
    def __init__(
        self,
        name: str,
        label: _StrOrPromise,
        action: str,
        icon_name: str = "",
        classname: str = "",
        method: str = "POST",
        attrs: Mapping[str, Any] = None,
    ) -> None: ...
    def js_args(self) -> list[dict[str, Any]]: ...
    def __eq__(self, other: object) -> bool: ...

class SubMenuItem(MenuItem):
    menu_items: list[MenuItem]
    footer_text: _StrOrPromise
    def __init__(
        self,
        name: str,
        label: _StrOrPromise,
        menu_items: list[MenuItem],
        icon_name: str = "",
        classname: str = "",
        footer_text: _StrOrPromise = "",
        attrs: Mapping[str, Any] = None,
    ) -> None: ...
    def js_args(self) -> list[dict[str, Any] | list[MenuItem]]: ...
    def __eq__(self, other: object) -> bool: ...

class PageExplorerMenuItem(LinkMenuItem):
    start_page_id: int
    def __init__(
        self,
        name: str,
        label: _StrOrPromise,
        url: str,
        start_page_id: int,
        icon_name: str = "",
        classname: str = "",
        attrs: Mapping[str, Any] = None,
    ) -> None: ...
    def js_args(self) -> list[dict[str, Any] | int]: ...
    def __eq__(self, other: object) -> bool: ...

class WagtailBrandingModule:
    def js_args(self) -> list[str]: ...

class SearchModule:
    search_area: SearchArea
    def __init__(self, search_area: SearchArea) -> None: ...
    def js_args(self) -> list[str]: ...

class MainMenuModule:
    menu_items: list[MenuItem]
    account_menu_items: list[MenuItem]
    user: AbstractBaseUser
    def __init__(
        self, menu_items: list[MenuItem], account_menu_items: list[MenuItem], user: AbstractBaseUser
    ) -> None: ...
    def js_args(self) -> list[list[MenuItem] | dict[str, Any]]: ...
