from django.urls import URLPattern, URLResolver
from wagtail import hooks as hooks
from wagtail.admin.auth import require_admin_access as require_admin_access
from wagtail.admin.views import (
    account as account,
)
from wagtail.admin.views import (
    chooser as chooser,
)
from wagtail.admin.views import (
    dismissibles as dismissibles,
)
from wagtail.admin.views import (
    home as home,
)
from wagtail.admin.views import (
    tags as tags,
)
from wagtail.admin.views.generic.preview import StreamFieldBlockPreview as StreamFieldBlockPreview
from wagtail.admin.views.i18n import localized_js_catalog as localized_js_catalog
from wagtail.admin.views.pages import listing as listing
from wagtail.utils.urlpatterns import decorate_urlpatterns as decorate_urlpatterns

urlpatterns: list[URLPattern | URLResolver]
urls: list[URLPattern | URLResolver]

def display_custom_404(view_func): ...
