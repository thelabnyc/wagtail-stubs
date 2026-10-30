from wagtail.models import AbstractPage
from wagtail.permissions import policy_registry as policy_registry

Page: type[AbstractPage]

def get_site_for_user(user): ...
