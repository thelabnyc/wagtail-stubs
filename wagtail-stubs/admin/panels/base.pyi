from typing import Any

from django.db import models
from django.forms import Form
from django.http import HttpRequest

from wagtail.admin.forms.models import WagtailAdminModelForm

def get_form_for_model(
    model: type[models.Model],
    form_class: type[WagtailAdminModelForm] = ...,
    **kwargs: Any,
) -> type[WagtailAdminModelForm]: ...

class Panel:
    BASE_ATTRS: dict[str, str]
    heading: str
    classname: str
    help_text: str
    base_form_class: type[Form] | None
    icon: str
    model: type[models.Model] | None
    attrs: dict[str, str]

    def __init__(
        self,
        heading: str = "",
        classname: str = "",
        help_text: str = "",
        base_form_class: type[Form] | None = None,
        icon: str = "",
        attrs: dict[str, str] | None = None,
    ) -> None: ...
    def clone(self) -> Panel: ...
    def clone_kwargs(self) -> dict[str, Any]: ...
    def get_form_options(self) -> dict[str, Any]: ...
    def get_form_class(self) -> type[WagtailAdminModelForm]: ...
    def bind_to_model(self, model: type[models.Model]) -> Panel: ...
    def get_bound_panel(self, instance: models.Model | None = None, request: HttpRequest | None = None, form: Form | None = None, prefix: str = "panel") -> Any: ...
    def on_model_bound(self) -> None: ...
    def classes(self) -> set[str]: ...

    class BoundPanel:
        panel: Panel
        instance: models.Model | None
        request: HttpRequest | None
        form: Form | None
        prefix: str
        def __init__(self, panel: Panel, instance: models.Model | None, request: HttpRequest | None, form: Form | None, prefix: str) -> None: ...
        @property
        def heading(self) -> str: ...
        @property
        def help_text(self) -> str: ...
