from datetime import datetime
from typing import Any

from django.http import HttpRequest, HttpResponseRedirect
from ninja import Field, Router, Schema, Status
from ninja.params.models import Query as _QueryParam
from wagtail.api.v3.pagination import WagtailLimitOffsetPagination
from wagtail.api.v3.schemas.params import OrderingSchema
from wagtail.contrib.redirects.models import Redirect

BASE_REDIRECT_READ_FIELDS: list[str]
router: Router

class RedirectSchema(Schema):
    id: int
    old_path: str
    site_id: int | None
    is_permanent: bool
    redirect_page_id: int | None
    redirect_page_route_path: str
    redirect_link: str
    automatically_created: bool
    created_at: datetime | None
    location: str | None = Field(alias="link")  # noqa: PYI015

class RedirectInputSchema(Schema):
    old_path: str
    site: int | None = ...
    is_permanent: bool = ...
    redirect_page: int | None = Field(None, alias="redirect_page_id")  # noqa: PYI015
    redirect_page_route_path: str = ...
    redirect_link: str = ...

def list_redirects(
    request: HttpRequest,
    *,
    ordering: OrderingSchema | _QueryParam = ...,
    ninja_pagination: WagtailLimitOffsetPagination.Input | None = None,
    **kwargs: Any,
) -> dict[str, Any]: ...
def find_redirect(
    request: HttpRequest, id: int | None = None, html_path: str | None = None
) -> HttpResponseRedirect: ...
def get_redirect_detail(request: HttpRequest, redirect_id: int) -> Redirect: ...
def create_redirect(request: HttpRequest, data: RedirectInputSchema) -> Status[Redirect]: ...
def update_redirect(request: HttpRequest, redirect_id: int, data: RedirectInputSchema) -> Redirect: ...
def delete_redirect(request: HttpRequest, redirect_id: int) -> Status[None]: ...
