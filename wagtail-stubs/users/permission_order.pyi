from _typeshed import Incomplete
from wagtail.coreutils import resolve_model_string as resolve_model_string

content_types_to_register: Incomplete
CONTENT_TYPE_ORDER: Incomplete

def register(model, **kwargs) -> None: ...
def get_content_type_order_lookup(): ...
