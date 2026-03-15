from wagtail import hooks as hooks
from wagtail.admin.admin_url_finder import (
    ModelAdminURLFinder as ModelAdminURLFinder,
)
from wagtail.admin.admin_url_finder import (
    register_admin_url_finder as register_admin_url_finder,
)
from wagtail.admin.menu import MenuItem as MenuItem
from wagtail.contrib.redirects import urls as urls
from wagtail.contrib.redirects.permissions import permission_policy as permission_policy

from .models import Redirect as Redirect

def register_admin_urls(): ...

class RedirectsMenuItem(MenuItem):
    def is_shown(self, request): ...

def register_redirects_menu_item(): ...
def register_permissions(): ...

class RedirectAdminURLFinder(ModelAdminURLFinder):
    edit_url_name: str
    permission_policy = permission_policy
