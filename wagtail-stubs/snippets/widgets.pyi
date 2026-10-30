from typing import Any

from django.db import models
from django.utils.functional import cached_property as cached_property
from wagtail.admin.staticfiles import versioned_static as versioned_static
from wagtail.admin.telepath import register as register
from wagtail.admin.widgets import BaseChooser as BaseChooser
from wagtail.admin.widgets import BaseChooserAdapter as BaseChooserAdapter

class AdminSnippetChooser(BaseChooser):
    display_title_key: str
    classname: str
    js_constructor: str
    model: type[models.Model]
    choose_one_text: str
    choose_another_text: str
    link_to_chosen_text: str
    def __init__(self, model: type[models.Model] | None = None, **kwargs: Any) -> None: ...
    def get_chooser_modal_url(self): ...
    @cached_property
    def media(self): ...

class SnippetChooserAdapter(BaseChooserAdapter):
    js_constructor: str
    @cached_property
    def media(self): ...
