from _typeshed import Incomplete
from django.db import models
from wagtail.admin import panels as panels
from wagtail.models import Page as Page

class Admin(models.Model):
    class Meta:
        default_permissions: Incomplete
        permissions: Incomplete

def get_object_usage(obj): ...
def popular_tags_for_model(model, count: int = 10): ...

class EditingSession(models.Model):
    user: Incomplete
    content_type: Incomplete
    object_id: Incomplete
    content_object: Incomplete
    last_seen_at: Incomplete
    is_editing: Incomplete
    @staticmethod
    def cleanup() -> None: ...
    class Meta:
        indexes: Incomplete
