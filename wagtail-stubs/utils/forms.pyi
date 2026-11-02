from typing import Self, TypeAlias

from django.core.exceptions import ValidationError
from django.forms import BaseForm

FieldPath: TypeAlias = tuple[str | int, ...]  # NOQA:UP040
CodedMessage: TypeAlias = tuple[str, str]  # NOQA:UP040

class FormValidationError(ValidationError):
    loc_errors: list[tuple[FieldPath, list[CodedMessage]]]
    def __init__(self, errors: dict[FieldPath, list[CodedMessage]]) -> None: ...
    @classmethod
    def from_form(cls, form: BaseForm) -> Self: ...
    @classmethod
    def get_form_errors_as_dict(cls, form: BaseForm, path: FieldPath = ()) -> dict[FieldPath, list[CodedMessage]]: ...
