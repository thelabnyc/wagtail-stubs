from _typeshed import Incomplete
from wagtail.admin.filters import WagtailFilterSet as WagtailFilterSet
from wagtail.contrib.redirects.models import Redirect as Redirect
from wagtail.models.sites import Site as Site

class RedirectsReportFilterSet(WagtailFilterSet):
    is_permanent: Incomplete
    site: Incomplete
    def filter_type(self, queryset, name, value): ...
    class Meta:
        model = Redirect
        fields: Incomplete
