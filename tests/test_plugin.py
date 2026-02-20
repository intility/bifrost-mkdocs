from __future__ import annotations

from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig

from intility_bifrost_mkdocs.plugin import IntilityBifrostPlugin


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


def test_plugin_injects_overrides_and_css():
    """The plugin should prepend its overrides dir and extra.css into the config."""
    plugin = IntilityBifrostPlugin()
    config = _minimal_config()

    original_dirs_len = len(config.theme.dirs)
    original_css = list(config["extra_css"])

    result = plugin.on_config(config)

    # Overrides dir is prepended (first entry = highest priority).
    overrides_dir = str((Path(__file__).parent.parent / "src" / "intility_bifrost_mkdocs" / "overrides").resolve())
    assert result.theme.dirs[0] == overrides_dir
    assert len(result.theme.dirs) == original_dirs_len + 1

    # extra.css is prepended to extra_css.
    assert result["extra_css"][0] == "assets/stylesheets/extra.css"
    assert result["extra_css"][1:] == original_css
