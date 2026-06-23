# Bifrost MkDocs

An MkDocs Material plugin that applies Intility's Bifrost design system.

See the [Feature Showcase](showcase/index.md) for a live demonstration of every enabled extension and component.

## Quick Start

1. **Create a new repo** from the [bifrost-mkdocs-template](https://github.com/intility/bifrost-mkdocs-template), or add the plugin to an existing project
2. **Install the plugin** and add it to your `mkdocs.yml`. This is the complete minimum:

    ```yaml
    site_name: My Docs
    theme:
      name: material      # required: the plugin overrides Material's theme
    plugins:
      - intility-bifrost
      - search            # re-add: defining a plugins: block drops MkDocs' default search
    ```

3. **Start writing docs.** The plugin configures the markdown extensions, theme features, fonts, and icons for you.

That's all you need. Everything else (markdown extensions, theme features, fonts, icons, and a teal light/dark palette toggle) is injected automatically and can be overridden by setting it yourself. To use a [different color](#change-the-color-scheme), set your own `palette`.

## Overriding Defaults

The plugin never overwrites your config. To customize any default, just set it explicitly in your `mkdocs.yml`. For example, to disable the permalink on headings:

```yaml
markdown_extensions:
  - toc:
      permalink: false
```

## Customization

### Change the Color Scheme

The plugin injects a teal light/dark palette by default. To use a different color, set your own `palette` (this also lets you customize the toggle icons and labels):

```yaml
theme:
  name: material
  palette:
    - scheme: light
      primary: &bifrost_theme teal  # Options: teal, purple, pink, yellow
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: dark
      primary: *bifrost_theme
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

The `&bifrost_theme` anchor defines the color once and reuses it for both modes. A user-defined `palette` replaces the injected default entirely, so include both modes if you want to keep the toggle.

### Version Badge

Display a version badge in the header next to the site name by setting `extra.version`:

```yaml
extra:
  version: 1.0.0
```

The badge renders using Bifrost's `bf-badge` styling and only appears when `version` is set.

### Add Pages

The bundled [awesome-nav](https://lukasgeiter.github.io/mkdocs-awesome-nav/) plugin builds the navigation from `.nav.yml` files placed next to your content, so there's no central `nav:` block to maintain. Enable it once in `mkdocs.yml`:

```yaml
plugins:
  - intility-bifrost
  - search
  - awesome-nav
```

Then create markdown files in `docs/` and drop a `.nav.yml` alongside them to set the order and titles:

```yaml
# docs/.nav.yml
nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - User Guide: guide
```

A `.nav.yml` inside a subdirectory (for example `docs/guide/.nav.yml`) orders that section. Without awesome-nav, list pages in a standard MkDocs `nav:` block instead.

### Show Page Dates

The bundled [git-revision-date-localized](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin) plugin adds "last updated" (and optionally creation) dates to pages from your git history. It's installed alongside the theme; opt in by adding it to your `plugins:` list:

```yaml
plugins:
  - intility-bifrost
  - search
  - git-revision-date-localized:
      enable_creation_date: true
      type: timeago
```

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Material Extensions Reference](https://squidfunk.github.io/mkdocs-material/reference/)
- [Markdown Guide](https://www.markdownguide.org/)
