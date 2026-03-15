from _typeshed import Incomplete
from wagtail import hooks as hooks
from wagtail.admin.admin_url_finder import (
    ModelAdminURLFinder as ModelAdminURLFinder,
)
from wagtail.admin.admin_url_finder import (
    register_admin_url_finder as register_admin_url_finder,
)
from wagtail.admin.menu import AdminOnlyMenuItem as AdminOnlyMenuItem
from wagtail.admin.menu import MenuItem as MenuItem
from wagtail.contrib.search_promotions import admin_urls as admin_urls
from wagtail.permission_policies import ModelPermissionPolicy as ModelPermissionPolicy

from .models import SearchPromotion as SearchPromotion

def register_admin_urls(): ...

class SearchPicksMenuItem(MenuItem):
    def is_shown(self, request): ...

def register_search_picks_menu_item(): ...
def register_query_search_report_menu_item(): ...
def register_permissions(): ...

class SearchPromotionAdminURLFinder(ModelAdminURLFinder):
    permission_policy: Incomplete
    def construct_edit_url(self, instance): ...
