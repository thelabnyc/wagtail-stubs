from _typeshed import Incomplete
from django.contrib.auth.models import Permission
from wagtail.admin.models import Admin as Admin
from wagtail.users.permission_order import get_content_type_order_lookup as get_content_type_order_lookup

register: Incomplete

def normalize_permission_label(permission: Permission): ...

VIEW_PERMISSION_LABEL: Incomplete

def format_permissions(permission_bound_field): ...
