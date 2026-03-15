from _typeshed import Incomplete
from wagtail.contrib.search_promotions.models import Query as Query
from wagtail.contrib.search_promotions.models import SearchPromotion as SearchPromotion

register: Incomplete

@register.simple_tag
def get_search_promotions(search_query): ...
