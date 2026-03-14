import logging

from wagtail.actions.publish_revision import (
    PublishPermissionError as PublishPermissionError,
    PublishRevisionAction,
)

logger: logging.Logger

class PublishPagePermissionError(PublishPermissionError): ...

class PublishPageRevisionAction(PublishRevisionAction):
    def check(self, skip_permission_checks: bool = False) -> None: ...
