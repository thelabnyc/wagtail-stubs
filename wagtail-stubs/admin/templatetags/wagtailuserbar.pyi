from django import template
from wagtail.admin.userbar import Userbar as Userbar
from wagtail.models import PAGE_TEMPLATE_VAR as PAGE_TEMPLATE_VAR, Page as Page

register: template.Library

def get_page_instance(context): ...
def wagtailuserbar(context, position: str = 'bottom-right'): ...
