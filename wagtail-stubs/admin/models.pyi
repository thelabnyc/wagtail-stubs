from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from wagtail.admin import panels as panels
from wagtail.models import Page as Page

class Admin(models.Model):
    class Meta:
        default_permissions: list[str]
        permissions: list[tuple[str, str]]

def get_object_usage(obj): ...
def popular_tags_for_model(model, count: int = 10): ...

class EditingSession(models.Model):
    user: models.ForeignKey
    content_type: models.ForeignKey
    object_id: models.CharField
    content_object: GenericForeignKey
    last_seen_at: models.DateTimeField
    is_editing: models.BooleanField
    @staticmethod
    def cleanup() -> None: ...
    class Meta:
        indexes: list[models.Index]
