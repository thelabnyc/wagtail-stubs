from jinja2.ext import Extension

from .templatetags.wagtailuserbar import wagtailuserbar as wagtailuserbar

class WagtailUserbarExtension(Extension):
    def __init__(self, environment) -> None: ...

userbar = WagtailUserbarExtension
