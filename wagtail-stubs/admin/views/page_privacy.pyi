from wagtail.admin.forms.pages import PageViewRestrictionForm as PageViewRestrictionForm
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.models.pages import Page as Page
from wagtail.models.pages import PageViewRestriction as PageViewRestriction
from wagtail.models.view_restrictions import BaseViewRestriction as BaseViewRestriction

def set_privacy(request, page_id): ...
