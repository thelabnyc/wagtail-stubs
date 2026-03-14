from typing import Any

from django.db import models
from taggit.forms import TagWidget

class AdminTagWidget(TagWidget):
    template_name: str
    tag_model: type[models.Model]
    free_tagging: bool | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_context(self, name: str, value: Any, attrs: dict[str, Any] | None) -> dict[str, Any]: ...
