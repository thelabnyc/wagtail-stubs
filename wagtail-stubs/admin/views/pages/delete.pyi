from typing import Any

from django.http import HttpRequest, HttpResponseBase
from django.views.generic.base import TemplateView
from wagtail import hooks as hooks
from wagtail.actions.delete_page import DeletePageAction as DeletePageAction
from wagtail.admin import messages as messages
from wagtail.admin.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.admin.views.pages.utils import type_to_delete_confirmation as type_to_delete_confirmation
from wagtail.models import AbstractPage
from wagtail.models.reference_index import ReferenceGroups
from wagtail.models.reference_index import ReferenceIndex as ReferenceIndex

Page: type[AbstractPage]

class DeleteView(TemplateView):
    template_name: str
    page: AbstractPage
    wagtail_site_name: str
    next_url: str
    pages_to_delete: list[AbstractPage]
    usage: ReferenceGroups
    def dispatch(self, request: HttpRequest, page_id: int, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...
