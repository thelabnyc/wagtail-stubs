from _typeshed import Incomplete
from wagtail.admin.ui.components import Component as Component

class EditingSessionsModule(Component):
    template_name: str
    current_session: Incomplete
    ping_url: Incomplete
    release_url: Incomplete
    sessions_list: Incomplete
    revision_id: Incomplete
    revision_created_at: Incomplete
    def __init__(self, current_session, ping_url, release_url, other_sessions, revision_id=None, revision_created_at=None) -> None: ...
    def get_context_data(self, parent_context): ...

class EditingSessionsList(Component):
    template_name: str
    current_session: Incomplete
    sessions: Incomplete
    def __init__(self, current_session, other_sessions) -> None: ...
    def get_context_data(self, parent_context): ...
