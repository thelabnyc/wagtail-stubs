from _typeshed import Incomplete
from django.utils.functional import cached_property as cached_property
from wagtail.admin.staticfiles import versioned_static as versioned_static
from wagtail.admin.telepath import register as register
from wagtail.admin.widgets import BaseChooser as BaseChooser, BaseChooserAdapter as BaseChooserAdapter
from wagtail.admin.widgets.button import Button as Button
from wagtail.utils.deprecation import RemovedInWagtail80Warning as RemovedInWagtail80Warning

class AdminSnippetChooser(BaseChooser):
    display_title_key: str
    classname: str
    js_constructor: str
    model: Incomplete
    choose_one_text: Incomplete
    choose_another_text: Incomplete
    link_to_chosen_text: Incomplete
    def __init__(self, model, **kwargs) -> None: ...
    def get_chooser_modal_url(self): ...
    @cached_property
    def media(self): ...

class SnippetChooserAdapter(BaseChooserAdapter):
    js_constructor: str
    @cached_property
    def media(self): ...

class SnippetListingButton(Button):
    def __init__(self, *args, **kwargs) -> None: ...
