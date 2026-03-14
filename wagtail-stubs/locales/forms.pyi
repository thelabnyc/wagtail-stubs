from typing import Any

from django import forms
from wagtail.coreutils import get_content_languages as get_content_languages
from wagtail.models import Locale as Locale

class LocaleForm(forms.ModelForm):
    required_css_class: str
    language_code: forms.ChoiceField
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    class Meta:
        model = Locale
        fields: list[str]
