from wagtail.admin.ui.side_panels import StatusSidePanel as StatusSidePanel

class SnippetStatusSidePanel(StatusSidePanel):
    def get_context_data(self, parent_context): ...
