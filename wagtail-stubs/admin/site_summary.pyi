from _typeshed import Incomplete
from wagtail import hooks as hooks
from wagtail.admin.auth import user_has_any_page_permission as user_has_any_page_permission
from wagtail.admin.navigation import get_site_for_user as get_site_for_user
from wagtail.admin.ui.components import Component as Component
from wagtail.models import Page as Page, Site as Site

class SummaryItem(Component):
    order: int
    request: Incomplete
    def __init__(self, request) -> None: ...
    def is_shown(self): ...

class PagesSummaryItem(SummaryItem):
    order: int
    template_name: str
    def get_context_data(self, parent_context): ...
    def is_shown(self): ...

class SiteSummaryPanel(Component):
    template_name: str
    request: Incomplete
    summary_items: Incomplete
    def __init__(self, request) -> None: ...
    def get_context_data(self, parent_context): ...
    @property
    def media(self): ...
