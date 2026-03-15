from collections.abc import Callable
from typing import Any

from django.core.checks import CheckMessage
from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse
from wagtail.models import Page
from wagtail.url_routing import RouteResult

def re_path(pattern: str, name: str | None = None) -> Callable[..., Any]: ...
def path(pattern: str, name: str | None = None) -> Callable[..., Any]: ...

route = re_path

class RoutablePageMixin:
    def index_route(self, request: HttpRequest, *args: Any, **kwargs: Any) -> TemplateResponse: ...
    @classmethod
    def get_subpage_urls(cls) -> list[Any]: ...
    @classmethod
    def get_resolver(cls) -> Any: ...
    @classmethod
    def check(cls, **kwargs: Any) -> list[CheckMessage]: ...
    def reverse_subpage(
        self, name: str, args: list[Any] | None = None, kwargs: dict[str, Any] | None = None
    ) -> str: ...
    def resolve_subpage(self, path: str) -> RouteResult: ...
    def route(self, request: HttpRequest, path_components: list[str]) -> RouteResult: ...
    def serve(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def render(
        self,
        request: HttpRequest,
        *args: Any,
        template: str | None = None,
        context_overrides: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> TemplateResponse: ...
    def serve_preview(self, request: HttpRequest, mode_name: str) -> HttpResponse: ...

class RoutablePage(RoutablePageMixin, Page):
    class Meta:
        abstract: bool
