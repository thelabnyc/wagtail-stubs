from _typeshed import Incomplete
from django.utils.functional import cached_property as cached_property
from wagtail.admin.ui.menus import MenuItem as MenuItem

class PageMenuItem(MenuItem):
    url_name: Incomplete
    label: Incomplete
    icon_name: Incomplete
    priority: Incomplete
    link_rel: Incomplete
    page: Incomplete
    next_url: Incomplete
    def __init__(self, label=None, url=None, icon_name=None, priority=None, *, page, next_url=None) -> None: ...
    @cached_property
    def url(self): ...
