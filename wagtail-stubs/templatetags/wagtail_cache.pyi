from _typeshed import Incomplete
from django.templatetags.cache import CacheNode as DjangoCacheNode
from wagtail.models import PAGE_TEMPLATE_VAR as PAGE_TEMPLATE_VAR, Site as Site

register: Incomplete

class WagtailCacheNode(DjangoCacheNode):
    def render(self, context): ...

class WagtailPageCacheNode(WagtailCacheNode):
    CACHE_SITE_TEMPLATE_VAR: str
    def __init__(self, *args, **kwargs) -> None: ...
    def render(self, context): ...

def register_cache_tag(tag_name, node_class): ...
