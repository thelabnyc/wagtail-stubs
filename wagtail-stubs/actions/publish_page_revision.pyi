from _typeshed import Incomplete
from wagtail.actions.publish_revision import PublishPermissionError as PublishPermissionError, PublishRevisionAction as PublishRevisionAction
from wagtail.signals import page_published as page_published

logger: Incomplete

class PublishPagePermissionError(PublishPermissionError): ...

class PublishPageRevisionAction(PublishRevisionAction):
    def check(self, skip_permission_checks: bool = False): ...
