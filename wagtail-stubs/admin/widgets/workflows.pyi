from typing import Any

from django import forms

from wagtail.admin.widgets.chooser import BaseChooser

class AdminTaskChooser(BaseChooser):
    choose_one_text: str
    choose_another_text: str
    link_to_chosen_text: str
    icon: str
    chooser_modal_url_name: str
    classname: str
    def render_js_init(self, id_: str, name: str, value_data: dict[str, Any] | None) -> str: ...
    @property
    def media(self) -> forms.Media: ...
