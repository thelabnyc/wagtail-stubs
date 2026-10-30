from typing import Any

from django.http import HttpResponse
from ninja import NinjaAPI, Schema
from pydantic import ValidationError

PROBLEM_JSON: str
DEFAULT_PROBLEM_TYPE: str

def as_validation_error(
    exc: Exception,
    message: str | None = None,
    loc: tuple[int | str, ...] = (),
) -> ValidationError: ...

class ProblemDetail(Schema):
    type: str
    title: str
    status: int
    detail: str = ...
    errors: list[dict[str, Any]] | None = ...

def build_problem_detail(
    *,
    status: int,
    title: str | None = None,
    detail: str = "",
    errors: list[dict[str, Any]] | None = None,
    type_uri: str = ...,
) -> ProblemDetail: ...
def problem_response(
    *,
    status: int,
    title: str | None = None,
    detail: str = "",
    errors: list[dict[str, Any]] | None = None,
    type_uri: str = ...,
) -> HttpResponse: ...
def register_exception_handlers(api: NinjaAPI) -> None: ...
