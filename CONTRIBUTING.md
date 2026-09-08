# Contributing

Contributions are welcome! Here's how to get started.

## Prerequisites

This project uses [mise](https://mise.jdx.dev/) to manage tooling (uv, Python,
Node, just, lefthook) and [just](https://github.com/casey/just) as a task
runner. Install mise once, and it provides everything else.

## Setup

```bash
git clone git@github.com:intility/bifrost-zensical.git
cd bifrost-zensical
mise install   # installs uv, Python, Node, just and lefthook
just setup     # syncs dev dependencies and installs git hooks
```

`just setup` pre-warms the virtualenv and installs the lefthook pre-commit and
pre-push hooks.

## Common tasks

Run `just` (or `just --list`) to see every recipe. The ones you'll use most:

| Command             | What it does                                      |
| ------------------- | ------------------------------------------------- |
| `just dev`          | Serve the docs site locally with live reload      |
| `just check`        | Lint, format check, and run all tests (mirrors CI)|
| `just lint`         | Lint with Ruff                                     |
| `just lint-fix`     | Lint and auto-fix what Ruff can                    |
| `just format`       | Format code with Ruff                              |
| `just test`         | Run Python and JS tests                            |
| `just test-matrix`  | Run pytest on the Python versions CI covers        |
| `just build`        | Build the static docs site into `./site`           |
| `just sync-bifrost-css` | Refresh the vendored Bifrost CSS + Satoshi font |

## Git hooks

Lefthook runs automatically once installed:

- **pre-commit** lints and format-checks staged Python files (fast).
- **pre-push** runs the Python and JS test suites.

Reinstall them anytime with `just hooks`.

## Theming architecture

The theme restyles Zensical's built-in (Material-derived) theme to Bifrost
using CSS cascade layers. Zensical ships that stylesheet unlayered, which
always beats `@layer` rules, so `bifrost-layers.css` re-imports it into a
low-priority layer. The order is:

```
@layer material, bifrost-framework, bifrost-overrides;
```

Because our rules live in `bifrost-overrides` (above `material`), they win
without specificity ladders. A plain single-class selector beats anything
the built-in theme defines.

Layout under `src/intility_bifrost_zensical/theme/`, a packaged Zensical
theme registered via the `mkdocs.themes` entry point:

- `mkdocs_theme.yml` — `extends: material`; sets the modern variant, theme
  features, palette, fonts, and icons.
- `main.html` — extends Zensical's `base.html`; loads `bifrost-layers.css`
  and `bifrost-theme.js`.
- `assets/stylesheets/bifrost-layers.css` — a static file that re-imports
  Zensical's own hashed stylesheets into `layer(material)`. The filenames are
  hardcoded (Zensical hardcodes them too, in its own `base.html`); pinning
  the Zensical version keeps them in sync, and `tests/test_theme.py` fails
  loudly if a bump shifts the hash.
- `assets/vendor/` — the vendored Bifrost framework CSS and Satoshi font.
- `assets/stylesheets/bifrost.css` — a thin manifest that imports the framework
  and the override partials into their layers.
- `assets/stylesheets/bifrost/` — the override partials, one per concern.

A theme cannot set `markdown_extensions`; that stays a project-level key
(see `zensical.toml` and the Quick Start in the docs).

### Adding an override

1. **Reach for a token first.** Most of the built-in theme's UI is driven by
   `--md-*` custom properties. Map the relevant one to a Bifrost `--bfc-*`
   token in `bifrost/tokens.css`. That recolors the built-in components with
   no per-component rule, and switches with light/dark for free.
2. **Only write a rule if there's no variable for it** (layout, radii,
   borders, the admonition icon layout). Add a single-class rule to the matching
   partial in `bifrost/`. No specificity ladders, no `!important` — the layer
   handles precedence.

### Overriding a template

`theme/` shadows any template from Zensical's built-in theme. To adjust
structure (header, footer, nav), add the template there and use
`{% extends "base.html" %}` with the relevant `{% block %}`, as `main.html` does.

### Updating the Bifrost framework

The framework CSS is vendored (no runtime CDN fetch, works offline). Bump the
pin in `package.json`, then run `just sync-bifrost-css` and commit the result.
Dependabot does this automatically: it bumps the pin and the `sync-vendored-css`
workflow regenerates the committed CSS on the PR. `tests/test_vendored.py` fails
the build if the committed CSS ever drifts from the pin.

## Pull requests

1. Fork the repo and create a branch from `main`
2. Make your changes
3. Run `just check` and make sure it passes
4. Open a pull request
