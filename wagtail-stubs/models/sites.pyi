from collections.abc import Collection
from typing import Any, NamedTuple

from django.contrib.auth.models import Group, Permission
from django.db import models
from django.http import HttpRequest

MATCH_HOSTNAME_PORT: int
MATCH_HOSTNAME_DEFAULT: int
MATCH_DEFAULT: int
MATCH_HOSTNAME: int

SITE_ROOT_PATHS_CACHE_KEY: str
SITE_ROOT_PATHS_CACHE_VERSION: int

def get_site_for_hostname(hostname: str, port: int) -> Site: ...

class SiteRootPath(NamedTuple):
    site_id: int
    root_path: str
    root_url: str
    language_code: str

class SiteManager(models.Manager["Site"]):
    def get_queryset(self) -> models.QuerySet[Site]: ...
    def get_by_natural_key(self, hostname: str, port: int) -> Site: ...

class Site(models.Model):
    hostname: models.CharField[str, str]
    port: models.IntegerField[int, int]
    site_name: models.CharField[str, str]
    # Any, not AbstractPage: the target is the swappable page model, and stock projects rely on it being a Page.
    root_page: models.ForeignKey[Any, Any]
    is_default_site: models.BooleanField[bool, bool]
    objects: SiteManager  # type: ignore[assignment]

    def natural_key(self) -> tuple[str, int]: ...
    def clean(self) -> None: ...
    def clean_fields(self, exclude: Collection[str] | None = None) -> None: ...
    @staticmethod
    def find_for_request(request: HttpRequest) -> Site | None: ...
    @property
    def root_url(self) -> str: ...
    @staticmethod
    def get_site_root_paths() -> list[SiteRootPath]: ...
    @staticmethod
    def clear_site_root_paths_cache() -> None: ...

class GroupSitePermissionManager(models.Manager["GroupSitePermission"]):
    def get_by_natural_key(self, group: Group, site: Site, permission: Permission) -> GroupSitePermission: ...

class GroupSitePermission(models.Model):
    group: models.ForeignKey[Group, Group]
    site: models.ForeignKey[Site, Site]
    permission: models.ForeignKey[Permission, Permission]
    objects: GroupSitePermissionManager  # type: ignore[assignment]

    def natural_key(self) -> tuple[Group, Site, Permission]: ...
