from typing import Any

from django.http import HttpRequest
from ninja import Router, Schema, Status
from wagtail.api.v3.schemas import BaseSchema
from wagtail.models import Locale

router: Router

class LocaleSchema(BaseSchema):
    id: int
    language_code: str
    display_name: str
    is_bidi: bool
    is_default: bool
    @staticmethod
    def resolve_display_name(obj: Locale) -> str: ...

class LocaleInputSchema(Schema):
    language_code: str

def _check_can_delete(locale: Locale) -> None: ...
def list_locales(request: HttpRequest) -> dict[str, Any]: ...
def get_locale_detail(request: HttpRequest, locale_id: int) -> Locale: ...
def create_locale(request: HttpRequest, data: LocaleInputSchema) -> Status[Locale]: ...
def update_locale(request: HttpRequest, locale_id: int, data: LocaleInputSchema) -> Locale: ...
def delete_locale(request: HttpRequest, locale_id: int) -> Status[None]: ...
