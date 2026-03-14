from _typeshed import Incomplete
from django.db import models
from django.utils.functional import cached_property as cached_property
from wagtail.models import Page as Page, Site as Site

class Redirect(models.Model):
    old_path: Incomplete
    site: Incomplete
    is_permanent: Incomplete
    redirect_page: Incomplete
    redirect_page_route_path: Incomplete
    redirect_link: Incomplete
    automatically_created: Incomplete
    created_at: Incomplete
    @property
    def title(self): ...
    @cached_property
    def link(self): ...
    def old_links(self, site_root_paths=None): ...
    def get_is_permanent_display(self): ...
    @classmethod
    def get_for_site(cls, site=None): ...
    @staticmethod
    def add_redirect(old_path, redirect_to=None, is_permanent: bool = True, page_route_path=None, site=None, automatically_created: bool = False): ...
    @staticmethod
    def normalise_path(url, decode_unicode: bool = True): ...
    @staticmethod
    def normalise_page_route_path(url): ...
    def clean(self) -> None: ...
    class Meta:
        verbose_name: Incomplete
        verbose_name_plural: Incomplete
        unique_together: Incomplete
