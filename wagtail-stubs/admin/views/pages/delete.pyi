from wagtail import hooks as hooks
from wagtail.actions.delete_page import DeletePageAction as DeletePageAction
from wagtail.admin import messages as messages
from wagtail.admin.utils import get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.admin.views.pages.utils import type_to_delete_confirmation as type_to_delete_confirmation
from wagtail.models import Page as Page
from wagtail.models import ReferenceIndex as ReferenceIndex

def delete(request, page_id): ...
