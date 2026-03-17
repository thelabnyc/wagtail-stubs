from django.db import models
from django.utils.functional import cached_property as cached_property
from django.views.generic.base import View
from wagtail.admin.auth import PermissionPolicyChecker as PermissionPolicyChecker
from wagtail.admin.modal_workflow import render_modal_workflow as render_modal_workflow
from wagtail.admin.models import popular_tags_for_model as popular_tags_for_model
from wagtail.admin.ui.tables import (
    BaseColumn as BaseColumn,
)
from wagtail.admin.ui.tables import (
    Column as Column,
)
from wagtail.admin.ui.tables import (
    DateColumn as DateColumn,
)
from wagtail.admin.ui.tables import (
    TitleColumn as TitleColumn,
)
from wagtail.admin.ui.tables import (
    UsageCountColumn as UsageCountColumn,
)
from wagtail.admin.views.generic.chooser import (
    BaseChooseView as BaseChooseView,
)
from wagtail.admin.views.generic.chooser import (
    ChooseResultsViewMixin as ChooseResultsViewMixin,
)
from wagtail.admin.views.generic.chooser import (
    ChooseViewMixin as ChooseViewMixin,
)
from wagtail.admin.views.generic.chooser import (
    ChosenMultipleViewMixin as ChosenMultipleViewMixin,
)
from wagtail.admin.views.generic.chooser import (
    ChosenResponseMixin as ChosenResponseMixin,
)
from wagtail.admin.views.generic.chooser import (
    ChosenViewMixin as ChosenViewMixin,
)
from wagtail.admin.views.generic.chooser import (
    CreateViewMixin as CreateViewMixin,
)
from wagtail.admin.views.generic.chooser import (
    CreationFormMixin as CreationFormMixin,
)
from wagtail.admin.views.generic.chooser import (
    PreserveURLParametersMixin as PreserveURLParametersMixin,
)
from wagtail.admin.viewsets.chooser import ChooserViewSet as ChooserViewSet
from wagtail.images import get_image_model as get_image_model
from wagtail.images.formats import get_image_format as get_image_format
from wagtail.images.forms import ImageInsertionForm as ImageInsertionForm
from wagtail.images.forms import get_image_form as get_image_form
from wagtail.images.permissions import permission_policy as permission_policy
from wagtail.images.utils import find_image_duplicates as find_image_duplicates
from wagtail.models.reference_index import ReferenceIndex as ReferenceIndex

permission_checker: PermissionPolicyChecker

class ImageChosenResponseMixin(ChosenResponseMixin):
    def get_chosen_response_data(self, image, preview_image_filter: str = "max-165x165"): ...

class ImageCreationFormMixin(CreationFormMixin):
    creation_tab_id: str
    create_action_label: str
    create_action_clicked_label: str
    permission_policy = permission_policy
    def get_creation_form_class(self): ...
    def get_creation_form_kwargs(self): ...

class BaseImageChooseView(BaseChooseView):
    template_name: str
    results_template_name: str
    ordering: str
    construct_queryset_hook_name: str
    @property
    def per_page(self): ...
    def get_object_list(self): ...
    def filter_object_list(self, objects): ...
    def get_filter_form(self): ...
    @cached_property
    def collections(self): ...
    model: type[models.Model]
    def get(self, request): ...
    def get_usage_counts(self, results): ...
    def get_context_data(self, **kwargs): ...
    @cached_property
    def layout(self): ...
    @cached_property
    def columns(self): ...

class ImagePreviewColumn(BaseColumn):
    cell_template_name: str

class TitleColumnWithFilename(TitleColumn):
    cell_template_name: str

class ImageChooseViewMixin(ChooseViewMixin):
    def get_context_data(self, **kwargs): ...

class ImageChooseView(ImageChooseViewMixin, ImageCreationFormMixin, BaseImageChooseView): ...
class ImageChooseResultsView(ChooseResultsViewMixin, ImageCreationFormMixin, BaseImageChooseView): ...

class ImageChosenView(ChosenViewMixin, ImageChosenResponseMixin, View):
    model: type[models.Model]
    def get(self, request, *args, pk, **kwargs): ...

class ImageChosenMultipleView(ChosenMultipleViewMixin, ImageChosenResponseMixin, View):
    model: type[models.Model]
    def get(self, request, *args, **kwargs): ...

class SelectFormatResponseMixin(PreserveURLParametersMixin):
    def render_select_format_response(self, image, form): ...

class ImageUploadViewMixin(SelectFormatResponseMixin, CreateViewMixin):
    model: type[models.Model]
    def get(self, request): ...
    form: ImageInsertionForm
    def post(self, request): ...
    def render_duplicate_found_response(self, request, new_image, existing_image): ...

class ImageUploadView(ImageUploadViewMixin, ImageCreationFormMixin, ImageChosenResponseMixin, View): ...

class ImageSelectFormatView(SelectFormatResponseMixin, ImageChosenResponseMixin, View):
    model: type[models.Model] | None
    def get(self, request, image_id): ...
    def get_chosen_response_data(self, image): ...
    form: ImageInsertionForm
    def post(self, request, image_id): ...

class ImageChooserViewSet(ChooserViewSet):
    choose_view_class = ImageChooseView
    choose_results_view_class = ImageChooseResultsView
    chosen_view_class = ImageChosenView
    chosen_multiple_view_class = ImageChosenMultipleView
    create_view_class = ImageUploadView
    select_format_view_class = ImageSelectFormatView
    permission_policy = permission_policy
    register_widget: bool
    preserve_url_parameters: list[str]
    icon: str
    choose_one_text: str
    create_action_label: str
    create_action_clicked_label: str
    choose_another_text: str
    edit_item_text: str
    @property
    def select_format_view(self): ...
    def get_urlpatterns(self): ...

viewset: ImageChooserViewSet
