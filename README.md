# Intility Bifrost MkDocs Theme
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

A pip-installable MkDocs plugin that applies Intility's Bifrost design system to Material for MkDocs.

Requires Python 3.10 or newer.

Take a look at the [documentation](https://intility.github.io/mkdocs-template) for a preview.

## Installation

Add to your `requirements.txt`:

```
intility-bifrost-mkdocs @ git+https://github.com/intility/mkdocs-template.git@v0.1.0
```

> [!TIP]
> Pin to a specific release tag for reproducible builds. Check [releases](https://github.com/intility/mkdocs-template/releases) for the latest version.

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

The plugin is batteries-included. Adding `intility-bifrost` to your plugins list gives you:

- **Bifrost design system**: Colors, typography, and component styling matching the Intility design system
- **Light/dark mode**: Automatic theme switching with Bifrost color variables
- **Theme colors**: teal, purple, pink, yellow (set via `primary` in your palette config)
- **Typography**: Satoshi for headings, Open Sans for body, JetBrains Mono for code
- **23 markdown extensions**: Admonitions, code highlighting, tabs, mermaid diagrams, math (MathJax), emoji, task lists, and more
- **13 theme features**: Instant navigation, search suggestions, code copy buttons, etc.
- **Admonition icons**: Custom FontAwesome icons for all admonition types

All defaults are injected only when the user hasn't provided their own config, so you can override anything by setting it explicitly in your `mkdocs.yml`.

## Local development (this repo)

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -e ".[dev]"
mkdocs serve
```

This installs the plugin in editable mode with dev dependencies (ruff, pytest, livereload, git-revision-date plugin). The demo site at `docs/index.md` uses the plugin directly.

## Using as a GitHub template

This repo also works as a GitHub template. Click "Use this template" to create a new docs site with the Bifrost theme pre-configured.
