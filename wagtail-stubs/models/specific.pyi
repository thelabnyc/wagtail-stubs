from typing import Any

from django.db import models

class SpecificMixin:
    @property
    def specific(self) -> Any: ...
    @property
    def specific_deferred(self) -> Any: ...
    @property
    def specific_class(self) -> type | None: ...
