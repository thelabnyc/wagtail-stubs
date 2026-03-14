from django.db import models

class LogEntryQuerySet(models.QuerySet["BaseLogEntry"]): ...

class BaseLogEntryManager(models.Manager["BaseLogEntry"]):
    def get_queryset(self) -> LogEntryQuerySet: ...

class BaseLogEntry(models.Model):
    class Meta:
        abstract: bool

class ModelLogEntry(BaseLogEntry): ...
