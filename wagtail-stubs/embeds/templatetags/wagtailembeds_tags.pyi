from django.template import Library
from wagtail.embeds import embeds as embeds
from wagtail.embeds.exceptions import EmbedException as EmbedException

register: Library

def embed_tag(url, max_width=None): ...
