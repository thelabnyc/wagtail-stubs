from typing import Any

from django.db import models
from django.http import HttpRequest, HttpResponse

class PreviewableMixin(models.Model):
    preview_modes: list[tuple[str, str]]
    default_preview_mode: str

    def serve_preview(self, request: HttpRequest, mode_name: str) -> HttpResponse: ...
    def get_preview_context(self, request: HttpRequest, mode_name: str) -> dict[str, Any]: ...
    def get_preview_template(self, request: HttpRequest, mode_name: str) -> str: ...

    class Meta:
        abstract: bool
