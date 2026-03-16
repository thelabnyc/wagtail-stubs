## v7.2.0a1 (2026-03-16)

### Feat

- update stubs for wagtail 7.2 support
- add ModelViewSet.sort_order_field attribute
- add Task.lock_class class attribute
- add BaseSearchBackend.refresh_indexes() method

## v7.1.0a1 (2026-03-16)

### Feat

- update stubs for wagtail 7.1 support
- add wagtail.admin.telepath module (relocated from wagtail.telepath)
- add wagtail.admin.telepath.widgets module (relocated from wagtail.widget_adapters)
- add StructBlock.Meta.collapsed option
- add init_new_page signal to wagtail.signals

## v7.0.0a4 (2026-03-16)

### Fix

- lint

## v7.0.0a3 (2026-03-16)

### Feat

- initial wagtail-stubs package

### Fix

- improve stubs accuracy based on integration testing
- treebeard version
- version
- **ci**: remove TOX_SKIP_ENV matrix that skips all envs
- add LICENSE
- replace Any/object with concrete types where possible
- comprehensive type stub audit and improvement
