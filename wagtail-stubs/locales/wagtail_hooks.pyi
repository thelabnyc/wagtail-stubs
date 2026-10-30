from wagtail import hooks as hooks
from wagtail.admin.menu import MenuItem as MenuItem
from wagtail.permissions import policy_registry as policy_registry

from .views import LocaleViewSet as LocaleViewSet

def register_viewset(): ...

class LocalesMenuItem(MenuItem):
    def is_shown(self, request): ...

def register_locales_menu_item(): ...
