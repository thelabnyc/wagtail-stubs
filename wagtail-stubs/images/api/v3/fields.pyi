from wagtail.api.v3.fields import FieldSerializer
from wagtail.images.api.fields import ImageRenditionDict, ImageRenditionErrorDict
from wagtail.images.models import AbstractImage

class ImageRenditionField(FieldSerializer):
    filter_spec: str
    preserve_svg: bool
    def __init__(self, filter_spec: str, preserve_svg: bool = False, *, source: str | None = None) -> None: ...
    def to_representation(self, value: AbstractImage) -> ImageRenditionDict | ImageRenditionErrorDict: ...
