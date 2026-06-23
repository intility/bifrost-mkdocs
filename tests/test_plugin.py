from __future__ import annotations

import re
from pathlib import Path

import pytest
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import PluginError

from intility_bifrost_mkdocs.plugin import (
    BIFROST_LAYERS_CSS,
    DEFAULT_ADMONITION_ICONS,
    DEFAULT_EXTENSIONS,
    DEFAULT_FEATURES,
    DEFAULT_PALETTE,
    DEFAULT_TOP_ICON,
    IntilityBifrostPlugin,
    _build_layer_bootstrap_css,
    _discover_material_stylesheets,
)

OVERRIDES_DIR = (
    Path(__file__).parent.parent / "src" / "intility_bifrost_mkdocs" / "overrides"
)


def _minimal_config() -> MkDocsConfig:
    """Return a minimal MkDocs config suitable for testing."""
    cfg = MkDocsConfig()
    cfg.load_dict(
        {
            "site_name": "Test",
            "theme": {"name": "material"},
        }
    )

    # Validation populates defaults (theme.dirs, extra_css, etc.)
    errors, _warnings = cfg.validate()
    assert not errors, errors
    return cfg  # type: ignore


# ---------------------------------------------------------------------------
# Original tests (preserved)
# ---------------------------------------------------------------------------


def test_plugin_injects_overrides_dir():
    """The plugin should prepend its overrides dir into the config."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    original_dirs_len = len(config.theme.dirs)

    result = plugin.on_config(config)

    overrides_dir = str(OVERRIDES_DIR.resolve())
    assert result.theme.dirs[0] == overrides_dir
    assert len(result.theme.dirs) == original_dirs_len + 1


def test_overrides_directory_exists():
    """The overrides directory should contain the expected theme files."""
    assert OVERRIDES_DIR.is_dir()
    assert (OVERRIDES_DIR / "main.html").is_file()
    assert (OVERRIDES_DIR / "assets" / "stylesheets" / "bifrost.css").is_file()


def test_plugin_does_not_inject_extra_css():
    """extra.css used to be auto-injected; ensure it no longer is."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    paths = [str(entry) for entry in result["extra_css"]]
    assert "assets/stylesheets/extra.css" not in paths


def test_plugin_preserves_existing_extra_css():
    """User-defined extra_css entries should not be clobbered by the plugin."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config["extra_css"].append("custom/user.css")
    config["extra_css"].append("custom/other.css")

    result = plugin.on_config(config)

    assert "custom/user.css" in result["extra_css"]
    assert "custom/other.css" in result["extra_css"]


# ---------------------------------------------------------------------------
# Markdown extensions
# ---------------------------------------------------------------------------


def test_default_extensions_injected():
    """All default extensions should be injected on a bare config."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    for ext in DEFAULT_EXTENSIONS:
        assert ext in result.markdown_extensions, (
            f"{ext} missing from markdown_extensions"
        )


def test_default_extension_configs_injected():
    """Builtin extension configs (e.g. toc permalink) should be set."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    assert result.mdx_configs.get("toc", {}).get("permalink") is True
    assert (
        result.mdx_configs.get("pymdownx.highlight", {}).get("anchor_linenums") is True
    )


def test_user_extension_config_preserved():
    """User-provided extension config must not be overwritten."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    # User sets their own toc config.
    config.markdown_extensions.append("toc")
    config.mdx_configs["toc"] = {"permalink": False, "toc_depth": 3}

    result = plugin.on_config(config)

    assert result.mdx_configs["toc"]["permalink"] is False
    assert result.mdx_configs["toc"]["toc_depth"] == 3


def test_no_duplicate_extensions():
    """Extensions already present should not be added again."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.markdown_extensions.append("admonition")
    config.markdown_extensions.append("abbr")

    result = plugin.on_config(config)

    assert result.markdown_extensions.count("admonition") == 1
    assert result.markdown_extensions.count("abbr") == 1


# ---------------------------------------------------------------------------
# Theme features
# ---------------------------------------------------------------------------


def test_default_features_injected():
    """All default theme features should be present after plugin runs."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    for feature in DEFAULT_FEATURES:
        assert feature in result.theme["features"], f"{feature} missing"


def test_no_duplicate_features():
    """Features already in config should not be duplicated."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.theme["features"] = ["navigation.instant", "content.code.copy"]

    result = plugin.on_config(config)

    features = result.theme["features"]
    assert features.count("navigation.instant") == 1
    assert features.count("content.code.copy") == 1


# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------


def test_default_fonts_disable_google_fonts():
    """With no user font, Google Fonts are disabled (Bifrost styles fonts via CSS)."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    assert result.theme["font"] is False


def test_user_fonts_preserved():
    """User-set fonts should not be overwritten."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.theme["font"] = {"text": "Inter", "code": "Fira Code"}

    result = plugin.on_config(config)

    assert result.theme["font"]["text"] == "Inter"
    assert result.theme["font"]["code"] == "Fira Code"


# ---------------------------------------------------------------------------
# Admonition icons
# ---------------------------------------------------------------------------


def test_admonition_icons_injected():
    """Default admonition icons should be set on a bare config."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    icons = result.theme["icon"]["admonition"]
    for key, value in DEFAULT_ADMONITION_ICONS.items():
        assert icons[key] == value


def test_user_admonition_icons_preserved():
    """User-provided admonition icons should not be overwritten."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.theme["icon"] = {"admonition": {"note": "material/pencil"}}

    result = plugin.on_config(config)

    assert result.theme["icon"]["admonition"]["note"] == "material/pencil"


def test_top_icon_injected():
    """The back-to-top icon should default to a Font Awesome arrow."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    assert result.theme["icon"]["top"] == DEFAULT_TOP_ICON


def test_user_top_icon_preserved():
    """A user-provided back-to-top icon should not be overwritten."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.theme["icon"] = {"top": "material/arrow-up"}

    result = plugin.on_config(config)

    assert result.theme["icon"]["top"] == "material/arrow-up"


# ---------------------------------------------------------------------------
# Palette
# ---------------------------------------------------------------------------


def test_default_palette_injected():
    """The minimal config should get a light/dark palette with a toggle."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    palette = result.theme["palette"]
    assert [entry["scheme"] for entry in palette] == ["light", "dark"]
    assert all("toggle" in entry for entry in palette)


def test_user_palette_preserved():
    """A user-provided palette should not be overwritten."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.theme["palette"] = [{"scheme": "slate", "primary": "purple"}]

    result = plugin.on_config(config)

    assert result.theme["palette"] == [{"scheme": "slate", "primary": "purple"}]


def test_default_palette_not_shared_across_configs():
    """Injected palette must be a copy, not the shared module constant."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)
    result.theme["palette"][0]["primary"] = "pink"

    assert DEFAULT_PALETTE[0]["primary"] == "teal"


# ---------------------------------------------------------------------------
# Extra JavaScript
# ---------------------------------------------------------------------------


def test_bifrost_theme_js_injected():
    """The Bifrost theme-sync script should be added to extra_javascript."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    paths = [str(entry) for entry in result.extra_javascript]
    assert "javascripts/bifrost-theme.js" in paths


def test_bifrost_theme_js_exists_in_overrides():
    """The bifrost-theme.js file should ship in the overrides directory."""
    assert (OVERRIDES_DIR / "javascripts" / "bifrost-theme.js").is_file()


def test_existing_extra_javascript_preserved():
    """User-provided extra_javascript entries should not be removed."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.extra_javascript.append("custom/app.js")

    result = plugin.on_config(config)

    paths = [str(entry) for entry in result.extra_javascript]
    assert "custom/app.js" in paths
    assert "javascripts/bifrost-theme.js" in paths


def test_no_duplicate_extra_javascript():
    """Default JS entries should not be duplicated if already present."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.extra_javascript.append("javascripts/bifrost-theme.js")

    result = plugin.on_config(config)

    theme_js_count = sum(
        1
        for entry in result.extra_javascript
        if (isinstance(entry, str) and entry == "javascripts/bifrost-theme.js")
    )
    assert theme_js_count == 1


# ---------------------------------------------------------------------------
# Critical extension configs (features that silently break if misconfigured)
# ---------------------------------------------------------------------------


def test_mermaid_custom_fence_configured():
    """Mermaid diagrams rely on the superfences custom fence being registered."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    fences = result.mdx_configs["pymdownx.superfences"]["custom_fences"]
    mermaid = next((f for f in fences if f.get("name") == "mermaid"), None)
    assert mermaid is not None, "mermaid custom fence not registered"
    assert mermaid["class"] == "mermaid"
    assert callable(mermaid["format"])


def test_emoji_generator_configured():
    """Emoji rendering needs both a generator and an index callable."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    emoji = result.mdx_configs["pymdownx.emoji"]
    assert callable(emoji["emoji_generator"])
    assert callable(emoji["emoji_index"])


# ---------------------------------------------------------------------------
# Font edge cases
# ---------------------------------------------------------------------------


def test_partial_font_text_only_preserved():
    """User setting only the text font keeps that font (fonts stay enabled)."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.theme["font"] = {"text": "Inter"}

    result = plugin.on_config(config)

    assert result.theme["font"]["text"] == "Inter"


def test_partial_font_code_only_preserved():
    """User setting only the code font keeps that font (fonts stay enabled)."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.theme["font"] = {"code": "Fira Code"}

    result = plugin.on_config(config)

    assert result.theme["font"]["code"] == "Fira Code"


def test_font_false_is_respected():
    """`font: false` disables Google Fonts and must not be re-enabled."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.theme["font"] = False

    result = plugin.on_config(config)

    assert result.theme["font"] is False


# ---------------------------------------------------------------------------
# Idempotency (on_config may run more than once, e.g. during `mkdocs serve`)
# ---------------------------------------------------------------------------


def test_on_config_is_idempotent():
    """Running on_config twice must not duplicate any injected config."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    plugin.on_config(config)
    result = plugin.on_config(config)

    overrides_dir = str(OVERRIDES_DIR.resolve())
    assert result.theme.dirs.count(overrides_dir) == 1
    assert result.markdown_extensions.count("admonition") == 1
    assert result.theme["features"].count("navigation.instant") == 1

    js_paths = [str(entry) for entry in result.extra_javascript]
    assert js_paths.count("javascripts/bifrost-theme.js") == 1


# ---------------------------------------------------------------------------
# Material stylesheet discovery (guards the cascade-layer setup)
#
# These tests are the safety net for Material upgrades: if a future
# mkdocs-material release changes its asset layout, discovery fails here in CI
# (e.g. on a Dependabot bump) rather than silently shipping a broken theme.
# ---------------------------------------------------------------------------


def test_discover_material_stylesheets_finds_main():
    """Discovery must resolve Material's hashed main stylesheet."""
    sheets = _discover_material_stylesheets()

    assert "main" in sheets
    assert sheets["main"].startswith("main.")
    assert sheets["main"].endswith(".min.css")


def test_discover_material_stylesheets_finds_palette():
    """Material ships a palette stylesheet; discovery should find it too."""
    sheets = _discover_material_stylesheets()

    assert "palette" in sheets
    assert sheets["palette"].startswith("palette.")
    assert sheets["palette"].endswith(".min.css")


def test_discover_raises_when_main_missing(monkeypatch, tmp_path):
    """A clear PluginError must fire if Material's layout changes (empty dir)."""
    import material

    empty = tmp_path / "templates" / "assets" / "stylesheets"
    empty.mkdir(parents=True)
    monkeypatch.setattr(material, "__file__", str(tmp_path / "__init__.py"))

    with pytest.raises(PluginError, match=r"main.*min\.css"):
        _discover_material_stylesheets()


def test_layer_bootstrap_css_content():
    """The generated bootstrap declares layer order and imports Material's CSS.

    @import paths must be bare filenames so the browser resolves them relative
    to the bootstrap stylesheet (its siblings), keeping them page-independent.
    """
    config = _minimal_config()

    css = _build_layer_bootstrap_css(config)

    # The @layer statement must come first, before any @import (otherwise
    # browsers drop the following @import rules).
    assert css.index("@layer material, bifrost-framework, bifrost-overrides;") == 0
    assert '@import "main.' in css
    assert "layer(material)" in css
    # Bare filenames, not page-relative or absolute URLs.
    assert "url(" not in css
    assert "assets/stylesheets/" not in css
    assert "../" not in css


def test_on_files_generates_layer_bootstrap():
    """on_files must emit the bootstrap stylesheet as a real site file."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()
    config = plugin.on_config(config)

    from mkdocs.structure.files import Files

    # File.generated tags the file with the plugin that created it, which mkdocs
    # only sets during event dispatch; emulate it for this isolated call.
    config.plugins._current_plugin = "intility-bifrost"

    files = plugin.on_files(Files([]), config=config)

    generated = files.get_file_from_path(BIFROST_LAYERS_CSS)
    assert generated is not None
    assert "@layer material, bifrost-framework, bifrost-overrides;" in (
        generated.content_string
    )


def test_main_html_links_layer_bootstrap():
    """The template loads the bootstrap via a stable <link>, not inline <style>.

    Material's navigation.instant re-appends per-page inline <style> @imports on
    every navigation, which breaks the cascade-layer order. A <link> stays
    identical across pages and is kept, so it must not be inlined.
    """
    raw = (OVERRIDES_DIR / "main.html").read_text(encoding="utf-8")
    # Strip Jinja comments so prose explaining the mechanism doesn't trip the
    # "not inlined" assertions below.
    main_html = re.sub(r"\{#.*?#\}", "", raw, flags=re.DOTALL)

    assert BIFROST_LAYERS_CSS in main_html
    # The layer setup must not be inlined in the template (it belongs in the
    # generated stylesheet so instant navigation keeps it stable).
    assert "@layer" not in main_html
    assert "layer(material)" not in main_html
    # bifrost-layers.css must precede bifrost.css so the order is declared first.
    assert main_html.index(BIFROST_LAYERS_CSS) < main_html.index(
        "assets/stylesheets/bifrost.css"
    )
    # super() must NOT be called in styles, or Material's unlayered <link> would
    # win over everything and defeat the layering.
    assert "{{ super() }}" not in main_html


# ---------------------------------------------------------------------------
# End-to-end build (proves the entry point loads and the pipeline produces a site)
# ---------------------------------------------------------------------------


def test_full_site_build(tmp_path):
    """A site using the plugin builds and references the Bifrost overrides."""
    from mkdocs.commands.build import build
    from mkdocs.config import load_config

    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "index.md").write_text("# Hello\n\nBody.\n", encoding="utf-8")

    mkdocs_yml = tmp_path / "mkdocs.yml"
    mkdocs_yml.write_text(
        "site_name: Smoke Test\n"
        "theme:\n"
        "  name: material\n"
        "plugins:\n"
        "  - intility-bifrost\n"
        "  - search\n",
        encoding="utf-8",
    )

    # load_config raises if the `intility-bifrost` entry point can't be resolved.
    config = load_config(str(mkdocs_yml))
    build(config)

    index_html = (tmp_path / "site" / "index.html").read_text(encoding="utf-8")
    # bifrost.css comes from the overrides theme dir; bifrost-theme.js from the
    # injected extra_javascript. Both present means the full pipeline ran.
    assert "assets/stylesheets/bifrost.css" in index_html
    assert "javascripts/bifrost-theme.js" in index_html
    # The cascade-layer bootstrap is loaded via a <link> (not inline <style>),
    # so instant navigation keeps it stable across pages.
    assert BIFROST_LAYERS_CSS in index_html
    assert "@layer" not in index_html

    # The generated bootstrap re-imports Material into the `material` layer.
    layers_css = (tmp_path / "site" / BIFROST_LAYERS_CSS).read_text(encoding="utf-8")
    assert "@layer material, bifrost-framework, bifrost-overrides;" in layers_css
    assert "layer(material)" in layers_css
    assert '@import "main.' in layers_css
