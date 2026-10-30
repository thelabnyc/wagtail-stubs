from collections.abc import Iterable
from typing import Any

from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from django.db.models import Model
from django.forms import BaseForm
from django.utils.datastructures import MultiValueDict
from pydantic import BaseModel
from wagtail.admin.forms.models import WagtailAdminModelForm
from wagtail.admin.forms.pages import WagtailAdminPageForm
from wagtail.blocks import Block
from wagtail.models import AbstractPage

Page: type[AbstractPage]

def filter_form_options(
    model: type[Model],
    form_options: dict[str, Any],
    writable_fields: Iterable[str],
) -> dict[str, Any]: ...
def get_api_form_class(model: type[Model], field_names: Iterable[str] | None = None) -> type[WagtailAdminModelForm]: ...
def build_page_form(
    model: type[AbstractPage],
    parent: AbstractPage,
    data: BaseModel,
    user: AbstractBaseUser | AnonymousUser,
) -> WagtailAdminPageForm: ...
def build_page_update_form(
    page: AbstractPage,
    data: BaseModel,
    user: AbstractBaseUser | AnonymousUser,
) -> WagtailAdminPageForm: ...
def build_model_form(
    model: type[Model],
    data: BaseModel,
    user: AbstractBaseUser | AnonymousUser,
) -> WagtailAdminModelForm: ...
def build_model_update_form(
    instance: Model,
    data: BaseModel,
    user: AbstractBaseUser | AnonymousUser,
) -> WagtailAdminModelForm: ...
def get_warnings(data: MultiValueDict[str, Any]) -> list[Any]: ...
def add_warnings(data: MultiValueDict[str, Any], warnings: list[Any]) -> None: ...
def flatten_block_value(block: Block, value: Any, prefix: str, data: MultiValueDict[str, Any]) -> None: ...
def build_form_data(
    form_class: type[BaseForm],
    payload: dict[str, Any],
    instance: Model | None = None,
) -> MultiValueDict[str, Any]: ...
