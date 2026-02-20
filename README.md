# Intility Bifrost MkDocs Theme

A pip-installable MkDocs plugin that applies Intility's Bifrost design system to Material for MkDocs.

Take a look at the [documentation](https://intility.github.io/mkdocs-template) for a preview.

## Installation

Add to your `requirements.txt`:

```
intility-bifrost-mkdocs @ git+https://github.com/intility/mkdocs-template.git@v0.1.0
```

Then install:

```bash
pip install -r requirements.txt
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

That's it. No `custom_dir`, no `extra_css`, no theme files in your repo. The plugin injects everything automatically.

## What it provides

- **Bifrost design system**: Colors, typography, and component styling matching the Intility design system
- **Light/dark mode**: Automatic theme switching with Bifrost color variables
- **Theme colors**: teal, purple, pink, yellow (set via `primary` in your palette config)
- **Typography**: Satoshi for headings, Open Sans for body, JetBrains Mono for code
- **All Material features**: Search, navigation, code highlighting, admonitions, mermaid diagrams, etc.

## How it works

The plugin uses MkDocs' `on_config` hook to:

1. Insert its `overrides/` directory into `config.theme.dirs` (highest priority)
2. Inject `extra.css` for typography and component overrides

The `overrides/main.html` extends Material's `base.html`, adds a `<link>` to `bifrost.css`, and includes JavaScript that syncs Material's color scheme/primary attributes to Bifrost CSS classes (`bf-lightmode`/`bf-darkmode`, `bf-theme-teal`/etc.).

The core Bifrost CSS variables are loaded from CDN (`@intility/bifrost-css@latest`), so design token updates are automatic.

## Local development (this repo)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

The demo site at `docs/index.md` uses the plugin via the editable install (`-e .` in requirements.txt).

## Using as a GitHub template

This repo also works as a GitHub template. Click "Use this template" to create a new docs site with the Bifrost theme pre-configured.

## Package structure

```
src/intility_bifrost_mkdocs/
├── __init__.py              # Package version
├── plugin.py                # MkDocs plugin (on_config hook)
└── overrides/               # Theme override files
    ├── main.html            # Extends Material base, adds Bifrost CSS + JS
    └── assets/
        ├── stylesheets/
        │   ├── bifrost.css  # Bifrost CSS vars -> Material CSS props
        │   └── extra.css    # Typography and component overrides
        └── fonts/
            ├── satoshi-variable.woff2
            └── satoshi-variable-italic.woff2
```
