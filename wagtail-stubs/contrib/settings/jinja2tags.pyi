from _typeshed import Incomplete
from jinja2.ext import Extension
from wagtail.contrib.settings.models import BaseGenericSetting as BaseGenericSetting
from wagtail.contrib.settings.models import BaseSiteSetting as BaseSiteSetting
from wagtail.contrib.settings.registry import registry as registry
from wagtail.models.sites import Site as Site
import jinja2

settings_cache: Incomplete

class SettingContextCache(dict):
    def __missing__(self, key): ...

class Setting(dict):
    site: Incomplete
    def __init__(self, site) -> None: ...
    def __getitem__(self, key): ...
    def __missing__(self, key): ...

@jinja2.pass_context
def get_setting(context, model_string, use_default_site: bool = False): ...

class SettingsExtension(Extension):
    def __init__(self, environment) -> None: ...

settings = SettingsExtension
