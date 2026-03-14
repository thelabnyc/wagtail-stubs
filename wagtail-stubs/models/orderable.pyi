from django.db import models

class Orderable(models.Model):
    sort_order: models.IntegerField[int | None, int | None]
    class Meta:
        abstract: bool
        ordering: list[str]
