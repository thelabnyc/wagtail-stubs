from wagtail.coreutils import resolve_model_string as resolve_model_string

content_types_to_register: list[tuple[str, int]]
CONTENT_TYPE_ORDER: dict[int, int]

def register(model, **kwargs) -> None: ...
def get_content_type_order_lookup(): ...
