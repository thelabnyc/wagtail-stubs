from _typeshed import Incomplete
from wagtail.images import get_image_model as get_image_model
from wagtail.images.models import Image as Image
from wagtail.permission_policies.collections import CollectionOwnershipPermissionPolicy as CollectionOwnershipPermissionPolicy

permission_policy: Incomplete

class ImagesPermissionPolicyGetter:
    def __get__(self, obj, objtype=None): ...

def set_permission_policy() -> None: ...
def update_permission_policy(signal, sender, setting, **kwargs) -> None: ...
