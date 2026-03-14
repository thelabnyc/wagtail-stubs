from django.urls import URLPattern, URLResolver
from wagtail.documents.views import documents as documents, multiple as multiple

app_name: str
urlpatterns: list[URLPattern | URLResolver]
