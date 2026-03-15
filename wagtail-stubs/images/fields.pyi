from django.core.validators import FileExtensionValidator
from django.forms.fields import ImageField
from wagtail.images.utils import (
    get_accept_attributes as get_accept_attributes,
)
from wagtail.images.utils import (
    get_allowed_image_extensions as get_allowed_image_extensions,
)

def ImageFileExtensionValidator(value): ...

class WagtailImageField(ImageField):
    default_validators: list[type[FileExtensionValidator]]
    allowed_image_extensions: list[str]
    max_upload_size: int | None
    max_image_pixels: int | None
    max_upload_size_text: str
    supported_formats_text: str
    help_text: str
    def __init__(self, *args, **kwargs) -> None: ...
    def check_image_file_format(self, f) -> None: ...
    def check_image_file_size(self, f) -> None: ...
    def check_image_pixel_size(self, f) -> None: ...
    def to_python(self, data): ...
    def widget_attrs(self, widget): ...
