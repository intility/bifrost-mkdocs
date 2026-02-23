from __future__ import annotations

from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig

from intility_bifrost_mkdocs.plugin import (
    DEFAULT_ADMONITION_ICONS,
    DEFAULT_EXTENSIONS,
    DEFAULT_EXTRA_JS,
    DEFAULT_FEATURES,
    BIFROST_FONT_CODE,
    BIFROST_FONT_TEXT,
    IntilityBifrostPlugin,
)

OVERRIDES_DIR = Path(__file__).parent.parent / "src" / "intility_bifrost_mkdocs" / "overrides"


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
    errors, warnings = cfg.validate()
    assert not errors, errors
    return cfg


# ---------------------------------------------------------------------------
# Original tests (preserved)
# ---------------------------------------------------------------------------


def test_plugin_injects_overrides_and_css():
    """The plugin should prepend its overrides dir and extra.css into the config."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    original_dirs_len = len(config.theme.dirs)
    original_css = list(config["extra_css"])

    result = plugin.on_config(config)

    # Overrides dir is prepended (first entry = highest priority).
    overrides_dir = str(OVERRIDES_DIR.resolve())
    assert result.theme.dirs[0] == overrides_dir
    assert len(result.theme.dirs) == original_dirs_len + 1

    # extra.css is prepended to extra_css.
    assert result["extra_css"][0] == "assets/stylesheets/extra.css"
    assert result["extra_css"][1:] == original_css


def test_overrides_directory_exists():
    """The overrides directory should contain the expected theme files."""
    assert OVERRIDES_DIR.is_dir()
    assert (OVERRIDES_DIR / "main.html").is_file()
    assert (OVERRIDES_DIR / "assets" / "stylesheets" / "extra.css").is_file()
    assert (OVERRIDES_DIR / "assets" / "stylesheets" / "bifrost.css").is_file()
    assert (OVERRIDES_DIR / "assets" / "fonts" / "satoshi-variable.woff2").is_file()
    assert (OVERRIDES_DIR / "assets" / "fonts" / "satoshi-variable-italic.woff2").is_file()


def test_plugin_preserves_existing_extra_css():
    """User-defined extra_css entries should not be clobbered by the plugin."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config["extra_css"].append("custom/user.css")
    config["extra_css"].append("custom/other.css")

    result = plugin.on_config(config)

    assert result["extra_css"][0] == "assets/stylesheets/extra.css"
    assert "custom/user.css" in result["extra_css"]
    assert "custom/other.css" in result["extra_css"]
    assert result["extra_css"].index("assets/stylesheets/extra.css") < result["extra_css"].index("custom/user.css")


# ---------------------------------------------------------------------------
# Markdown extensions
# ---------------------------------------------------------------------------


def test_default_extensions_injected():
    """All default extensions should be injected on a bare config."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    for ext in DEFAULT_EXTENSIONS:
        assert ext in result.markdown_extensions, f"{ext} missing from markdown_extensions"


def test_default_extension_configs_injected():
    """Builtin extension configs (e.g. toc permalink) should be set."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    assert result.mdx_configs.get("toc", {}).get("permalink") is True
    assert result.mdx_configs.get("pymdownx.arithmatex", {}).get("generic") is True
    assert result.mdx_configs.get("pymdownx.highlight", {}).get("anchor_linenums") is True


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


def test_bifrost_fonts_replace_material_defaults():
    """Material's default Roboto fonts should be replaced with Bifrost fonts."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    assert result.theme["font"]["text"] == BIFROST_FONT_TEXT
    assert result.theme["font"]["code"] == BIFROST_FONT_CODE


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


# ---------------------------------------------------------------------------
# Extra JavaScript (MathJax)
# ---------------------------------------------------------------------------


def test_mathjax_js_injected():
    """MathJax JS entries should be added to extra_javascript."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    result = plugin.on_config(config)

    paths = [str(entry) for entry in result.extra_javascript]
    assert "javascripts/mathjax.js" in paths
    assert "https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js" in paths


def test_existing_extra_javascript_preserved():
    """User-provided extra_javascript entries should not be removed."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.extra_javascript.append("custom/app.js")

    result = plugin.on_config(config)

    paths = [str(entry) for entry in result.extra_javascript]
    assert "custom/app.js" in paths
    assert "javascripts/mathjax.js" in paths


def test_no_duplicate_mathjax_js():
    """MathJax entries should not be duplicated if already present."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    config.extra_javascript.append("javascripts/mathjax.js")

    result = plugin.on_config(config)

    mathjax_count = sum(
        1
        for entry in result.extra_javascript
        if (isinstance(entry, str) and entry == "javascripts/mathjax.js")
    )
    assert mathjax_count == 1


# ---------------------------------------------------------------------------
# Overrides file checks
# ---------------------------------------------------------------------------


def test_mathjax_js_exists_in_overrides():
    """The mathjax.js file should exist in the overrides directory."""
    assert (OVERRIDES_DIR / "javascripts" / "mathjax.js").is_file()
