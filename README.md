<h1 align="center">
  <img src="https://avatars.githubusercontent.com/u/35199565" width="124px"/><br/>
  Bifrost MkDocs
</h1>

<p align="center">
    <em>Intility's Bifrost design system as a Material for MkDocs plugin.</em>
</p>
<p align="center">
    <a href="https://python.org">
        <img src="https://img.shields.io/badge/python-v3.10+-blue.svg?logo=python&logoColor=white&label=python" alt="Python version">
    </a>
    <a href="https://squidfunk.github.io/mkdocs-material/">
        <img src="https://img.shields.io/badge/mkdocs--material-9.7.0+-blue.svg?logo=materialformkdocs&logoColor=white&label=mkdocs-material" alt="MkDocs Material version">
    </a>
    <a href="https://github.com/intility/bifrost-mkdocs/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
    </a>
</p>

## Description

A pip-installable MkDocs plugin that applies Intility's Bifrost design system to Material for MkDocs. The plugin is batteries-included: colors, typography, component styling, markdown extensions, theme features, and admonition icons are all configured automatically.

## Resources

[**Documentation**](https://intility.github.io/bifrost-mkdocs/)
| [**Template**](https://github.com/intility/bifrost-mkdocs-template)
| [**MIT License**](https://github.com/intility/bifrost-mkdocs/blob/main/LICENSE)

## Installation

Add to your `requirements.txt`, pinning to a [release tag](https://github.com/intility/bifrost-mkdocs/releases):

```
intility-bifrost-mkdocs @ git+https://github.com/intility/bifrost-mkdocs.git@<version>
```

Then install:

```bash
uv pip install -r requirements.txt
```

## Usage

Add `intility-bifrost` to your `mkdocs.yml` plugins:

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

## What it provides

Adding `intility-bifrost` to your plugins list gives you:

- **Bifrost design system** - Colors, typography, and component styling matching the Intility design system
- **Light/dark mode** - Automatic theme switching with Bifrost color variables
- **Theme colors** - teal, purple, pink, yellow (set via `primary` in your palette config)
- **Typography** - Satoshi for headings, Open Sans for body, JetBrains Mono for code
- **23 markdown extensions** - Admonitions, code highlighting, tabs, mermaid diagrams, math (MathJax), emoji, task lists, and more
- **13 theme features** - Instant navigation, search suggestions, code copy buttons, etc.
- **Admonition icons** - Custom FontAwesome icons for all admonition types

All defaults are injected only when the user hasn't provided their own config, so you can override anything by setting it explicitly in your `mkdocs.yml`.

## Local development

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -e ".[dev]"
mkdocs serve
```

This installs the plugin in editable mode with dev dependencies (ruff, pytest, livereload, git-revision-date plugin). The demo site at `docs/index.md` uses the plugin directly.
