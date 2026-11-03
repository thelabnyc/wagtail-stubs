from typing import Any, Self

from django.db.models import Field as ModelField
from django.db.models import ForeignObjectRel, Model
from rest_framework.fields import Field
from wagtail.api.v3.fields import FieldSerializer

def get_model_field(model: type[Model], name: str) -> ModelField[Any, Any] | ForeignObjectRel: ...

class APIField:
    name: str
    serializer: Field | FieldSerializer | None
    writable: bool
    def __init__(
        self, name: str, serializer: Field | FieldSerializer | None = None, writable: bool = False
    ) -> None: ...
    def __hash__(self) -> int: ...
    @classmethod
    def get_fields_for_model(cls, model: type[Model], db_fields_only: bool = False) -> list[Self]: ...
    @classmethod
    def get_writable_fields_for_model(cls, model: type[Model]) -> list[Self]: ...
