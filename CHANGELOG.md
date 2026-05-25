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
