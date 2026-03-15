from collections.abc import Callable

from django.http import HttpResponse
from wagtail.admin.localization import get_localized_response as get_localized_response

js_catalog: Callable[..., HttpResponse]

def localized_js_catalog(request, *args, **kwargs): ...
