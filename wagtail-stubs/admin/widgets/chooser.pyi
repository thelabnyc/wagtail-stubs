from typing import Any

from django import forms
from django.db import models
from django.forms import widgets
from django.utils.functional import cached_property as cached_property
from django.utils.safestring import SafeString

from wagtail.widget_adapters import WidgetAdapter

class BaseChooser(widgets.Input):
    choose_one_text: str
    choose_another_text: str
    clear_choice_text: str
    link_to_chosen_text: str
    show_edit_link: bool
    show_clear_link: bool
    template_name: str
    display_title_key: str
    icon: str | None
    classname: str | None
    model: type[models.Model] | None
    js_constructor: str
    linked_fields: dict[str, str | dict[str, str]]
    input_type: str
    is_hidden: bool
    def __init__(self, **kwargs: Any) -> None: ...
    @cached_property
    def model_class(self) -> type[models.Model]: ...
    def value_from_datadict(self, data: dict[str, Any], files: dict[str, Any], name: str) -> Any: ...
    def get_hidden_input_context(self, name: str, value: Any, attrs: dict[str, Any] | None) -> dict[str, Any]: ...
    def render_hidden_input(self, name: str, value: Any, attrs: dict[str, Any] | None) -> str: ...
    def get_chooser_modal_url(self) -> str: ...
    def get_context(self, name: str, value_data: dict[str, Any], attrs: dict[str, Any] | None) -> dict[str, Any]: ...
    def render_html(self, name: str, value_data: dict[str, Any] | None, attrs: dict[str, Any] | None) -> str: ...
    def get_instance(self, value: Any) -> models.Model | None: ...
    def get_display_title(self, instance: models.Model) -> str: ...
    def get_value_data_from_instance(self, instance: models.Model) -> dict[str, Any]: ...
    def get_value_data(self, value: Any) -> dict[str, Any] | None: ...
    def render(self, name: str, value: Any, attrs: dict[str, Any] | None = None, renderer: Any = None) -> SafeString: ...
    @property
    def base_js_init_options(self) -> dict[str, Any]: ...
    def get_js_init_options(self, id_: str, name: str, value_data: dict[str, Any] | None) -> dict[str, Any]: ...
    def render_js_init(self, id_: str, name: str, value_data: dict[str, Any] | None) -> str: ...
    @cached_property
    def media(self) -> forms.Media: ...

class BaseChooserAdapter(WidgetAdapter):
    js_constructor: str
    def js_args(self, widget: BaseChooser) -> list[Any]: ...
    @cached_property
    def media(self) -> forms.Media: ...

class AdminPageChooser(BaseChooser):
    choose_one_text: str
    choose_another_text: str
    link_to_chosen_text: str
    display_title_key: str
    chooser_modal_url_name: str
    icon: str
    classname: str
    js_constructor: str
    user_perms: str | None
    target_models: list[type[models.Model]]
    can_choose_root: bool
    def __init__(
        self,
        target_models: list[type[models.Model] | str] | None = None,
        can_choose_root: bool = False,
        user_perms: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    @property
    def model_names(self) -> list[str]: ...
    @property
    def base_js_init_options(self) -> dict[str, Any]: ...
    def get_instance(self, value: Any) -> models.Model | None: ...
    def get_display_title(self, instance: models.Model) -> str: ...
    def get_value_data_from_instance(self, instance: models.Model) -> dict[str, Any]: ...
    def get_js_init_options(self, id_: str, name: str, value_data: dict[str, Any] | None) -> dict[str, Any]: ...
    @property
    def media(self) -> forms.Media: ...  # type: ignore[override]

class PageChooserAdapter(BaseChooserAdapter):
    js_constructor: str
    @cached_property
    def media(self) -> forms.Media: ...

class AdminPageMoveChooser(AdminPageChooser):
    pages_to_move: list[Any]
    def __init__(
        self,
        target_models: list[type[models.Model] | str] | None = None,
        can_choose_root: bool = False,
        user_perms: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    @property
    def base_js_init_options(self) -> dict[str, Any]: ...
