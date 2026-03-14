from .views import SiteViewSet as SiteViewSet
from wagtail import hooks as hooks
from wagtail.admin.menu import MenuItem as MenuItem
from wagtail.permissions import site_permission_policy as site_permission_policy

def register_viewset(): ...

class SitesMenuItem(MenuItem):
    def is_shown(self, request): ...

def register_sites_menu_item(): ...
