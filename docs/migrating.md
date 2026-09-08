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

2. **Change the theme** in `mkdocs.yml`.

    ```diff
     theme:
    -  name: material
    +  name: intility-bifrost

     plugins:
    -  - intility-bifrost
    -  - git-revision-date-localized
       - search
       - awesome-nav
    ```

3. **Copy the `markdown_extensions` block** from the [Quick Start](index.md#quick-start).
4. **Build with `zensical`** instead of `mkdocs`. If you use the reusable workflow,
   point it to `intility/bifrost-zensical/.github/workflows/docs.yml@intility-bifrost-zensical-v0.1.0`.

Only if it applies to you:

- A custom `palette` must use `scheme: default` / `slate` instead of `light` / `dark`.
- Zensical has no plugin API yet, so `git-revision-date-localized` and custom hooks
  do not run ([zensical/backlog#18](https://github.com/zensical/backlog/issues/18)).
- You can convert `mkdocs.yml` to `zensical.toml` later; both work.
