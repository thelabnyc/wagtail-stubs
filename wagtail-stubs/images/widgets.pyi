from django.db import models
from django.utils.functional import cached_property as cached_property
from wagtail.admin.staticfiles import versioned_static as versioned_static
from wagtail.admin.widgets import BaseChooser as BaseChooser
from wagtail.admin.widgets import BaseChooserAdapter as BaseChooserAdapter
from wagtail.images import get_image_model as get_image_model
from wagtail.images.shortcuts import get_rendition_or_not_found as get_rendition_or_not_found
from wagtail.telepath import register as register

class AdminImageChooser(BaseChooser):
    choose_one_text: str
    choose_another_text: str
    link_to_chosen_text: str
    template_name: str
    chooser_modal_url_name: str
    icon: str
    classname: str
    js_constructor: str
    model: type[models.Model]
    def __init__(self, **kwargs) -> None: ...
    def get_value_data_from_instance(self, instance): ...
    def get_context(self, name, value_data, attrs): ...
    @property
    def media(self): ...

class ImageChooserAdapter(BaseChooserAdapter):
    js_constructor: str
    @cached_property
    def media(self): ...
