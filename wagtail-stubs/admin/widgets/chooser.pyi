from typing import Any

from django import forms
from django.forms import widgets

from wagtail.admin.telepath import Adapter

class BaseChooser(widgets.Input):
    show_edit_link: bool
    show_clear_link: bool
    linked_fields: dict[str, str | dict[str, str]]
    chooser_modal_url_name: str
    icon: str
    classname: str
    model: type | None
    def __init__(self, *args: Any, linked_fields: dict[str, str | dict[str, str]] | None = None, **kwargs: Any) -> None: ...

class BaseChooserAdapter(Adapter): ...

class AdminPageChooser(BaseChooser):
    target_models: list[type] | None
    can_choose_root: bool
    user_perms: str | None
    def __init__(self, target_models: list[type] | None = None, can_choose_root: bool = False, user_perms: str | None = None, **kwargs: Any) -> None: ...

class PageChooserAdapter(BaseChooserAdapter): ...
class AdminPageMoveChooser(AdminPageChooser): ...
