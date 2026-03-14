from .actions.convert_alias import ConvertAliasPageAPIAction as ConvertAliasPageAPIAction
from .actions.copy import CopyPageAPIAction as CopyPageAPIAction
from .actions.copy_for_translation import CopyForTranslationAPIAction as CopyForTranslationAPIAction
from .actions.create_alias import CreatePageAliasAPIAction as CreatePageAliasAPIAction
from .actions.delete import DeletePageAPIAction as DeletePageAPIAction
from .actions.move import MovePageAPIAction as MovePageAPIAction
from .actions.publish import PublishPageAPIAction as PublishPageAPIAction
from .actions.revert_to_page_revision import RevertToPageRevisionAPIAction as RevertToPageRevisionAPIAction
from .actions.unpublish import UnpublishPageAPIAction as UnpublishPageAPIAction
from .filters import ForExplorerFilter as ForExplorerFilter, HasChildrenFilter as HasChildrenFilter
from .serializers import AdminPageSerializer as AdminPageSerializer
from rest_framework.authentication import SessionAuthentication
from wagtail.api.v2.views import PagesAPIViewSet as PagesAPIViewSet
from wagtail.models import Page as Page

class PagesAdminAPIViewSet(PagesAPIViewSet):
    base_serializer_class = AdminPageSerializer
    authentication_classes: list[type[SessionAuthentication]]
    actions: dict[str, type]
    filter_backends: list[type]
    meta_fields: list[str]
    body_fields: list[str]
    listing_default_fields: list[str]
    detail_only_fields: list[str]
    known_query_parameters: frozenset[str]
    @classmethod
    def get_detail_default_fields(cls, model): ...
    def get_root_page(self): ...
    def get_base_queryset(self): ...
    def get_queryset(self): ...
    def get_type_info(self): ...
    def listing_view(self, request): ...
    def detail_view(self, request, pk): ...
    def action_view(self, request, pk, action_name): ...
    @classmethod
    def get_urlpatterns(cls): ...
