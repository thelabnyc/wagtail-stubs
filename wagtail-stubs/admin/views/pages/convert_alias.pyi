from typing import Any

from django.http import HttpRequest, HttpResponseBase
from django.views.generic.base import TemplateView
from wagtail import hooks as hooks
from wagtail.actions.convert_alias import ConvertAliasPageAction as ConvertAliasPageAction
from wagtail.admin import messages as messages
from wagtail.admin.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.models import AbstractPage

Page: type[AbstractPage]

class ConvertAliasView(TemplateView):
    template_name: str
    page: AbstractPage
    next_url: str
    def dispatch(self, request: HttpRequest, page_id: int, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
