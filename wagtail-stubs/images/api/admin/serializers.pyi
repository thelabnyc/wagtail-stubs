from ..fields import ImageRenditionField as ImageRenditionField
from ..v2.serializers import ImageSerializer as ImageSerializer
from _typeshed import Incomplete

class AdminImageSerializer(ImageSerializer):
    thumbnail: Incomplete
