from typing import Any

from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from ninja import UploadedFile
from pydantic import BaseModel
from wagtail.documents.forms import BaseDocumentForm
from wagtail.documents.models import AbstractDocument

def _restore_hidden_collection_field(form: BaseDocumentForm, payload: dict[str, Any]) -> BaseDocumentForm: ...
def build_document_form(
    model: type[AbstractDocument],
    data: BaseModel,
    file: UploadedFile,
    user: AbstractBaseUser | AnonymousUser,
) -> BaseDocumentForm: ...
def build_document_update_form(
    instance: AbstractDocument,
    data: BaseModel,
    user: AbstractBaseUser | AnonymousUser,
) -> BaseDocumentForm: ...
