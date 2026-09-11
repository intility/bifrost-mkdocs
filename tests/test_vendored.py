"""Guards on the vendored Bifrost framework assets.

These fail the build if the committed CSS drifts from the package.json pin, if
the remote font imports creep back in (which would break offline builds), or if
a bundled font goes missing. On a Dependabot npm bump the sync-vendored-css
workflow regenerates the CSS; if that ever fails to run, these tests catch it.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
VENDOR = ROOT / "src" / "intility_bifrost_zensical" / "theme" / "assets" / "vendor"
FRAMEWORK_CSS = VENDOR / "bifrost-all.css"
SATOSHI_FONT = VENDOR / "fonts" / "satoshi-intility-variable.woff2"
JETBRAINS_MONO_FONT = VENDOR / "fonts" / "jetbrains-mono-variable.woff2"


def _pinned_version() -> str:
    pkg = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    return pkg["dependencies"]["@intility/bifrost-css"]


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


def test_jetbrains_mono_font_is_vendored():
    """The JetBrains Mono woff2 must ship so code renders the same for everyone."""
    assert JETBRAINS_MONO_FONT.is_file()
    # woff2 magic number: 'wOF2'
    assert JETBRAINS_MONO_FONT.read_bytes()[:4] == b"wOF2"
    # SIL OFL requires the license to ship with the font.
    assert (VENDOR / "fonts" / "JetBrainsMono-OFL.txt").is_file()


def test_manifest_layer_statement_precedes_imports():
    """The @layer order statement must come before every @import.

    A @layer statement placed *after* an @import makes the browser silently
    drop all following @import rules, which would unload tokens.css and every
    override partial (and the theme would fall back to bare Material). This
    guards that exact regression without needing a browser.
    """
    stylesheets = VENDOR.parent / "stylesheets"
    manifest = (stylesheets / "bifrost.css").read_text(encoding="utf-8")
    assert manifest.index("@layer ") < manifest.index("@import "), (
        "The @layer statement must precede all @import rules in bifrost.css, "
        "or browsers drop the partial @imports and the overrides never load."
    )
    assert "../vendor/bifrost-all.css" in manifest
    assert "layer(bifrost-framework)" in manifest

    partials = sorted(p.name for p in (stylesheets / "bifrost").glob("*.css"))
    for name in partials:
        assert f"bifrost/{name}" in manifest, f"{name} is not imported"
    assert manifest.count("@import ") == len(partials) + 1
