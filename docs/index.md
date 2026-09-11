# Bifrost Zensical

A packaged [Zensical](https://zensical.org/) theme that applies Intility's Bifrost design system.

See the [Feature Showcase](showcase/index.md) for a live demonstration of every enabled extension and component.

## Quick Start

### New repo

Create the repo from the [bifrost-zensical-template](https://github.com/intility/bifrost-zensical-template).
It ships the config from the next section, a `requirements.txt`, and the deploy workflow. Then:

1. Set `site_name` and `site_url` in `zensical.toml`.
2. Enable GitHub Pages: Settings > Pages > Source: GitHub Actions.
3. Write docs in `docs/`.

### Existing repo

1. **Install the theme.** Zensical is a dependency of the package, so this is the only install step:

    ```bash
    uv pip install intility-bifrost-zensical
    ```

2. **Set `theme.name` and the markdown extensions** in your config file. Zensical reads `zensical.toml` (its native format) or `mkdocs.yml`. A theme cannot inject markdown extensions for you, so this block is the complete list (it replaces Zensical's own defaults, it doesn't add to them):

    === "zensical.toml"

        ```toml
        [project]
        site_name = "My Docs"

        [project.theme]
        name = "intility-bifrost"

        [project.plugins]
        search = {}
        awesome-nav = {}

        [project.markdown_extensions]
        abbr = {}
        admonition = {}
        github-callouts = {}
        attr_list = {}
        def_list = {}
        footnotes = {}
        md_in_html = {}
        toc.permalink = true
        pymdownx.arithmatex.generic = true
        pymdownx.betterem.smart_enable = "all"
        pymdownx.caret = {}
        pymdownx.details = {}
        pymdownx.emoji.emoji_generator = "zensical.extensions.emoji.to_svg"
        pymdownx.emoji.emoji_index = "zensical.extensions.emoji.twemoji"
        pymdownx.highlight.anchor_linenums = true
        pymdownx.highlight.line_spans = "__span"
        pymdownx.highlight.pygments_lang_class = true
        pymdownx.inlinehilite = {}
        pymdownx.keys = {}
        pymdownx.magiclink = {}
        pymdownx.mark = {}
        pymdownx.smartsymbols = {}
        pymdownx.snippets = {}
        pymdownx.superfences.custom_fences = [
          { name = "mermaid", class = "mermaid", format = "pymdownx.superfences.fence_code_format" },
        ]
        pymdownx.tabbed.alternate_style = true
        pymdownx.tabbed.combine_header_slug = true
        pymdownx.tasklist.custom_checkbox = true
        pymdownx.tilde = {}
        # Quoted on purpose: an unquoted dotted key nests into a sub-table.
        "intility_bifrost_zensical.table_ext" = {}
        ```

    === "mkdocs.yml"

        ```yaml
        site_name: My Docs

        theme:
          name: intility-bifrost

        plugins:
          - search
          - awesome-nav

        markdown_extensions:
          - abbr
          - admonition
          - github-callouts
          - attr_list
          - def_list
          - footnotes
          - md_in_html
          - toc:
              permalink: true
          - pymdownx.arithmatex:
              generic: true
          - pymdownx.betterem:
              smart_enable: all
          - pymdownx.caret
          - pymdownx.details
          - pymdownx.emoji:
              emoji_generator: !!python/name:zensical.extensions.emoji.to_svg
              emoji_index: !!python/name:zensical.extensions.emoji.twemoji
          - pymdownx.highlight:
              anchor_linenums: true
              line_spans: __span
              pygments_lang_class: true
          - pymdownx.inlinehilite
          - pymdownx.keys
          - pymdownx.magiclink
          - pymdownx.mark
          - pymdownx.smartsymbols
          - pymdownx.snippets
          - pymdownx.superfences:
              custom_fences:
                - name: mermaid
                  class: mermaid
                  format: !!python/name:pymdownx.superfences.fence_code_format
          - pymdownx.tabbed:
              alternate_style: true
              combine_header_slug: true
          - pymdownx.tasklist:
              custom_checkbox: true
          - pymdownx.tilde
          - intility_bifrost_zensical.table_ext
        ```

3. **Serve the site** and start writing docs:

    ```bash
    zensical serve
    ```

4. **Deploy with the reusable workflow.** Add the file below, then enable GitHub
   Pages: Settings > Pages > Source: GitHub Actions. The caller sets
   `permissions` and `concurrency` itself:

    ```yaml
    # .github/workflows/deploy-docs.yml
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
        uses: intility/bifrost-zensical/.github/workflows/docs.yml@intility-bifrost-zensical-v0.1.1 # x-release-please-version
        with:
          config-file: zensical.toml   # default: mkdocs.yml
          # install: -r requirements.txt   # default: intility-bifrost-zensical
    ```

    Pin to an `intility-bifrost-zensical-v*` tag. If your org requires SHA
    pinning, use the commit SHA of the tag and keep the tag as a trailing
    comment; Dependabot bumps both together.

Theme features, fonts, and a teal palette that follows the system light/dark preference are set by the theme. Override any of them by setting `theme.*` yourself.

## Customization

### Change the Color Scheme

Set `extra.primary` to `green`, `teal`, `purple`, `pink`, or `yellow`. The theme's palette and the light/dark toggle stay as they are:

=== "zensical.toml"

    ```toml
    [project.extra]
    primary = "purple"
    ```

=== "mkdocs.yml"

    ```yaml
    extra:
      primary: purple
    ```

To change the toggle icons or labels, or to drop the "follow system" option, set your own `palette` instead. A user-defined `palette` replaces the theme's default entirely, so include both modes if you want to keep the toggle. Use `scheme: default` for light mode and `scheme: slate` for dark mode; the theme maps them onto Bifrost's light and dark modes. See the [Zensical palette docs](https://zensical.org/docs/setup/colors/) for the full syntax.

### Version Badge

Display a version badge in the header next to the site name by setting `extra.version`:

=== "zensical.toml"

    ```toml
    [project.extra]
    version = "1.0.0"
    ```

=== "mkdocs.yml"

    ```yaml
    extra:
      version: 1.0.0
    ```

The badge renders using Bifrost's `bf-badge` styling and only appears when `version` is set.

### Add Pages

The `awesome-nav` plugin from the Quick Start builds the navigation from `.nav.yml` files placed next to your content, so there's no central `nav:` block to maintain. It is built into Zensical itself, no separate package needed. Create markdown files in `docs/` and drop a `.nav.yml` alongside them to set the order and titles:

```yaml
# docs/.nav.yml
nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - User Guide: guide
```

A `.nav.yml` inside a subdirectory (for example `docs/guide/.nav.yml`) orders that section. Without `awesome-nav`, list pages in a standard `nav:` block instead.

## Migrating from bifrost-mkdocs

See the [migration guide](migrating.md) if you're on the old `intility-bifrost-mkdocs` plugin.

## Resources

- [Zensical Documentation](https://zensical.org/docs/)
- [Markdown Guide](https://www.markdownguide.org/)
