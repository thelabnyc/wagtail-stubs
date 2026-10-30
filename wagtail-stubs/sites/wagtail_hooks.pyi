from wagtail import hooks as hooks
from wagtail.admin.menu import MenuItem as MenuItem
from wagtail.models import Site as Site
from wagtail.permissions import policy_registry as policy_registry

from .views import SiteViewSet as SiteViewSet

def register_viewset(): ...

class SitesMenuItem(MenuItem):
    def is_shown(self, request): ...

def register_sites_menu_item(): ...
