from _typeshed import Incomplete
from django import forms
from wagtail.admin.forms.models import WagtailAdminModelForm as WagtailAdminModelForm
from wagtail.admin.widgets import AdminPageChooser as AdminPageChooser
from wagtail.contrib.search_promotions.models import Query as Query, SearchPromotion as SearchPromotion

class QueryForm(forms.ModelForm):
    query_string: Incomplete
    def clean(self) -> None: ...
    class Meta:
        model = Query
        fields: Incomplete

class SearchPromotionForm(WagtailAdminModelForm):
    sort_order: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def clean(self): ...
    class Meta(WagtailAdminModelForm.Meta):
        model = SearchPromotion
        fields: Incomplete
        widgets: Incomplete

SearchPromotionsFormSetBase: Incomplete

class SearchPromotionsFormSet(SearchPromotionsFormSetBase):
    minimum_forms: int
    minimum_forms_message: Incomplete
    def add_fields(self, form, *args, **kwargs) -> None: ...
    def clean(self) -> None: ...
