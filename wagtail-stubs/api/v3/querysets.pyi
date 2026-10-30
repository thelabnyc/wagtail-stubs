from typing import overload

from django.http import HttpRequest
from wagtail.models import AbstractPage
from wagtail.query import PageQuerySet

Page: type[AbstractPage]

@overload
def get_pages_queryset[P: AbstractPage](request: HttpRequest, model: type[P]) -> PageQuerySet[P]: ...
@overload
def get_pages_queryset(request: HttpRequest, model: type[AbstractPage] = ...) -> PageQuerySet[AbstractPage]: ...
