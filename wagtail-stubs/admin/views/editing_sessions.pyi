from django.views.decorators.http import require_POST
from wagtail.admin.models import EditingSession as EditingSession
from wagtail.admin.ui.editing_sessions import EditingSessionsList as EditingSessionsList
from wagtail.admin.utils import get_user_display_name as get_user_display_name
from wagtail.models import (
    Page as Page,
)
from wagtail.models import (
    Revision as Revision,
)
from wagtail.models import (
    RevisionMixin as RevisionMixin,
)
from wagtail.models import (
    WorkflowMixin as WorkflowMixin,
)

@require_POST
def ping(request, app_label, model_name, object_id, session_id): ...
@require_POST
def release(request, session_id): ...
