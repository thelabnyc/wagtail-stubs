from django.contrib.auth.models import Group
from django.db import models
from django.http import HttpRequest
from django.utils.functional import _StrOrPromise

class BaseViewRestriction(models.Model):
    NONE: str
    PASSWORD: str
    GROUPS: str
    LOGIN: str

    RESTRICTION_CHOICES: tuple[
        tuple[str, _StrOrPromise],
        tuple[str, _StrOrPromise],
        tuple[str, _StrOrPromise],
        tuple[str, _StrOrPromise],
    ]

    restriction_type: models.CharField[str, str]
    password: models.CharField[str, str]
    groups: models.ManyToManyField[Group, Group]

    def accept_request(self, request: HttpRequest) -> bool: ...
    def mark_as_passed(self, request: HttpRequest) -> None: ...

    class Meta:
        abstract: bool
        verbose_name: _StrOrPromise
        verbose_name_plural: _StrOrPromise
