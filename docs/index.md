# Bifrost MkDocs

An MkDocs Material plugin that applies Intility's Bifrost design system.

See the [Feature Showcase](showcase/index.md) for a live demonstration of every enabled extension and component.

## Quick Start

1. **Create a new repo** from the [bifrost-mkdocs-template](https://github.com/intility/bifrost-mkdocs-template), or add the plugin to an existing project
2. **Install the plugin** and add it to your `mkdocs.yml`:

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

    plugins:
      - intility-bifrost
      - search
    ```

3. **Start writing docs.** The plugin configures the markdown extensions, theme features, fonts, and icons for you.

## Overriding Defaults

The plugin never overwrites your config. To customize any default, just set it explicitly in your `mkdocs.yml`. For example, to disable the permalink on headings:

```yaml
markdown_extensions:
  - toc:
      permalink: false
```

## Customization

### Change the Color Scheme

Change the `primary` value in your palette config:

```yaml
primary: &bifrost_theme teal  # Options: teal, purple, pink, yellow
```

The color is defined once and automatically applied to both light and dark modes.

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

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Material Extensions Reference](https://squidfunk.github.io/mkdocs-material/reference/)
- [Markdown Guide](https://www.markdownguide.org/)
