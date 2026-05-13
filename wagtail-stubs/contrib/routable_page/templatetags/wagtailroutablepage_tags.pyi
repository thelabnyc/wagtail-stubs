from typing import Any

from django import template
from wagtail.contrib.routable_page.models import RoutablePage
from wagtail.models.sites import Site as Site

register: template.Library

def routablepageurl(
    context: template.Context | dict[str, Any], page: RoutablePage | None, url_name: str, *args: Any, **kwargs: Any
) -> str: ...
def routablefullpageurl(
    context: template.Context | dict[str, Any], page: RoutablePage | None, url_name: str, *args: Any, **kwargs: Any
) -> str: ...
