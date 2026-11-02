# wagtail-stubs

PEP 561 type stubs for [wagtail](https://github.com/wagtail/wagtail).

## Custom base page models

Wagtail 8.0 lets a project replace `wagtail.models.Page` with its own base page model (the `WAGTAIL_PAGE_MODEL` setting). The stubs cannot read Django settings, so:

- `wagtail.models.Page` is always typed as Wagtail's own `Page` class. In a project with a custom base page model, use your own model class (or `AbstractPage`) instead.
- Values that are "a page of whatever model the project uses", such as `GroupPagePermission.page`, `PageViewRestriction.page`, `Workflow.all_pages()` or `page_permission_policy`, are typed as `AbstractPage`. `Site.root_page` stays untyped (`Any`) so that projects using the stock `Page` keep working unchanged.
- On a custom base page model, tree methods (`get_children()`, `get_parent()`, `get_descendants()`, ...) return `AbstractPage` / `PageQuerySet[AbstractPage]`. For a precise type, query through your model: `BasePage.objects.child_of(page)`.
- `PageQuerySet[Page].type(BlogPage)` and `PageQuerySet[AbstractPage].type(BlogPage)` narrow to `PageQuerySet[BlogPage]`, but `PageQuerySet[BasePage].type(BlogPage)` does not.
- `PageQuerySet` is invariant (its type parameter comes from `django-treebeard-stubs`), so a `PageQuerySet[Page]` cannot be passed where a `PageQuerySet[AbstractPage]` is expected.
- `swapper` ships no type information, so `swapper.load_model("wagtailcore", "Page")` is untyped. Annotate the result as `type[AbstractPage]`.

## Generic admin views and viewsets

`ModelViewSet`, `SnippetViewSet`, `ChooserViewSet`, the generic admin views (`wagtail.admin.views.generic`), the chooser views, and the page views with `PageListingViewSet` / `PageViewSet` take the model as a type parameter. The parameter ties `model`, `object`, `get_object()`, `get_queryset()`, `save_instance()` and `action_class` to your model. Create and edit views take the form class as an optional second parameter. Without parameters, model views and viewsets default to `Model`, page views and viewsets default to `AbstractPage`, and the form defaults to `WagtailAdminModelForm`, so existing subclasses keep their current types.

`permission_policy` is not tied to the parameter. Wagtail looks it up in the policy registry, which returns the policy of the nearest registered ancestor model, so it is typed `BasePermissionPolicy[Any]` (or `PagePermissionPolicy[AbstractPage]` on page views).

Wagtail's classes do not support subscripting at runtime, so `class GroupViewSet(ModelViewSet[Group])` raises `TypeError`. Subscript the base class for the type checker only:

```python
from typing import TYPE_CHECKING

from django.contrib.auth.models import Group
from wagtail.admin.views.generic import EditView
from wagtail.admin.viewsets.model import ModelViewSet

if TYPE_CHECKING:
    _GroupEditViewBase = EditView[Group]
    _GroupViewSetBase = ModelViewSet[Group]
else:
    _GroupEditViewBase = EditView
    _GroupViewSetBase = ModelViewSet


class GroupEditView(_GroupEditViewBase):
    def get_success_message(self) -> str | None:
        return f"Saved {self.object.name}"  # self.object is a Group


class GroupViewSet(_GroupViewSetBase):
    model = Group
    edit_view_class = GroupEditView
```

If you already call `django_stubs_ext.monkeypatch()`, you can instead pass the classes you subscript, for example `django_stubs_ext.monkeypatch(extra_classes=[ModelViewSet, EditView])`, and write `ModelViewSet[Group]` directly.

The `*_view_class` attributes are not tied to the viewset's parameter, because code such as `PageListingViewSet.index_view_class.base_columns` reads them from the class itself. Parameterize the view classes you assign to them yourself.
