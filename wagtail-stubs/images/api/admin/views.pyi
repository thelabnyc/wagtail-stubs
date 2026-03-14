from ..v2.views import ImagesAPIViewSet as ImagesAPIViewSet
from .serializers import AdminImageSerializer as AdminImageSerializer

class ImagesAdminAPIViewSet(ImagesAPIViewSet):
    base_serializer_class = AdminImageSerializer
    body_fields: list[str]
    listing_default_fields: list[str]
