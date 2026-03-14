from collections.abc import Iterable

from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property

class SpecificMixin:
    def get_specific(
        self,
        deferred: bool = False,
        copy_attrs: Iterable[str] | None = None,
        copy_attrs_exclude: Iterable[str] | None = None,
    ) -> SpecificMixin: ...
    @cached_property
    def specific(self) -> SpecificMixin: ...
    @cached_property
    def specific_deferred(self) -> SpecificMixin: ...
    @cached_property
    def specific_class(self) -> type[SpecificMixin] | None: ...
    @property
    def cached_content_type(self) -> ContentType: ...
