from collections.abc import Mapping
from typing import Any

from django.contrib.sitemaps import Sitemap as DjangoSitemap
from django.http import HttpRequest
from django.template.response import TemplateResponse

from .sitemap_generator import Sitemap as Sitemap

type _SitemapsArg = Mapping[str, type[DjangoSitemap[Any]] | DjangoSitemap[Any]]

def index(request: HttpRequest, sitemaps: _SitemapsArg, **kwargs: Any) -> TemplateResponse: ...
def sitemap(
    request: HttpRequest, sitemaps: _SitemapsArg | None = None, alternates: bool | None = None, **kwargs: Any
) -> TemplateResponse: ...
def prepare_sitemaps(
    request: HttpRequest, sitemaps: _SitemapsArg, alternates: bool = False
) -> dict[str, type[DjangoSitemap[Any]] | DjangoSitemap[Any]]: ...
