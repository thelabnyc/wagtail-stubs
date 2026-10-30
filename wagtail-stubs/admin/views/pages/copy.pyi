from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseBase
from django.views.generic.edit import FormView
from wagtail import hooks as hooks
from wagtail.actions.copy_page import CopyPageAction as CopyPageAction
from wagtail.actions.create_alias import CreatePageAliasAction as CreatePageAliasAction
from wagtail.admin import messages as messages
from wagtail.admin.forms.pages import CopyForm as CopyForm
from wagtail.admin.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.models import AbstractPage

Page: type[AbstractPage]

class CopyView(FormView[CopyForm]):
    template_name: str
    page: AbstractPage
    parent_page: AbstractPage | None
    next_url: str
    def dispatch(self, request: HttpRequest, page_id: int, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
    def get_form_class(self) -> type[CopyForm]: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def post(self, request: HttpRequest, page_id: int, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def form_valid(self, form: CopyForm) -> HttpResponse: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
