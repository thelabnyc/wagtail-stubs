from .registry import register_setting as register_setting
from _typeshed import Incomplete
from django.db import models
from django.utils.functional import cached_property

__all__ = ['BaseGenericSetting', 'BaseSiteSetting', 'register_setting']

class AbstractSetting(models.Model):
    class Meta:
        abstract: bool
    select_related: Incomplete
    @classmethod
    def base_queryset(cls): ...
    @classmethod
    def get_cache_attr_name(cls): ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def get_permission_policy(cls): ...
    @cached_property
    def page_url(self): ...
    def get_page_url(self, attribute_name, request=None): ...

class BaseSiteSetting(AbstractSetting):
    site: Incomplete
    class Meta:
        abstract: bool
    @classmethod
    def get_permission_policy(cls): ...
    @classmethod
    def for_request(cls, request): ...
    @classmethod
    def for_site(cls, site): ...

class BaseGenericSetting(AbstractSetting):
    class Meta:
        abstract: bool
    @classmethod
    def load(cls, request_or_site=None): ...
