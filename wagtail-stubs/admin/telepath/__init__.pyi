from _typeshed import Incomplete
from telepath import Adapter as Adapter, AdapterRegistry, JSContextBase

class WagtailJSContextBase(JSContextBase):
    @property
    def base_media(self) -> Incomplete: ...

class WagtailAdapterRegistry(AdapterRegistry):
    js_context_base_class: type[WagtailJSContextBase]

registry: WagtailAdapterRegistry
JSContext: type[WagtailJSContextBase]

def register(*args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
def adapter(js_constructor: str, base: type[Adapter] = ...) -> Incomplete: ...
