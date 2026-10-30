from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseBase
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from wagtail import hooks as hooks
from wagtail.actions.move_page import MovePageAction as MovePageAction
from wagtail.admin import messages as messages
from wagtail.admin.forms.pages import MoveForm as MoveForm
from wagtail.models import AbstractPage
from wagtail.models.pages import PagePermissionTester

Page: type[AbstractPage]

class MoveChooseDestinationView(TemplateView, FormMixin[MoveForm]):
    template_name: str
    form_class = MoveForm
    page_to_move: AbstractPage
    page_perms: PagePermissionTester
    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
    def form_valid(self, form: MoveForm) -> HttpResponse: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...

class MoveConfirmView(TemplateView):
    template_name: str
    page_to_move: AbstractPage
    destination: AbstractPage
    i18n_enabled: bool
    pages_to_move: list[AbstractPage]
    def dispatch(
        self, request: HttpRequest, page_to_move_id: int, destination_id: int, *args: Any, **kwargs: Any
    ) -> HttpResponseBase: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
