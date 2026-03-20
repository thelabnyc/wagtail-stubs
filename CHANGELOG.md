## v7.0.0b6 (2026-03-19)

### Fix

- widen str to StrOrPromise for labels

## v7.0.0b5 (2026-03-19)

### Fix

- improve type accuracy across multiple stub modules

## v7.0.0b4 (2026-03-19)

### Fix

- sendmail stubs

## v7.0.0b3 (2026-03-19)

### Fix

- resolve type errors found during stubs testing

## v7.0.0b2 (2026-03-19)

### Fix

- use TypeAlias instead of PEP 695 type statement for _FilterValue

## v7.0.0b1 (2026-03-18)

### Fix

- make BasePageManager generic

## v7.0.0b0 (2026-03-18)

### Fix

- stub signature mismatches and reduce stubtest allowlist

## v7.0.0a10 (2026-03-16)

### Fix

- bump django-treebeard-stubs to >=4.8.3

## v7.0.0a9 (2026-03-16)

### Fix

- make TreeQuerySet generic

## v7.0.0a8 (2026-03-16)

### Fix

- improve type accuracy for Page properties, PageQuerySet, ChooserBlock, and DocumentChooserBlock

## v7.0.0a7 (2026-03-16)

### Feat

- add /publish-all slash command for multi-branch releases

### Fix

- subpage_types / parent_page_types types

## v7.0.0a6 (2026-03-16)

### Feat

- add generic type parameters to block and field stubs

## v7.0.0a5 (2026-03-16)

### Fix

- allow publish.sh to run from wagtail-* branches
- add _default_manager to Page stub for reverse manager resolution

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
