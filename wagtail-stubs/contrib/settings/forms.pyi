from collections.abc import Iterable
from typing import Any

from django import forms
from django.contrib.auth.models import Group, Permission
from django.db.models import QuerySet
from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.models.sites import GroupSitePermission
from wagtail.models.sites import Site as Site

class SiteSwitchForm(forms.Form):
    site: forms.ChoiceField
    def __init__(self, current_site: Site, model: type, sites: Iterable[Site], **kwargs: Any) -> None: ...
    @classmethod
    def get_change_url(cls, site: Site, model: type) -> str: ...

class SitePermissionForm(forms.Form):
    template_name: str
    sites: forms.ModelMultipleChoiceField[Site]
    settings_model: type[BaseSiteSetting]
    permission: Permission
    instance: Group | None
    def __init__(self, *args: Any, instance: Group | None, **kwargs: Any) -> None: ...
    def get_existing_permissions(self) -> QuerySet[GroupSitePermission]: ...
    def as_admin_panel(self) -> str: ...
    def save(self) -> None: ...
