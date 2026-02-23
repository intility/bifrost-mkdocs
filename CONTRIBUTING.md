# Contributing

Contributions are welcome! Here's how to get started.

## Setup

```bash
git clone git@github.com:intility/bifrost-mkdocs.git
cd bifrost-mkdocs
uv venv .venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

## Development

Preview the docs site locally:

```bash
mkdocs serve
```

## Code quality

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting:

```bash
ruff check src/
ruff format src/
```

Run tests with:

```bash
pytest
```

## Pull requests

1. Fork the repo and create a branch from `main`
2. Make your changes
3. Ensure `ruff check`, `ruff format --check`, and `pytest` all pass
4. Open a pull request
