from wagtail.admin.forms.pages import PageViewRestrictionForm as PageViewRestrictionForm
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.models import Page as Page, PageViewRestriction as PageViewRestriction
from wagtail.models.view_restrictions import BaseViewRestriction as BaseViewRestriction

def set_privacy(request, page_id): ...
