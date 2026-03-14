from .templatetags.wagtailcore_tags import fullpageurl as fullpageurl, pageurl as pageurl, richtext as richtext, slugurl as slugurl, wagtail_site as wagtail_site, wagtail_version as wagtail_version
from _typeshed import Incomplete
from jinja2.ext import Extension

class WagtailCoreExtension(Extension):
    tags: Incomplete
    def __init__(self, environment) -> None: ...
    def parse(self, parser): ...
    def parse_include_block(self, parser): ...
core = WagtailCoreExtension
