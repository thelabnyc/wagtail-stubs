from typing import Any

from django.db import models
from taggit.forms import TagWidget

class AdminTagWidget(TagWidget):
    template_name: str
    tag_model: type[models.Model]
    free_tagging: bool | None
    def __init__(
        self,
        *args: Any,
        tag_model: type[models.Model] = ...,
        free_tagging: bool | None = None,
        **kwargs: Any,
    ) -> None: ...
    def get_context(self, name: str, value: str | None, attrs: dict[str, Any] | None) -> dict[str, Any]: ...
