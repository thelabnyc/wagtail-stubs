from _typeshed import Incomplete
from django.db.models import Model
from wagtail import hooks as hooks
from wagtail.models.i18n import Locale as Locale

class SimpleTranslation(Model):
    class Meta:
        default_permissions: Incomplete
        permissions: Incomplete

def after_create_page(request, page) -> None: ...
