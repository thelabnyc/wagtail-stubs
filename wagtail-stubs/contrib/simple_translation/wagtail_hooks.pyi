from collections.abc import Generator

from _typeshed import Incomplete
from wagtail import hooks as hooks
from wagtail.admin.menu import MenuItem as MenuItem
from wagtail.models.i18n import Locale as Locale
from wagtail.models.i18n import TranslatableMixin as TranslatableMixin
from wagtail.models.pages import Page as Page

from .views import (
    SubmitPageTranslationView as SubmitPageTranslationView,
)
from .views import (
    SubmitSnippetTranslationView as SubmitSnippetTranslationView,
)

def register_admin_urls(): ...
def register_submit_translation_permission(): ...
def page_listing_more_buttons(page, user, next_url=None) -> Generator[Incomplete]: ...
def page_header_buttons(page, user, view_name, next_url=None) -> Generator[Incomplete]: ...
def register_snippet_listing_buttons(snippet, user, next_url=None) -> Generator[Incomplete]: ...
def construct_translated_pages_to_cascade_actions(pages: list[Page], action: str): ...
