from ..models import SourceImageIOError as SourceImageIOError
from ..utils import to_svg_safe_spec as to_svg_safe_spec
from rest_framework.fields import Field

class ImageRenditionField(Field):
    filter_spec: str
    preserve_svg: bool
    def __init__(self, filter_spec, preserve_svg: bool = False, *args, **kwargs) -> None: ...
    def to_representation(self, image): ...
