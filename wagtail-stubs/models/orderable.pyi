from django.db import models

class Orderable(models.Model):
    sort_order: models.IntegerField[int | None, int | None]
    sort_order_field: str
    class Meta:
        abstract: bool
        ordering: list[str]

def set_max_order(instance: models.Model, sort_order_field: str) -> None: ...
