from wagtail.admin.forms.collections import CollectionViewRestrictionForm as CollectionViewRestrictionForm
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.models.media import Collection as Collection
from wagtail.models.media import CollectionViewRestriction as CollectionViewRestriction
from wagtail.permissions import collection_permission_policy as collection_permission_policy

def set_privacy(request, collection_id): ...
