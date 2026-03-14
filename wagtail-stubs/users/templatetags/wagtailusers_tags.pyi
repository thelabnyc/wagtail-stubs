from django import template
from django.contrib.auth.models import Permission
from wagtail.admin.models import Admin as Admin
from wagtail.users.permission_order import get_content_type_order_lookup as get_content_type_order_lookup

register: template.Library

def normalize_permission_label(permission: Permission): ...

VIEW_PERMISSION_LABEL: str

def format_permissions(permission_bound_field): ...
