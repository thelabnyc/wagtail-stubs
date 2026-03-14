from ..fields import ImageRenditionField as ImageRenditionField
from ..v2.serializers import ImageSerializer as ImageSerializer

class AdminImageSerializer(ImageSerializer):
    thumbnail: ImageRenditionField
