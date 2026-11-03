from typing import Any, TypedDict

from django.http import HttpRequest
from ninja import Router
from ninja.pagination import LimitOffsetPagination
from ninja.params.models import Query as _QueryParam
from wagtail.models import AbstractPage
from wagtail.query import PageQuerySet

Page: type[AbstractPage]
router: Router
EXPLORER_PAGE_SIZE: int

class ExplorerPagination(LimitOffsetPagination):
    class Input(LimitOffsetPagination.Input):
        limit: int = ...
        offset: int = ...

def get_explorer_queryset[QS: PageQuerySet[Any]](queryset: QS) -> QS: ...
def get_children[QS: PageQuerySet[Any]](request: HttpRequest, page: AbstractPage, explorable_pages: QS) -> QS: ...
def get_translations[QS: PageQuerySet[Any]](
    page: AbstractPage, explorable_pages: QS
) -> QS | PageQuerySet[AbstractPage]: ...

class _ExplorerChildren(TypedDict):
    count: int
    items: PageQuerySet[AbstractPage]

class _Explorer(TypedDict):
    page: AbstractPage
    translations: PageQuerySet[AbstractPage]
    children: _ExplorerChildren

def explorer(
    request: HttpRequest,
    page_id: int,
    pagination: ExplorerPagination.Input | _QueryParam = ...,
) -> _Explorer: ...
