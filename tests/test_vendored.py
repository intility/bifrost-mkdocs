"""Guards on the vendored Bifrost framework assets.

These fail the build if the committed CSS drifts from the package.json pin, if
the remote font imports creep back in (which would break offline builds), or if
the Satoshi font goes missing. On a Dependabot npm bump the sync-vendored-css
workflow regenerates the CSS; if that ever fails to run, these tests catch it.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
VENDOR = ROOT / "src" / "intility_bifrost_mkdocs" / "overrides" / "assets" / "vendor"
FRAMEWORK_CSS = VENDOR / "bifrost-all.css"
SATOSHI_FONT = VENDOR / "fonts" / "satoshi-intility-variable.woff2"


def _pinned_version() -> str:
    pkg = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    return pkg["dependencies"]["@intility/bifrost-css"]


def test_framework_css_is_vendored():
    """The framework CSS must be committed and non-trivial."""
    assert FRAMEWORK_CSS.is_file()
    assert FRAMEWORK_CSS.stat().st_size > 10_000


def test_vendored_css_matches_pinned_version():
    """The banner stamped by the sync script must match the package.json pin."""
    head = FRAMEWORK_CSS.read_text(encoding="utf-8").splitlines()[0]
    version = _pinned_version()
    assert version in head, (
        f"Vendored CSS banner ({head!r}) does not match the pinned "
        f"@intility/bifrost-css version {version}. Run scripts/sync-bifrost-css.sh."
    )


def test_vendored_css_has_no_remote_imports():
    """Remote font @imports must be stripped so builds stay offline-capable."""
    css = FRAMEWORK_CSS.read_text(encoding="utf-8")
    assert "fonts.googleapis.com" not in css
    assert "api.fontshare.com" not in css
    assert not re.search(r'@import\s+url\(\s*"https?://', css)


def test_satoshi_font_is_vendored():
    """The Satoshi woff2 must ship so headings render offline."""
    assert SATOSHI_FONT.is_file()
    # woff2 magic number: 'wOF2'
    assert SATOSHI_FONT.read_bytes()[:4] == b"wOF2"


def test_bifrost_css_imports_framework_and_partials():
    """The manifest must layer the framework and import the override partials."""
    manifest = (VENDOR.parent / "stylesheets" / "bifrost.css").read_text(
        encoding="utf-8"
    )
    assert "../vendor/bifrost-all.css" in manifest
    assert "layer(bifrost-framework)" in manifest
    assert "layer(bifrost-overrides.tokens)" in manifest
    # No runtime CDN import for the framework anymore.
    assert "unpkg.com" not in manifest
