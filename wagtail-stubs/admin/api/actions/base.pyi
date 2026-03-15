from rest_framework.request import Request
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

class APIAction:
    serializer: type[Serializer] | None
    view: APIView
    request: Request
    def __init__(self, view: APIView, request: Request) -> None: ...
