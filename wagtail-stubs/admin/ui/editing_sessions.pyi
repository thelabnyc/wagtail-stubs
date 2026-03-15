from collections.abc import Sequence
from typing import Any

from wagtail.admin.models import EditingSession
from wagtail.admin.ui.components import Component as Component

class EditingSessionsModule(Component):
    template_name: str
    current_session: EditingSession
    ping_url: str
    release_url: str
    sessions_list: EditingSessionsList
    revision_id: int | None
    def __init__(
        self,
        current_session: EditingSession,
        ping_url: str,
        release_url: str,
        other_sessions: Sequence[EditingSession],
        revision_id: int | None = None,
    ) -> None: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...

class EditingSessionsList(Component):
    template_name: str
    current_session: EditingSession
    sessions: Sequence[EditingSession]
    def __init__(self, current_session: EditingSession, other_sessions: Sequence[EditingSession]) -> None: ...
    def get_context_data(self, parent_context: dict[str, Any]) -> dict[str, Any]: ...
