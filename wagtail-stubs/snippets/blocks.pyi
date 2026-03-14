from django.utils.functional import cached_property as cached_property
from wagtail.blocks import ChooserBlock as ChooserBlock
from wagtail.coreutils import resolve_model_string as resolve_model_string

class SnippetChooserBlock(ChooserBlock):
    MUTABLE_META_ATTRIBUTES: list[str]
    has_explicit_icon: bool
    def __init__(self, target_model, **kwargs) -> None: ...
    @cached_property
    def target_model(self): ...
    @cached_property
    def widget(self): ...
    class Meta:
        icon: str
