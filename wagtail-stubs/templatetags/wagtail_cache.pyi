from django import template
from django.template.base import FilterExpression, NodeList
from django.template.context import Context
from django.templatetags.cache import CacheNode as DjangoCacheNode

register: template.Library

class WagtailCacheNode(DjangoCacheNode):
    def render(self, context: Context) -> str: ...

class WagtailPageCacheNode(WagtailCacheNode):
    CACHE_SITE_TEMPLATE_VAR: str
    def __init__(
        self,
        nodelist: NodeList,
        expire_time_var: FilterExpression,
        fragment_name: str,
        vary_on: list[FilterExpression],
        cache_name: FilterExpression | None,
    ) -> None: ...
    def render(self, context: Context) -> str: ...

def register_cache_tag(
    tag_name: str,
    node_class: type[WagtailCacheNode],
) -> None: ...
