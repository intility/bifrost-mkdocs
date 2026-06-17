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

## Git hooks

Lefthook runs automatically once installed:

- **pre-commit** lints and format-checks staged Python files (fast).
- **pre-push** runs the Python and JS test suites.

Reinstall them anytime with `just hooks`.

## Pull requests

1. Fork the repo and create a branch from `main`
2. Make your changes
3. Run `just check` and make sure it passes
4. Open a pull request
