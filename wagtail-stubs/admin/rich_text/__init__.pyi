from wagtail.admin.rich_text.editors.draftail import DraftailRichTextArea as DraftailRichTextArea

DEFAULT_RICH_TEXT_EDITORS: dict[str, dict[str, str]]

def get_rich_text_editor_widget(name: str = "default", features=None): ...
