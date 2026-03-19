from _typeshed import Incomplete
from django import forms
from wagtail.models.i18n import Locale as Locale
from wagtail.models.pages import Page as Page

class CheckboxSelectMultipleWithDisabledOptions(forms.CheckboxSelectMultiple):
    option_template_name: str
    disabled_values: Incomplete
    def create_option(self, *args, **kwargs): ...

class SubmitTranslationForm(forms.Form):
    select_all: Incomplete
    locales: Incomplete
    include_subtree: Incomplete
    show_submit: bool
    def __init__(self, instance, *args, **kwargs) -> None: ...
