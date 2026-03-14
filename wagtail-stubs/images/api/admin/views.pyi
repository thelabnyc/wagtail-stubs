from ..v2.views import ImagesAPIViewSet as ImagesAPIViewSet
from .serializers import AdminImageSerializer as AdminImageSerializer
from _typeshed import Incomplete

class ImagesAdminAPIViewSet(ImagesAPIViewSet):
    base_serializer_class = AdminImageSerializer
    body_fields: Incomplete
    listing_default_fields: Incomplete
