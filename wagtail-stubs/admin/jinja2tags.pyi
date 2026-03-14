from .templatetags.wagtailuserbar import wagtailuserbar as wagtailuserbar
from jinja2.ext import Extension

class WagtailUserbarExtension(Extension):
    def __init__(self, environment) -> None: ...
userbar = WagtailUserbarExtension
