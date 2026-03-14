from _typeshed import Incomplete
from django.core.exceptions import PermissionDenied
from wagtail.log_actions import log as log
from wagtail.models.i18n import TranslatableMixin as TranslatableMixin

logger: Incomplete

class CreatePageAliasIntegrityError(RuntimeError): ...
class CreatePageAliasPermissionError(PermissionDenied): ...

class CreatePageAliasAction:
    page: Incomplete
    recursive: Incomplete
    parent: Incomplete
    update_slug: Incomplete
    update_locale: Incomplete
    user: Incomplete
    log_action: Incomplete
    reset_translation_key: Incomplete
    def __init__(self, page, *, recursive: bool = False, parent=None, update_slug=None, update_locale=None, user=None, log_action: str = 'wagtail.create_alias', reset_translation_key: bool = True, _mpnode_attrs=None) -> None: ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False): ...
