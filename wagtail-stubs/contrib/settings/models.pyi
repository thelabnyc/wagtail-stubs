from typing import Any

from django.db import models
from django.http import HttpRequest
from django.utils.functional import cached_property
from wagtail.coreutils import InvokeViaAttributeShortcut
from wagtail.models.sites import Site

from .registry import register_setting as register_setting

__all__ = ["BaseGenericSetting", "BaseSiteSetting", "register_setting"]

class AbstractSetting(models.Model):
    class Meta:
        abstract: bool

    select_related: list[str] | None
    @classmethod
    def base_queryset(cls): ...
    @classmethod
    def get_cache_attr_name(cls) -> str: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @cached_property
    def page_url(self) -> InvokeViaAttributeShortcut: ...
    def get_page_url(self, attribute_name: str, request: HttpRequest | None = None) -> str: ...

class BaseSiteSetting(AbstractSetting):
    site: models.OneToOneField[Site, Site]
    class Meta:
        abstract: bool

    @classmethod
    def for_request(cls, request: HttpRequest): ...
    @classmethod
    def for_site(cls, site: Site): ...

class BaseGenericSetting(AbstractSetting):
    class Meta:
        abstract: bool

    @classmethod
    def load(cls, request_or_site: HttpRequest | Site | None = None): ...
