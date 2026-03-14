from typing import Any

from django.utils.functional import cached_property as cached_property
from wagtail.admin.ui.menus import MenuItem as MenuItem

class PageMenuItem(MenuItem):
    url_name: str | None
    label: str | None
    icon_name: str | None
    priority: int | None
    link_rel: str
    page: Any
    next_url: str | None
    def __init__(self, label=None, url=None, icon_name=None, priority=None, *, page, next_url=None) -> None: ...
    @cached_property
    def url(self): ...
