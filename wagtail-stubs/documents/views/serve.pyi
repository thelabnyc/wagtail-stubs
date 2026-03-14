from wagtail import hooks as hooks
from wagtail.documents import get_document_model as get_document_model
from wagtail.documents.models import document_served as document_served
from wagtail.forms import PasswordViewRestrictionForm as PasswordViewRestrictionForm
from wagtail.models import CollectionViewRestriction as CollectionViewRestriction
from wagtail.utils import sendfile_streaming_backend as sendfile_streaming_backend
from wagtail.utils.sendfile import sendfile as sendfile

def document_etag(request, document_id, document_filename): ...
def serve(request, document_id, document_filename): ...
def authenticate_with_password(request, restriction_id): ...
