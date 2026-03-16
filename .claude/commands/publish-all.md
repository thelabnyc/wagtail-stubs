Publish a new release across all supported wagtail version branches.

Arguments: $ARGUMENTS

The argument should be one of:
- `alpha` — publish a prerelease alpha bump (`--prerelease alpha`)
- `beta` — publish a prerelease beta bump (`--prerelease beta`)
- `patch` — publish a stable patch-level bump (no prerelease flag)

Never bump major or minor — those are determined by the branch.

## Supported version policy

We maintain a branch per wagtail minor version (`wagtail-7.0`, `wagtail-7.1`, etc.) and support every version back to (and including) the last LTS release. Wagtail LTS releases happen on a regular cadence — as of March 2026, 7.0 is the current LTS and the next LTS is 7.4. See [Wagtail's Release Notes](https://docs.wagtail.org/en/stable/releases/index.html) for up-to-date info on what the current/LTS versions are. Check this every time you run this command and update the versions noted in the command if you notice they're now out of date.

- **Right now (March 2026)** we support: 7.0, 7.1, 7.2, 7.3
- **When 7.4 (LTS) ships**, we add 7.4 but still keep 7.0–7.3
- **When the first post-LTS release ships** (7.5 or 8.0), we drop everything before the LTS — so we'd drop 7.0, 7.1, 7.2, 7.3 and only support 7.4+

The `master` branch must always be identical to the latest (highest) version branch. It is kept in sync by fast-forward merging the latest branch into master after each publish cycle. This means `master` always has the wagtail dependency and version number of the newest supported release — e.g. if the latest branch is `wagtail-7.3`, then `master` pins `wagtail>=7.3,<7.4`. CI/CD pipelines and the default `pip install wagtail-stubs` experience are driven by `master`.

## Process

Starting from the **oldest** supported branch and working forward:

1. `git checkout wagtail-X.Y && git pull`
2. Run `uv run tox` — both `stubtest` and `mypy-plugins` must pass
3. If tests fail, fix the issues before proceeding
4. Publish:
   - For `alpha`: `bash bin/publish.sh --prerelease alpha`
   - For `beta`: `bash bin/publish.sh --prerelease beta`
   - For `patch`: `bash bin/publish.sh`
5. `git checkout wagtail-X.(Y+1)` (the next version branch)
6. `git merge wagtail-X.Y` — resolve any conflicts (always keep the current branch's version number and wagtail dependency range in `pyproject.toml`; keep both changelog sections)
7. Repeat from step 2

After the last version branch is published, fast-forward master:

```
git checkout master
git merge wagtail-X.Y --ff-only
git push origin master
```

## Conflict resolution rules

When merging an older branch into a newer one, the conflicts are always in `pyproject.toml` (version number) and `CHANGELOG.md`:

- **`pyproject.toml` version**: Keep the **current** (HEAD) branch's version
- **`pyproject.toml` wagtail dependency**: Keep the **current** branch's range (e.g. `>=7.2,<7.3`)
- **`CHANGELOG.md`**: Keep **both** sections — the current branch's entries on top, the incoming entries below

## Do this now

Publish on all supported version branches using the release type specified above, starting from the oldest. Currently supported: wagtail-7.0, wagtail-7.1, wagtail-7.2, wagtail-7.3.
