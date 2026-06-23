# Contributing

Contributions are welcome! Here's how to get started.

## Prerequisites

This project uses [mise](https://mise.jdx.dev/) to manage tooling (uv, Python,
Node, just, lefthook) and [just](https://github.com/casey/just) as a task
runner. Install mise once, and it provides everything else.

## Setup

```bash
git clone git@github.com:intility/bifrost-mkdocs.git
cd bifrost-mkdocs
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

The theme restyles Material for MkDocs to Bifrost using CSS cascade layers.
Material ships its CSS unlayered, which always beats `@layer` rules, so the
plugin re-imports Material's own stylesheets into a low-priority layer. The
order, declared in `overrides/main.html`, is:

```
@layer material, bifrost-framework, bifrost-overrides;
```

Because our rules live in `bifrost-overrides` (above `material`), they win
without specificity ladders. A plain single-class selector beats anything
Material defines.

Layout under `src/intility_bifrost_mkdocs/overrides/`:

- `main.html` — re-imports Material's hashed stylesheets into `layer(material)`.
  The plugin discovers the hashed filenames at build time (`plugin.py`).
- `assets/vendor/` — the vendored Bifrost framework CSS and Satoshi font.
- `assets/stylesheets/bifrost.css` — a thin manifest that imports the framework
  and the override partials into their layers.
- `assets/stylesheets/bifrost/` — the override partials, one per concern
  (`tokens`, `base`, `messages`, `highlighter`, `nav`, `tabs`, `search`, `footer`,
  `misc`).

### Adding an override

1. **Reach for a token first.** Most of Material's UI is driven by `--md-*`
   custom properties. Map the relevant one to a Bifrost `--bfc-*` token in
   `bifrost/tokens.css`. That recolors Material's own components with no
   per-component rule, and switches with light/dark for free. The 13
   `--md-code-hl-*-color` variables, for example, theme all syntax highlighting.
2. **Only write a rule if Material has no variable for it** (layout, radii,
   borders, the admonition icon layout). Add a single-class rule to the matching
   partial in `bifrost/`. No specificity ladders, no `!important` — the layer
   handles precedence.

### Overriding a template

`overrides/` shadows any Material template. To adjust structure (header, footer,
nav), add the template there and use `{% extends "base.html" %}` with the
relevant `{% block %}`, as `main.html` does.

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
