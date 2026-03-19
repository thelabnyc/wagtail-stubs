from typing import Any

from django.forms import Media

class Feature:
    js: list[str]
    css: dict[str, list[str]]

    def __init__(self, js: list[str] | None = None, css: dict[str, list[str]] | None = None) -> None: ...
    @property
    def media(self) -> Media: ...
    def construct_options(self, options: dict[str, Any]) -> None: ...

class BooleanFeature(Feature):
    option_name: str
    def __init__(self, option_name: str, **kwargs: Any) -> None: ...
    def construct_options(self, options: dict[str, Any]) -> None: ...

class ListFeature(Feature):
    option_name: str
    data: dict[str, Any]

    def __init__(self, data: dict[str, Any], **kwargs: Any) -> None: ...
    def construct_options(self, options: dict[str, Any]) -> None: ...

class EntityFeature(ListFeature):
    option_name: str

class BlockFeature(ListFeature):
    option_name: str

class InlineStyleFeature(ListFeature):
    option_name: str

class DecoratorFeature(ListFeature):
    option_name: str

class ControlFeature(ListFeature):
    option_name: str

class PluginFeature(ListFeature):
    option_name: str
