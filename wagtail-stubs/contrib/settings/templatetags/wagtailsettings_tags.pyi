from _typeshed import Incomplete
from django.template import Node
from wagtail.contrib.settings.context_processors import SettingProxy as SettingProxy
from wagtail.models.sites import Site as Site

register: Incomplete

class SettingsNode(Node):
    @staticmethod
    def get_settings_object(context, use_default_site: bool = False): ...
    kwargs: Incomplete
    target_var: Incomplete
    def __init__(self, kwargs, target_var) -> None: ...
    def render(self, context): ...

@register.tag
def get_settings(parser, token): ...
