from rest_framework.serializers import Serializer

class APIAction:
    serializer: type[Serializer] | None
    view: object
    request: object
    def __init__(self, view, request) -> None: ...
