from collections.abc import Sequence
from typing import Any

from django.core.files.uploadedfile import UploadedFile
from django.forms.fields import FileField

class WagtailDocumentField(FileField):
    allowed_document_extensions: Sequence[str] | None
    supported_formats_text: str | None
    max_upload_size: int | None
    max_upload_size_text: str
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def check_document_file_size(self, f: UploadedFile) -> None: ...
    def to_python(self, data: Any) -> UploadedFile | None: ...
