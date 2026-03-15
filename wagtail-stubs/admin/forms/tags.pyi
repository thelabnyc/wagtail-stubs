from typing import Any

from taggit.forms import TagField as TaggitTagField
from taggit.models import TagBase
from wagtail.admin.widgets import AdminTagWidget

def validate_tag_length(
    value: list[str],
    max_tag_length: int = ...,
) -> None: ...

class TagField(TaggitTagField):
    widget: type[AdminTagWidget]
    tag_model: type[TagBase]
    free_tagging: bool
    def __init__(
        self, *args: Any, tag_model: type[TagBase] | None = ..., free_tagging: bool | None = ..., **kwargs: Any
    ) -> None: ...
    def clean(self, value: str) -> list[str]: ...
