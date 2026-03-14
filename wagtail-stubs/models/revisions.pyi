from typing import Any

from django.db import models

class RevisionQuerySet(models.QuerySet["Revision"]): ...
class RevisionsManager(models.Manager["Revision"]): ...
class PageRevisionsManager(RevisionsManager): ...

class Revision(models.Model):
    content_type: models.ForeignKey[Any, Any]
    object_id: models.CharField[str, str]
    created_at: models.DateTimeField[Any, Any]
    user: models.ForeignKey[Any, Any]
    content: models.JSONField[Any, Any]
    approved_go_live_at: models.DateTimeField[Any, Any]
    objects: RevisionsManager  # type: ignore[assignment]

class RevisionMixin(models.Model):
    class Meta:
        abstract: bool
