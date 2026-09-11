# Migrating from bifrost-mkdocs

`intility-bifrost-mkdocs` is deprecated; Material for MkDocs reaches end of
life on 2026-11-05. `intility-bifrost-zensical` is the replacement.

1. **Swap the dependency.**

    ```diff
    -mkdocs
    -mkdocs-material
    -intility-bifrost-mkdocs
    +intility-bifrost-zensical
    ```

2. **Change the theme and prune the plugins** in `mkdocs.yml`. Zensical has no
   plugin API ([zensical/backlog#18](https://github.com/zensical/backlog/issues/18)).
   It ships native replacements for a fixed set of MkDocs plugins; see the
   [supported plugins](https://zensical.org/docs/compatibility/mkdocs/plugins/)
   list. Remove every plugin not on that list. `awesome-nav` is on it; add it
   if you want `.nav.yml` files instead of a central `nav:` block.

    ```diff
     theme:
    -  name: material
    +  name: intility-bifrost

     plugins:
    -  - intility-bifrost
    -  - git-revision-date-localized
       - search
    +  - awesome-nav
    ```

3. **Copy the `markdown_extensions` block** from the [Quick Start](index.md#quick-start).

4. **Build with `zensical`** instead of `mkdocs`. If you use the reusable
   workflow, the caller sets `permissions` and `concurrency` itself:

    ```yaml
    # .github/workflows/docs.yml
    name: Documentation

    on:
      push:
        branches: [main]
      workflow_dispatch:

    permissions:
      contents: read
      pages: write
      id-token: write

    concurrency:
      group: pages
      cancel-in-progress: false

    jobs:
      docs:
        uses: intility/bifrost-zensical/.github/workflows/docs.yml@intility-bifrost-zensical-v0.1.0
        # with:
        #   config-file: zensical.toml   # default: mkdocs.yml
        #   install: -r requirements.txt # default: intility-bifrost-zensical
    ```

    Pin to an `intility-bifrost-zensical-v*` tag. The plain `v*` tags in this
    repo belong to the deprecated `intility-bifrost-mkdocs` package.

!!! note "Styling covers the Quick Start setup only"

    The theme styles the plugins and markdown extensions from the
    [Quick Start](index.md#quick-start), nothing more. If another plugin or
    extension needs Bifrost styling, [open an issue](https://github.com/intility/bifrost-zensical/issues)
    or see the [contribution guide](https://github.com/intility/bifrost-zensical/blob/main/CONTRIBUTING.md).

## Edge cases

Skip anything here that does not match your setup.

- A fence with a bare option superfences does not know, such as
  `yaml file="x"`, renders as inline code. Use the brace form:
  `{.yaml file="x"}`.
- A custom `palette` must use `scheme: default` / `slate` instead of `light` / `dark`.
- Custom `hooks` do not run.
- The theme enables `content.action.edit`, so the edit link renders when
  `repo_url` is set. Zensical defaults `edit_uri` to `edit/master/docs/`; set
  it yourself if your branch is `main`. A custom `theme.features` list
  replaces the theme's, so add the feature back there.
- You can convert `mkdocs.yml` to `zensical.toml` later; both work. A deep
  central `nav:` becomes hard to read as nested TOML inline tables. Keep
  `mkdocs.yml` or switch to `awesome-nav` in that case.
