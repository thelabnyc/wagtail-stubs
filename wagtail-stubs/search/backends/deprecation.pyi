from wagtail.utils.deprecation import RemovedInWagtail80Warning as RemovedInWagtail80Warning

class IndexOptionMixin:
    def __init__(self, params) -> None: ...

class LegacyContentTypeMatchMixin:
    def get_content_type_filter(self): ...
