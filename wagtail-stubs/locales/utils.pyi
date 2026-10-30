from wagtail.models import AbstractPage
from wagtail.models.i18n import get_translatable_models as get_translatable_models

Page: type[AbstractPage]

def get_locale_usage(locale): ...
