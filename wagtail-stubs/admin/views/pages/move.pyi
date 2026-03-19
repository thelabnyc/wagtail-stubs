from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseBase
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from wagtail import hooks as hooks
from wagtail.actions.move_page import MovePageAction as MovePageAction
from wagtail.admin import messages as messages
from wagtail.admin.forms.pages import MoveForm as MoveForm
from wagtail.models.pages import Page as Page
from wagtail.models.pages import PagePermissionTester

class MoveChooseDestination(TemplateView, FormMixin):
    template_name: str
    form_class = MoveForm
    page_to_move: Page
    page_perms: PagePermissionTester
    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def form_valid(self, form: MoveForm) -> HttpResponseBase: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...

def move_confirm(request: HttpRequest, page_to_move_id: int, destination_id: int) -> HttpResponseBase: ...
