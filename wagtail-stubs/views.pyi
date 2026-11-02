from typing import Any

from django.http import HttpRequest, HttpResponse
from wagtail.models.pages import AbstractPage

Page: type[AbstractPage]

def serve_chain(page: AbstractPage, request: HttpRequest, args: list[Any], kwargs: dict[str, Any]) -> HttpResponse: ...
def serve(request: HttpRequest, path: str) -> HttpResponse: ...
def authenticate_with_password(request: HttpRequest, page_view_restriction_id: int, page_id: int) -> HttpResponse: ...
