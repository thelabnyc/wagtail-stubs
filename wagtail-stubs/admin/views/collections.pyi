from _typeshed import Incomplete
from wagtail import hooks as hooks
from wagtail.admin import messages as messages
from wagtail.admin.forms.collections import CollectionForm as CollectionForm
from wagtail.admin.ui.tables import TitleColumn as TitleColumn
from wagtail.admin.views.generic import CreateView as CreateView, DeleteView as DeleteView, EditView as EditView, IndexView as IndexView
from wagtail.models import Collection as Collection
from wagtail.permissions import collection_permission_policy as collection_permission_policy

class Index(IndexView):
    permission_policy = collection_permission_policy
    model = Collection
    context_object_name: str
    results_template_name: str
    add_url_name: str
    index_url_name: str
    page_title: Incomplete
    add_item_label: Incomplete
    header_icon: str
    columns: Incomplete
    def get_queryset(self): ...
    def get_table(self, object_list): ...

class Create(CreateView):
    permission_policy = collection_permission_policy
    model = Collection
    form_class = CollectionForm
    page_title: Incomplete
    success_message: Incomplete
    add_url_name: str
    edit_url_name: str
    index_url_name: str
    header_icon: str
    def get_form(self, form_class=None): ...
    def save_instance(self): ...

class Edit(EditView):
    permission_policy = collection_permission_policy
    model = Collection
    form_class = CollectionForm
    template_name: str
    success_message: Incomplete
    error_message: Incomplete
    edit_url_name: str
    index_url_name: str
    delete_url_name: str
    context_object_name: str
    header_icon: str
    def get_queryset(self): ...
    def get_form(self, form_class=None): ...
    def save_instance(self): ...

class Delete(DeleteView):
    permission_policy = collection_permission_policy
    model = Collection
    success_message: Incomplete
    index_url_name: str
    edit_url_name: str
    delete_url_name: str
    page_title: Incomplete
    confirmation_message: Incomplete
    header_icon: str
    def get_queryset(self): ...
    def get_collection_contents(self): ...
    template_name: str
    def get_context_data(self, **kwargs): ...
    object: Incomplete
    def post(self, request, pk): ...
