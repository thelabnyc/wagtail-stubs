from wagtail import hooks as hooks
from wagtail.embeds import urls as urls
from wagtail.embeds.rich_text import MediaEmbedHandler as MediaEmbedHandler
from wagtail.embeds.rich_text.contentstate import ContentstateMediaConversionRule as ContentstateMediaConversionRule
from wagtail.embeds.rich_text.editor_html import EditorHTMLEmbedConversionRule as EditorHTMLEmbedConversionRule

def register_admin_urls(): ...
def register_embed_feature(features) -> None: ...
