from wagtail.images import get_image_model as get_image_model
from wagtail.images import get_permission_policy as get_permission_policy
from wagtail.images.models import AbstractImage
from wagtail.permission_policies.base import BasePermissionPolicy
from wagtail.permissions import policy_registry as policy_registry
from wagtail.utils.deprecation import RemovedInWagtail90Warning as RemovedInWagtail90Warning

permission_policy: BasePermissionPolicy[AbstractImage]
