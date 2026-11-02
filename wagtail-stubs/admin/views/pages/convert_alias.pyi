from typing import Any, Generic

from django.http import HttpRequest, HttpResponseBase
from django.views.generic.base import TemplateView
from typing_extensions import TypeVar
from wagtail import hooks as hooks
from wagtail.actions.convert_alias import ConvertAliasPageAction as ConvertAliasPageAction
from wagtail.admin import messages as messages
from wagtail.admin.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.models import AbstractPage

Page: type[AbstractPage]
_PageT = TypeVar("_PageT", bound=AbstractPage, default=AbstractPage)

class ConvertAliasView(TemplateView, Generic[_PageT]):
    template_name: str
    page: _PageT
    next_url: str
    def dispatch(self, request: HttpRequest, page_id: int, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
