from wagtail import hooks as hooks
from wagtail.admin.menu import MenuItem as MenuItem
from wagtail.contrib.forms import urls as urls
from wagtail.contrib.forms.utils import get_forms_for_user as get_forms_for_user

def register_admin_urls(): ...

class FormsMenuItem(MenuItem):
    def is_shown(self, request): ...

def register_forms_menu_item(): ...
