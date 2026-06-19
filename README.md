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

## Installation

```bash
uv pip install intility-bifrost-mkdocs
```

## Usage

Add `intility-bifrost` to your `mkdocs.yml` plugins:

```yaml
theme:
  name: material
  palette:
    - scheme: default       # or 'light' — both map to Bifrost light mode
      primary: teal         # Options: teal, purple, pink, yellow
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate         # or 'dark' — both map to Bifrost dark mode
      primary: teal
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
- **Typography** - Satoshi for all text, JetBrains Mono for code (both self-hosted, no Google Fonts)
- **Markdown extensions** - Admonitions, code highlighting, tabs, mermaid diagrams, emoji, task lists, and more
- **Theme features** - Instant navigation, search suggestions, code copy buttons, and more
- **Admonition icons** - Custom FontAwesome icons for all admonition types
- **Bundled plugins** - `mkdocs-awesome-nav` and `mkdocs-git-revision-date-localized-plugin` are installed alongside; opt in by adding them to your `plugins:` list

All defaults are injected only when the user hasn't provided their own config, so you can override anything by setting it explicitly in your `mkdocs.yml`.

## Local development

This project uses [mise](https://mise.jdx.dev/) for tooling and
[just](https://github.com/casey/just) as a task runner:

```bash
mise install   # installs uv, Python, Node, just and lefthook
just setup     # syncs dev dependencies and installs git hooks
just dev       # serve the docs site locally
```

Run `just` to see all available recipes. The demo site at `docs/index.md` uses
the plugin directly. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full
workflow.
