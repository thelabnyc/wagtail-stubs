from django.utils.functional import cached_property as cached_property
from wagtail import hooks as hooks
from wagtail.admin.menu import MenuItem as MenuItem
from wagtail.snippets.bulk_actions.delete import DeleteBulkAction as DeleteBulkAction
from wagtail.snippets.permissions import user_can_access_snippets as user_can_access_snippets

def register_admin_urls(): ...

class SnippetsMenuItem(MenuItem):
    def is_shown(self, request): ...

def register_snippets_menu_item(): ...
