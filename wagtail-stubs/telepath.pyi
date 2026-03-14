from collections.abc import Callable
from typing import Any

from django import forms
from telepath import Adapter, AdapterRegistry, JSContextBase

class WagtailJSContextBase(JSContextBase):
    @property
    def base_media(self) -> forms.Media: ...

class WagtailAdapterRegistry(AdapterRegistry):
    js_context_base_class: type[WagtailJSContextBase]

registry: WagtailAdapterRegistry
JSContext: type

def register(adapter: Adapter, cls: type) -> None: ...
def adapter(js_constructor: str, base: type[Adapter] = ...) -> Callable[[type], type]: ...
