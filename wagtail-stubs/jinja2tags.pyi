from typing import Any

from jinja2 import Environment
from jinja2.ext import Extension
from markupsafe import Markup

class WagtailCoreExtension(Extension):
    tags: set[str]
    def __init__(self, environment: Environment) -> None: ...
    def parse(self, parser: Any) -> Any: ...
    def parse_include_block(self, parser: Any) -> Any: ...

core = WagtailCoreExtension
