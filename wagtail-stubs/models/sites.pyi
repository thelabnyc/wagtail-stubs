from typing import Any, NamedTuple

from django.db import models
from django.http import HttpRequest

class SiteRootPath(NamedTuple):
    site_id: int
    root_path: str
    root_url: str
    language_code: str

class SiteManager(models.Manager["Site"]):
    def get_queryset(self) -> models.QuerySet[Site]: ...

class Site(models.Model):
    hostname: models.CharField[str, str]
    port: models.IntegerField[int, int]
    site_name: models.CharField[str, str]
    root_page: models.ForeignKey[Any, Any]
    is_default_site: models.BooleanField[bool, bool]
    objects: SiteManager  # type: ignore[assignment]

    @staticmethod
    def find_for_request(request: HttpRequest) -> Site | None: ...
    @classmethod
    def get_site_root_paths(cls) -> list[SiteRootPath]: ...
    @staticmethod
    def clear_site_root_paths_cache() -> None: ...
    def natural_key(self) -> tuple[str, int]: ...

class GroupSitePermission(models.Model): ...
