from _typeshed import Incomplete
from django.utils.functional import cached_property as cached_property
from wagtail.admin import messages as messages
from wagtail.admin.auth import PermissionPolicyChecker as PermissionPolicyChecker
from wagtail.admin.forms.search import SearchForm as SearchForm
from wagtail.admin.ui.tables import Column as Column
from wagtail.admin.ui.tables import StatusTagColumn as StatusTagColumn
from wagtail.admin.ui.tables import TitleColumn as TitleColumn
from wagtail.admin.views import generic as generic
from wagtail.admin.widgets.button import Button as Button
from wagtail.contrib.frontend_cache.utils import (
    PurgeBatch as PurgeBatch,
)
from wagtail.contrib.frontend_cache.utils import (
    purge_urls_from_cache as purge_urls_from_cache,
)
from wagtail.contrib.redirects.filters import RedirectsReportFilterSet as RedirectsReportFilterSet
from wagtail.contrib.redirects.forms import (
    ConfirmImportForm as ConfirmImportForm,
)
from wagtail.contrib.redirects.forms import (
    ConfirmImportManagementForm as ConfirmImportManagementForm,
)
from wagtail.contrib.redirects.forms import (
    ImportForm as ImportForm,
)
from wagtail.contrib.redirects.forms import (
    RedirectForm as RedirectForm,
)
from wagtail.contrib.redirects.models import Redirect as Redirect
from wagtail.contrib.redirects.permissions import permission_policy as permission_policy
from wagtail.contrib.redirects.utils import (
    get_file_storage as get_file_storage,
)
from wagtail.contrib.redirects.utils import (
    get_format_cls_by_extension as get_format_cls_by_extension,
)
from wagtail.contrib.redirects.utils import (
    get_import_formats as get_import_formats,
)
from wagtail.contrib.redirects.utils import (
    get_supported_extensions as get_supported_extensions,
)
from wagtail.contrib.redirects.utils import (
    write_to_file_storage as write_to_file_storage,
)
from wagtail.log_actions import log as log
from wagtail.models.sites import Site as Site

permission_checker: Incomplete

class RedirectTargetColumn(Column):
    cell_template_name: str
    url_name: str
    def get_value(self, instance): ...
    def get_url(self, instance): ...
    def get_cell_context_data(self, instance, parent_context): ...

class IndexView(generic.IndexView):
    template_name: str
    results_template_name: str
    permission_policy = permission_policy
    model = Redirect
    header_icon: str
    add_item_label: Incomplete
    context_object_name: str
    index_url_name: str
    index_results_url_name: str
    add_url_name: str
    edit_url_name: str
    delete_url_name: str
    default_ordering: str
    paginate_by: int
    page_title: Incomplete
    search_fields: Incomplete
    columns: Incomplete
    filterset_class = RedirectsReportFilterSet
    list_export: Incomplete
    export_headings: Incomplete
    def get_base_queryset(self): ...
    @cached_property
    def header_more_buttons(self) -> list[Button]: ...

class EditView(generic.EditView):
    model = Redirect
    form_class = RedirectForm
    permission_policy = permission_policy
    template_name: str
    index_url_name: str
    edit_url_name: str
    delete_url_name: str
    pk_url_kwarg: str
    error_message: Incomplete
    header_icon: str
    def get_success_message(self): ...
    def save_instance(self): ...

class DeleteView(generic.DeleteView):
    model = Redirect
    pk_url_kwarg: str
    permission_policy = permission_policy
    template_name: str
    index_url_name: str
    delete_url_name: str
    header_icon: str
    def delete_action(self) -> None: ...
    def get_success_message(self): ...

class CreateView(generic.CreateView):
    model = Redirect
    form_class = RedirectForm
    permission_policy = permission_policy
    template_name: str
    add_url_name: str
    index_url_name: str
    edit_url_name: str
    error_message: Incomplete
    header_icon: str
    def get_success_message(self, instance): ...
    def save_instance(self): ...

def start_import(request): ...
def process_import(request): ...
def create_redirects_from_dataset(dataset, config): ...
def to_readable_errors(error): ...
