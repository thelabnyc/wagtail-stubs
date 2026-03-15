from typing import Any

from django import forms
from wagtail.models import Site as Site

class SiteSwitchForm(forms.Form):
    site: forms.ChoiceField
    def __init__(self, current_site: Site, model: type, **kwargs: Any) -> None: ...
    @classmethod
    def get_change_url(cls, site: Site, model: type) -> str: ...
