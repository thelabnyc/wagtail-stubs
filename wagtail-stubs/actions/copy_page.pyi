from _typeshed import Incomplete
from django.core.exceptions import PermissionDenied
from wagtail.log_actions import log as log
from wagtail.models.i18n import TranslatableMixin as TranslatableMixin
from wagtail.signals import page_published as page_published

logger: Incomplete

class CopyPageIntegrityError(RuntimeError): ...
class CopyPagePermissionError(PermissionDenied): ...

class CopyPageAction:
    page: Incomplete
    to: Incomplete
    update_attrs: Incomplete
    exclude_fields: Incomplete
    recursive: Incomplete
    copy_revisions: Incomplete
    keep_live: Incomplete
    user: Incomplete
    process_child_object: Incomplete
    log_action: Incomplete
    reset_translation_key: Incomplete
    def __init__(self, page, to=None, update_attrs=None, exclude_fields=None, recursive: bool = False, copy_revisions: bool = True, keep_live: bool = True, user=None, process_child_object=None, log_action: str = 'wagtail.copy', reset_translation_key: bool = True) -> None: ...
    def generate_translation_key(self, old_uuid): ...
    def check(self, skip_permission_checks: bool = False) -> None: ...
    def execute(self, skip_permission_checks: bool = False): ...
