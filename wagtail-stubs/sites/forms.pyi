from django import forms
from wagtail.admin.widgets import AdminPageChooser as AdminPageChooser
from wagtail.models.sites import Site as Site

class SiteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None: ...
    required_css_class: str
    class Meta:
        model = Site
        fields: tuple[str, ...]
