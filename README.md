<h1 align="center">
  <img src="https://avatars.githubusercontent.com/u/35199565" width="124px"/><br/>
  Bifrost Zensical
</h1>

<p align="center">
    <em>Intility's Bifrost design system as a Zensical theme.</em>
</p>
<p align="center">
    <a href="https://python.org">
        <img src="https://img.shields.io/badge/python-v3.10+-blue.svg?logo=python&logoColor=white&label=python" alt="Python version">
    </a>
    <a href="https://zensical.org/">
        <img src="https://img.shields.io/badge/zensical-0.0.59-blue.svg?label=zensical" alt="Zensical version">
    </a>
    <a href="https://github.com/intility/bifrost-zensical/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
    </a>
</p>

## Description

A pip-installable [Zensical](https://zensical.org/) theme that applies Intility's Bifrost design system.

Migrating from `intility-bifrost-mkdocs`? See the [migration guide](https://intility.github.io/bifrost-zensical/migrating/).

## Installation

Start from the [bifrost-zensical-template](https://github.com/intility/bifrost-zensical-template) for a preconfigured project, or add the theme to an existing one:

```bash
uv pip install intility-bifrost-zensical
```

## Usage

Set `theme.name` to `intility-bifrost` in `zensical.toml` (or `mkdocs.yml`):

```toml
[project.theme]
name = "intility-bifrost"
```

A theme cannot inject markdown extensions, so add those yourself. The
**[Quick Start](https://intility.github.io/bifrost-zensical/)** has the
complete block plus color, version badge, and navigation options.

## What it provides

- **Bifrost design system** - Colors and component styling, with light/dark mode that follows the system preference
- **Theme colors** - green (default), teal, purple, pink, yellow (set via `primary` in your palette)
- **Typography** - Satoshi for all text, JetBrains Mono for code (both self-hosted, no Google Fonts)
- **Version badge** - Set `extra.version` to show a Bifrost-styled version badge in the header
- **A Bifrost table extension** - `intility_bifrost_zensical.table_ext`, add to `markdown_extensions` for `.bf-table` styling

## Local development

This project uses [mise](https://mise.jdx.dev/) for tooling and
[just](https://github.com/casey/just) as a task runner:

```bash
mise install   # installs uv, Python, Node, just and lefthook
just setup     # syncs dev dependencies and installs git hooks
just dev       # serve the docs site locally
```

Run `just` to see all available recipes. The demo site at `docs/index.md` uses
the theme directly. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full
workflow.
