## v8.0.0 (2026-11-02)

### Feat

- parameterize page views and page viewsets by page model
- parameterize generic admin views and viewsets by model
- stub API token admin views and management command
- add v3 API routers for documents, images, locales, redirects and snippets
- add wagtail.api.v3 stubs
- stub wagtail.api 8.0 helpers and v2 API changes
- add admin report view stubs
- class-based page views and PageViewSet view classes
- admin permission_policy from the registry, action_class, menu_order
- add 8.0 block, rich text, form page and locale app members
- snippet chooser widget class and URL finder for 8.0
- type swappable Page sites in app modules as AbstractPage
- resolve app permission policies through the 8.0 registry
- make existing page actions generic over the page type
- move the page model body to AbstractPage for swappable Page
- shared 8.0 interfaces (permission registry, actions, api token)

### Fix

- address admin review findings
- run stubtest on images and documents API modules
- correct API v3 filter, form builder and warning types
- add Fuzzy.unaccent attribute
- type register_setting direct, keyword and factory forms
- return JsonResponse from document chosen views
- accept Site instances in SitePermissionPolicy instance checks
- re-export GroupSitePermission and HTMLExporter
- keep stock Page in Page subpage and parent model helpers
- stop narrowing registry and action permission policies to the queried model
- admin stubtest drift and narrower allowlist
- admin stubs follow the swappable page model and policy registry
- keep consumer-visible PageLinkHandler and setting lookup types
- correct embeds, search and settings form drift and narrow allowlist
- type swapper Page sites and page parameters as AbstractPage

## v7.4.2 (2026-05-24)

### Fix

- narrow page querysets by page type filters

## v7.4.1 (2026-05-20)

### Fix

- parameterize all unparameterized PageQuerySet return types

## v7.4.0 (2026-05-12)

### Feat

- add /publish-all slash command for multi-branch releases
- add generic type parameters to block and field stubs
- update stubs for wagtail 7.3 support
- update stubs for wagtail 7.2 support
- update stubs for wagtail 7.1 support
- initial wagtail-stubs package

### Fix

- typing tweaks from integration testing
- adapt stubs for wagtail 7.3 differences
- adapt stubs for wagtail 7.2 differences
- adapt stubs for wagtail 7.1 differences
- improve type accuracy across multiple stub modules
- sendmail stubs
- resolve type errors found during stubs testing
- use TypeAlias instead of PEP 695 type statement for _FilterValue
- make BasePageManager generic
- stub signature mismatches and reduce stubtest allowlist
- bump django-treebeard-stubs to >=4.8.3
- make TreeQuerySet generic
- improve type accuracy for Page properties, PageQuerySet, ChooserBlock, and DocumentChooserBlock
- subpage_types / parent_page_types types
- allow publish.sh to run from wagtail-* branches
- add _default_manager to Page stub for reverse manager resolution
- resolve stubtest failures for wagtail 7.3
- resolve stubtest failures for wagtail 7.2
- resolve stubtest failures for wagtail 7.1
- lint
- improve stubs accuracy based on integration testing
- treebeard version
- version
- **ci**: remove TOX_SKIP_ENV matrix that skips all envs
- add LICENSE
- replace Any/object with concrete types where possible
- comprehensive type stub audit and improvement
