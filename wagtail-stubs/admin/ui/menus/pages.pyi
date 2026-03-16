from django.utils.functional import cached_property
from wagtail.admin.ui.menus import MenuItem as MenuItem
from wagtail.models import Page

class PageMenuItem(MenuItem):
    url_name: str | None
    label: str | None
    icon_name: str | None
    priority: int | None
    link_rel: None
    page: Page
    next_url: str | None
    def __init__(
        self,
        label: str | None = None,
        url: str | None = None,
        icon_name: str | None = None,
        priority: int | None = None,
        *,
        page: Page,
        next_url: str | None = None,
    ) -> None: ...
    @cached_property
    def url(self) -> str | None: ...
