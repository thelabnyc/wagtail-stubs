from collections.abc import Iterable
from typing import Any

from django import forms
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from django.db.models import Model
from django.forms import BaseForm, BaseModelForm
from django.forms.utils import _DataT, _FilesT
from django.utils.datastructures import MultiValueDict
from pydantic import BaseModel
from wagtail.blocks import Block
from wagtail.models import AbstractPage

Page: type[AbstractPage]

def filter_form_options(
    model: type[Model],
    form_options: dict[str, Any],
    writable_fields: Iterable[str],
) -> dict[str, Any]: ...
def get_api_form_class[M: Model](
    model: type[M], field_names: Iterable[str] | None = None
) -> type[BaseModelForm[M]]: ...
def build_page_form[P: AbstractPage](
    model: type[P],
    parent: AbstractPage,
    data: BaseModel,
    user: AbstractBaseUser | AnonymousUser,
) -> BaseModelForm[P]: ...
def build_page_update_form[P: AbstractPage](
    page: P,
    data: BaseModel,
    user: AbstractBaseUser | AnonymousUser,
) -> BaseModelForm[P]: ...
def build_model_form[M: Model](
    model: type[M],
    data: BaseModel,
    user: AbstractBaseUser | AnonymousUser,
) -> BaseModelForm[M]: ...
def build_model_update_form[M: Model](
    instance: M,
    data: BaseModel,
    user: AbstractBaseUser | AnonymousUser,
) -> BaseModelForm[M]: ...
def get_warnings(data: MultiValueDict[str, Any]) -> list[Any]: ...
def add_warnings(data: MultiValueDict[str, Any], warnings: list[Any]) -> None: ...

class APIBlockWidget(forms.Widget):
    def value_from_datadict(self, data: _DataT, files: _FilesT, name: str) -> Any: ...
    def value_omitted_from_data(self, data: _DataT, files: _FilesT, name: str) -> bool: ...

def use_api_block_widgets(form_class: type[BaseForm]) -> None: ...
def to_prep_block_value(block: Block, value: Any, prefix: str, data: MultiValueDict[str, Any]) -> Any: ...
def to_native_block_value(block: Block, value: Any, prefix: str, data: MultiValueDict[str, Any]) -> Any: ...
def build_form_data(
    form_class: type[BaseForm],
    payload: dict[str, Any],
    instance: Model | None = None,
) -> MultiValueDict[str, Any]: ...
