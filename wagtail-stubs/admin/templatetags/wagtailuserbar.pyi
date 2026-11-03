from collections.abc import Mapping
from typing import Any

from django import template
from django.template.context import BaseContext
from wagtail.models import AbstractPage

register: template.Library

def get_page_instance(context: BaseContext | Mapping[str, Any]) -> AbstractPage | None: ...
def wagtailuserbar(context: BaseContext | Mapping[str, Any], position: str = "bottom-right") -> str: ...
