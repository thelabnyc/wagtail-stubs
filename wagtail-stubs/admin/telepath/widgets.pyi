from django.utils.functional import cached_property as cached_property
from wagtail.admin.staticfiles import versioned_static as versioned_static
from wagtail.admin.telepath import Adapter as Adapter, register as register

class WidgetAdapter(Adapter):
    js_constructor: str
    def js_args(self, widget): ...
    def get_media(self, widget): ...
    @cached_property
    def media(self): ...

class CheckboxInputAdapter(WidgetAdapter):
    js_constructor: str

class RadioSelectAdapter(WidgetAdapter):
    js_constructor: str

class SelectAdapter(WidgetAdapter):
    js_constructor: str

class ValidationErrorAdapter(Adapter):
    js_constructor: str
    def js_args(self, error): ...
    @cached_property
    def media(self): ...
