from datetime import datetime
from uuid import UUID

from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from wagtail.models import Revision

from .base import BaseSchema

class ContentTypeSchema(BaseSchema):
    id: int
    name: str
    label: str
    @staticmethod
    def resolve_name(obj: ContentType) -> str: ...
    @staticmethod
    def resolve_label(obj: ContentType) -> str: ...

class RevisionSchema(BaseSchema):
    id: int
    object_id: str
    created_at: datetime
    user_id: int | str | UUID | None = ...
    object_str: str
    approved_go_live_at: datetime | None = ...

class RevisionDetailSchema(RevisionSchema):
    content_type: ContentTypeSchema
    base_content_type: ContentTypeSchema
    @staticmethod
    def resolve_content_object(obj: Revision) -> Model: ...
