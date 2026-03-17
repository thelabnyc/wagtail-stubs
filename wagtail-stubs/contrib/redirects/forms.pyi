from _typeshed import Incomplete
from django import forms
from wagtail.admin.forms.models import WagtailAdminModelForm as WagtailAdminModelForm
from wagtail.admin.widgets import AdminPageChooser as AdminPageChooser
from wagtail.contrib.redirects.models import Redirect as Redirect
from wagtail.models.sites import Site as Site

class RedirectForm(WagtailAdminModelForm):
    site: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    required_css_class: str
    def clean(self) -> None: ...
    class Meta(WagtailAdminModelForm.Meta):
        model = Redirect
        fields: Incomplete

class ImportForm(forms.Form):
    import_file: Incomplete
    def __init__(self, allowed_extensions, *args, **kwargs) -> None: ...

class ConfirmImportManagementForm(forms.Form):
    import_file_name: Incomplete
    input_format: Incomplete
    signer: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def clean(self): ...

class ConfirmImportForm(ConfirmImportManagementForm):
    from_index: Incomplete
    to_index: Incomplete
    site: Incomplete
    permanent: Incomplete
    def __init__(self, headers, *args, **kwargs) -> None: ...
