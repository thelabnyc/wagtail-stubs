from wagtail.admin.compare import ForeignObjectComparison as ForeignObjectComparison

class ImageFieldComparison(ForeignObjectComparison):
    def htmldiff(self): ...
