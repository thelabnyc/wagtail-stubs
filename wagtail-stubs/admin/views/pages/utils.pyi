from django.utils.functional import cached_property as cached_property
from wagtail.admin import messages as messages
from wagtail.admin.utils import get_latest_str as get_latest_str, get_valid_next_url_from_request as get_valid_next_url_from_request
from wagtail.permissions import page_permission_policy as page_permission_policy

def get_breadcrumbs_items_for_page(page, user, url_name: str = 'wagtailadmin_explore', root_url_name: str = 'wagtailadmin_explore_root', include_self: bool = True, querystring_value: str = ''): ...

class GenericPageBreadcrumbsMixin:
    breadcrumbs_items_to_take: int
    @cached_property
    def breadcrumbs_items(self): ...
    def get_breadcrumbs_items(self): ...

def type_to_delete_confirmation(request, context=None): ...
