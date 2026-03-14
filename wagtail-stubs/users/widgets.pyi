from wagtail.admin.widgets import Button as Button
from wagtail.utils.deprecation import RemovedInWagtail80Warning as RemovedInWagtail80Warning

class UserListingButton(Button):
    def __init__(self, *args, **kwargs) -> None: ...
