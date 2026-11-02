from typing import Any

from django.http import HttpRequest, HttpResponse
from django.views.generic.base import View
from wagtail.models import AbstractPage

Page: type[AbstractPage]

class SetPagePositionView(View):
    def post(self, request: HttpRequest, page_to_move_id: int, *args: Any, **kwargs: Any) -> HttpResponse: ...
