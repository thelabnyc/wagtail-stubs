from typing import Any

from wagtail.admin.ui.components import Component as Component

class EditingSessionsModule(Component):
    template_name: str
    current_session: Any
    ping_url: str
    release_url: str
    sessions_list: EditingSessionsList
    revision_id: int | None
    revision_created_at: Any
    def __init__(self, current_session, ping_url, release_url, other_sessions, revision_id=None, revision_created_at=None) -> None: ...
    def get_context_data(self, parent_context): ...

class EditingSessionsList(Component):
    template_name: str
    current_session: Any
    sessions: Any
    def __init__(self, current_session, other_sessions) -> None: ...
    def get_context_data(self, parent_context): ...
