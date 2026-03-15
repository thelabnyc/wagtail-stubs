from collections.abc import Sequence

from django.db import models

from .base import Panel

def extract_panel_definitions_from_model_class(
    model: type[models.Model], exclude: list[str] | None = None
) -> list[Panel]: ...
def get_edit_handler(model: type[models.Model]) -> Panel: ...
def expand_panel_list(model: type[models.Model], panels: Sequence[Panel | str]) -> list[Panel]: ...
