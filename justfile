set dotenv-load := false

# List available recipes
default:
    @just --list

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

# Install tools (via mise), pre-warm the virtualenv, and install git hooks
[group('setup')]
setup:
    mise install
    uv sync --extra dev
    lefthook install
    @echo "Setup complete. Run 'just dev' to preview the docs."

# (Re)install lefthook git hooks
[group('setup')]
hooks:
    lefthook install

# ---------------------------------------------------------------------------
# Dev
# ---------------------------------------------------------------------------

# Serve the docs site locally with live reload
[group('dev')]
dev:
    uv run --extra dev mkdocs serve

# Build the static docs site into ./site
[group('dev')]
build:
    uv run --extra dev mkdocs build

# ---------------------------------------------------------------------------
# Quality
# ---------------------------------------------------------------------------

# Run lint, format check, and all tests (mirrors CI)
[group('quality')]
check: lint format-check test

# Lint with Ruff
[group('quality')]
lint:
    uv run --extra dev ruff check src/

# Lint and auto-fix what Ruff can
[group('quality')]
lint-fix:
    uv run --extra dev ruff check --fix src/

# Format code with Ruff
[group('quality')]
format:
    uv run --extra dev ruff format src/

# Check formatting without writing changes
[group('quality')]
format-check:
    uv run --extra dev ruff format --check src/

# Run all tests (Python + JS)
[group('quality')]
test: test-py test-js

# Run Python tests (against the default interpreter)
[group('quality')]
test-py:
    uv run --extra dev pytest

# Run Python tests across the versions CI covers (floor + ceiling)
[group('quality')]
test-matrix:
    #!/usr/bin/env bash
    set -uo pipefail
    code=0
    for v in 3.10 3.14; do
        echo "=== pytest on Python $v ==="
        uv run --python "$v" --extra dev pytest || code=1
    done
    exit $code

# Run JavaScript theme tests
[group('quality')]
test-js:
    node --test tests/javascripts/*.test.js

# ---------------------------------------------------------------------------
# Clean
# ---------------------------------------------------------------------------

# Remove build artifacts, caches, and the virtualenv
[group('clean')]
clean:
    rm -rf site/ dist/ build/ .venv/ .ruff_cache/ .pytest_cache/
    find . -type d -name __pycache__ -prune -exec rm -rf {} +
    find . -type d -name '*.egg-info' -prune -exec rm -rf {} +
    @echo "Cleaned."
