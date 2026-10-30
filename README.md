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
