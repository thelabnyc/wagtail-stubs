from typing import overload

from django.http import HttpRequest
from rest_framework.request import Request
from wagtail.models import AbstractPage
from wagtail.models import Page as _StockPage
from wagtail.query import PageQuerySet

Page: type[AbstractPage]

@overload
def get_public_pages_queryset[P: AbstractPage](request: HttpRequest | Request, model: type[P]) -> PageQuerySet[P]: ...
@overload
def get_public_pages_queryset(
    request: HttpRequest | Request, model: type[_StockPage] = ...
) -> PageQuerySet[_StockPage]: ...
