from typing import Any, Literal

from rest_framework.fields import Field
from typing_extensions import TypedDict
from wagtail.images.models import AbstractImage

from ..models import SourceImageIOError as SourceImageIOError
from ..utils import to_svg_safe_spec as to_svg_safe_spec

class ImageRenditionDict(TypedDict):
    url: str
    full_url: str
    width: int
    height: int
    alt: str

class ImageRenditionErrorDict(TypedDict):
    error: Literal["SourceImageIOError"]

class ImageRenditionField(Field):
    filter_spec: str
    preserve_svg: bool
    def __init__(self, filter_spec: str, preserve_svg: bool = False, *args: Any, **kwargs: Any) -> None: ...
    def to_representation(self, image: AbstractImage) -> ImageRenditionDict | ImageRenditionErrorDict: ...
