from collections.abc import Mapping, Sequence
from typing import Any

from django.contrib.auth.models import AbstractBaseUser
from django.forms import Media
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView
from wagtail import hooks as hooks
from wagtail.admin.forms.search import SearchForm as SearchForm
from wagtail.admin.icons import get_icons as get_icons
from wagtail.admin.navigation import get_site_for_user as get_site_for_user
from wagtail.admin.site_summary import SiteSummaryPanel as SiteSummaryPanel
from wagtail.admin.ui.components import Component as Component
from wagtail.admin.views.generic import WagtailAdminTemplateMixin as WagtailAdminTemplateMixin
from wagtail.models.content_types import get_default_page_content_type as get_default_page_content_type
from wagtail.models.pages import Page as Page
from wagtail.models.pages import PageLogEntry as PageLogEntry
from wagtail.models.revisions import Revision as Revision
from wagtail.models.workflows import TaskState as TaskState
from wagtail.models.workflows import WorkflowState as WorkflowState
from wagtail.permissions import page_permission_policy as page_permission_policy

User: type[AbstractBaseUser]

class UpgradeNotificationPanel(Component):
    template_name: str
    dismissible_id: str
    def get_upgrade_check_setting(self) -> bool | str: ...
    def upgrade_check_lts_only(self) -> bool: ...
    def get_dismissible_value(self, user: AbstractBaseUser) -> str | None: ...
    def get_context_data(self, parent_context: Mapping[str, Any]) -> dict[str, Any]: ...
    def render_html(self, parent_context: Mapping[str, Any] = None) -> str: ...

class WhatsNewInWagtailVersionPanel(Component):
    name: str
    template_name: str
    order: int
    def get_whats_new_banner_setting(self) -> bool | str: ...
    def get_dismissible_id(self) -> str: ...
    def get_context_data(self, parent_context: Mapping[str, Any]) -> dict[str, Any]: ...
    def is_shown(self, parent_context: Mapping[str, Any] = None) -> bool: ...
    def render_html(self, parent_context: Mapping[str, Any] = None) -> str: ...

class UserObjectsInWorkflowModerationPanel(Component):
    name: str
    template_name: str
    order: int
    def get_context_data(self, parent_context: Mapping[str, Any]) -> dict[str, Any]: ...

class WorkflowObjectsToModeratePanel(Component):
    name: str
    template_name: str
    order: int
    def get_context_data(self, parent_context: Mapping[str, Any]) -> dict[str, Any]: ...

class LockedPagesPanel(Component):
    name: str
    template_name: str
    order: int
    def get_context_data(self, parent_context: Mapping[str, Any]) -> dict[str, Any]: ...

class RecentEditsPanel(Component):
    name: str
    template_name: str
    order: int
    def get_context_data(self, parent_context: Mapping[str, Any]) -> dict[str, Any]: ...

class HomeView(WagtailAdminTemplateMixin, TemplateView):
    template_name: str
    page_title: str
    permission_policy = page_permission_policy
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_media(self, panels: Sequence[Component] | None = None) -> Media: ...
    def get_panels(self) -> list[Component]: ...
    def get_site_details(self) -> dict[str, Any]: ...

def error_test(request: HttpRequest) -> None: ...
def default(request: HttpRequest) -> None: ...
def sprite(request: HttpRequest) -> HttpResponse: ...
