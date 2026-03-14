from wagtail import hooks as hooks
from wagtail.actions.convert_alias import ConvertAliasPageAction as ConvertAliasPageAction
from wagtail.admin import messages as messages
from wagtail.admin.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.models import Page as Page

def convert_alias(request, page_id): ...
