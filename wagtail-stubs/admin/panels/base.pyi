from typing import Any
import functools

from django.db import models
from django.forms import Form
from django.http import HttpRequest
from django.utils.functional import _StrOrPromise
from django.utils.safestring import SafeString
from wagtail.admin.compare import ChildRelationComparison, FieldComparison
from wagtail.admin.forms.models import WagtailAdminModelForm
from wagtail.admin.ui.components import Component

def get_form_for_model(
    model: type[models.Model],
    form_class: type[WagtailAdminModelForm] = ...,
    **kwargs: str | list[str] | dict[str, str] | set[str],
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
        heading: _StrOrPromise = "",
        classname: str = "",
        help_text: _StrOrPromise = "",
        base_form_class: type[Form] | None = None,
        icon: str = "",
        attrs: dict[str, str] | None = None,
    ) -> None: ...
    def clone(self) -> Panel: ...
    def clone_kwargs(self) -> dict[str, str | type[Form] | dict[str, str] | None]: ...
    def get_form_options(self) -> dict[str, list[str] | dict[str, str] | set[str]]: ...
    def get_form_class(self) -> type[WagtailAdminModelForm]: ...
    def bind_to_model(self, model: type[models.Model]) -> Panel: ...
    def get_bound_panel(
        self,
        instance: models.Model | None = None,
        request: HttpRequest | None = None,
        form: Form | None = None,
        prefix: str = "panel",
    ) -> Panel.BoundPanel: ...
    def on_model_bound(self) -> None: ...
    def classes(self) -> list[str]: ...
    def id_for_label(self) -> str: ...
    @property
    def clean_name(self) -> str: ...
    def format_value_for_display(self, value: Any) -> str | Any: ...

    class BoundPanel(Component):
        panel: Panel
        instance: models.Model | None
        request: HttpRequest | None
        form: Form | None
        prefix: str
        heading: str
        help_text: str

        def __init__(
            self,
            panel: Panel,
            instance: models.Model | None,
            request: HttpRequest | None,
            form: Form | None,
            prefix: str,
        ) -> None: ...
        @property
        def classname(self) -> str: ...
        def classes(self) -> list[str]: ...
        @property
        def attrs(self) -> dict[str, str]: ...
        @property
        def icon(self) -> str: ...
        def id_for_label(self) -> str: ...
        def is_shown(self) -> bool: ...
        def show_panel_furniture(self) -> bool: ...
        def is_required(self) -> bool: ...
        def get_context_data(self, parent_context: dict[str, Any] | None = None) -> dict[str, Any]: ...
        def get_comparison(
            self,
        ) -> list[functools.partial[FieldComparison] | functools.partial[ChildRelationComparison]]: ...
        def render_missing_fields(self) -> SafeString: ...
        def render_form_content(self) -> SafeString: ...
