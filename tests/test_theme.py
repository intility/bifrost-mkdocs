"""Guards on the packaged Zensical theme.

Replaces test_plugin.py: there's no plugin API to unit-test against any more,
so this builds the project's own docs with the real `zensical` CLI and checks
the theme actually rendered, plus one guard that keeps bifrost-layers.css in
sync with the pinned Zensical version.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest
import zensical

ROOT = Path(__file__).parent.parent
THEME_DIR = ROOT / "src" / "intility_bifrost_zensical" / "theme"
LAYERS_CSS = THEME_DIR / "assets" / "stylesheets" / "bifrost-layers.css"


def test_layers_css_matches_installed_zensical():
    """bifrost-layers.css hardcodes Zensical's modern stylesheet filenames.

    Zensical hardcodes those hashed names in its own base.html rather than
    discovering them at build time, so a Zensical version bump can shift the
    hash. Dependabot bumps the pin; this fails loudly (fix: one line) instead
    of a silently broken cascade layer.
    """
    modern_dir = Path(zensical.__file__).parent / "templates/assets/stylesheets/modern"
    installed = sorted(p.name for p in modern_dir.glob("*.min.css"))
    assert installed, f"no stylesheets found in {modern_dir}"

    layers_css = LAYERS_CSS.read_text(encoding="utf-8")
    for name in installed:
        assert name in layers_css, (
            f"{name!r} not imported in bifrost-layers.css; "
            f"installed Zensical ships {installed}"
        )


@pytest.fixture(scope="module")
def built_site() -> Path:
    """Build this repo's own docs with the real zensical CLI."""
    subprocess.run(
        [sys.executable, "-m", "zensical", "build", "--strict", "-c"],
        check=True,
        cwd=ROOT,
        env={**os.environ, "PYTHONPATH": str(ROOT / "src")},
    )
    return ROOT / "site"


def test_build_wires_up_the_theme(built_site: Path):
    """A real build must show the layers link, a Bifrost table, an
    admonition, and the theme script -- one page per concern.
    """
    home = (built_site / "index.html").read_text(encoding="utf-8")
    assert "assets/stylesheets/bifrost-layers.css" in home
    assert "javascripts/bifrost-theme.js" in home
    assert 'name="bifrost-version"' in home

    tables_page = (built_site / "showcase" / "tables" / "index.html").read_text(
        encoding="utf-8"
    )
    assert "bf-table" in tables_page
    assert "md-typeset__scrollwrap" in tables_page

    messages_page = (built_site / "showcase" / "messages" / "index.html").read_text(
        encoding="utf-8"
    )
    assert "admonition" in messages_page
