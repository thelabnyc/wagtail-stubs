from wagtail import hooks as hooks
from wagtail.actions.copy_page import CopyPageAction as CopyPageAction
from wagtail.actions.create_alias import CreatePageAliasAction as CreatePageAliasAction
from wagtail.admin import messages as messages
from wagtail.admin.auth import user_has_any_page_permission as user_has_any_page_permission, user_passes_test as user_passes_test
from wagtail.admin.forms.pages import CopyForm as CopyForm
from wagtail.admin.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.models import Page as Page

def copy(request, page_id): ...
