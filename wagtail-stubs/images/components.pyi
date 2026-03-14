from wagtail.admin.ui.fields import BaseFieldDisplay as BaseFieldDisplay
from wagtail.images.shortcuts import get_rendition_or_not_found as get_rendition_or_not_found

class ImageDisplay(BaseFieldDisplay):
    rendition_spec: str
    def render_html(self, parent_context): ...
