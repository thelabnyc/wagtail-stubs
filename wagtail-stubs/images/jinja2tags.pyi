from jinja2.ext import Extension

from .models import Filter as Filter
from .models import Picture as Picture
from .models import ResponsiveImage as ResponsiveImage
from .shortcuts import (
    get_rendition_or_not_found as get_rendition_or_not_found,
)
from .shortcuts import (
    get_renditions_or_not_found as get_renditions_or_not_found,
)
from .templatetags.wagtailimages_tags import image_url as image_url

def image(image, filterspec, **attrs): ...
def srcset_image(image, filterspec, **attrs): ...
def picture(image, filterspec, **attrs): ...

class WagtailImagesExtension(Extension):
    def __init__(self, environment) -> None: ...

images = WagtailImagesExtension
