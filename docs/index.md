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

3. **Start writing docs.** The plugin handles the rest: markdown extensions, theme features, fonts, icons, and MathJax are all configured automatically.

That's it. No need to copy 40+ lines of extension config.

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

1. Create markdown files in the `docs/` directory
2. Update the `nav` section in `mkdocs.yaml`:

```yaml
nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - User Guide:
      - Installation: guide/installation.md
      - Configuration: guide/configuration.md
```

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Material Extensions Reference](https://squidfunk.github.io/mkdocs-material/reference/)
- [Markdown Guide](https://www.markdownguide.org/)
