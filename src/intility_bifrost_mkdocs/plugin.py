from __future__ import annotations

from pathlib import Path
from typing import Any

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin

# ---------------------------------------------------------------------------
# Default markdown extensions the plugin injects.
# ---------------------------------------------------------------------------
DEFAULT_EXTENSIONS: list[str] = [
    "abbr",
    "admonition",
    "attr_list",
    "def_list",
    "footnotes",
    "md_in_html",
    "toc",
    "pymdownx.arithmatex",
    "pymdownx.betterem",
    "pymdownx.caret",
    "pymdownx.details",
    "pymdownx.emoji",
    "pymdownx.highlight",
    "pymdownx.inlinehilite",
    "pymdownx.keys",
    "pymdownx.mark",
    "pymdownx.smartsymbols",
    "pymdownx.snippets",
    "pymdownx.superfences",
    "pymdownx.tabbed",
    "pymdownx.tasklist",
    "pymdownx.tilde",
    "tables",
]

# ---------------------------------------------------------------------------
# Default theme features.
# ---------------------------------------------------------------------------
DEFAULT_FEATURES: list[str] = [
    "navigation.instant",
    "navigation.instant.progress",
    "navigation.instant.prefetch",
    "navigation.tabs",
    "navigation.sections",
    "navigation.path",
    "navigation.top",
    "toc.follow",
    "search.suggest",
    "search.highlight",
    "search.share",
    "content.code.copy",
    "content.code.annotate",
]

# ---------------------------------------------------------------------------
# Default fonts (Bifrost branding).
# ---------------------------------------------------------------------------
BIFROST_FONT_TEXT = "Open Sans"
BIFROST_FONT_CODE = "JetBrains Mono"

# Material's defaults that we replace when the user hasn't customized them.
MATERIAL_DEFAULT_FONT_TEXT = "Roboto"
MATERIAL_DEFAULT_FONT_CODE = "Roboto Mono"

# ---------------------------------------------------------------------------
# Default admonition icons.
# ---------------------------------------------------------------------------
DEFAULT_ADMONITION_ICONS: dict[str, str] = {
    "note": "fontawesome/solid/note-sticky",
    "abstract": "fontawesome/solid/clipboard",
    "info": "fontawesome/solid/circle-info",
    "tip": "fontawesome/solid/lightbulb",
    "success": "fontawesome/solid/check",
    "question": "fontawesome/solid/circle-question",
    "warning": "fontawesome/solid/triangle-exclamation",
    "failure": "fontawesome/solid/bomb",
    "danger": "fontawesome/solid/skull",
    "bug": "fontawesome/solid/robot",
    "example": "fontawesome/solid/flask",
    "quote": "fontawesome/solid/quote-left",
}

# ---------------------------------------------------------------------------
# Default extra JavaScript (MathJax).
# ---------------------------------------------------------------------------
DEFAULT_EXTRA_JS: list[str] = [
    "javascripts/mathjax.js",
    "https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js",
]


def _default_mdx_configs() -> dict[str, dict[str, Any]]:
    """Build default extension configs.

    Returned as a function because ``pymdownx.emoji`` and
    ``pymdownx.superfences`` reference Python callables that must be
    imported at call-time.
    """
    from material.extensions.emoji import to_svg, twemoji
    from pymdownx.superfences import fence_code_format

    return {
        "toc": {"permalink": True},
        "pymdownx.arithmatex": {"generic": True},
        "pymdownx.betterem": {"smart_enable": "all"},
        "pymdownx.emoji": {
            "emoji_generator": to_svg,
            "emoji_index": twemoji,
        },
        "pymdownx.highlight": {
            "anchor_linenums": True,
            "line_spans": "__span",
            "pygments_lang_class": True,
        },
        "pymdownx.superfences": {
            "custom_fences": [
                {
                    "name": "mermaid",
                    "class": "mermaid",
                    "format": fence_code_format,
                },
            ],
        },
        "pymdownx.tabbed": {"alternate_style": True},
        "pymdownx.tasklist": {"custom_checkbox": True},
    }


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------


def _inject_markdown_extensions(config: MkDocsConfig) -> None:
    """Add default markdown extensions and their configs if not already set."""
    defaults = _default_mdx_configs()

    for ext in DEFAULT_EXTENSIONS:
        if ext not in config.markdown_extensions:
            config.markdown_extensions.append(ext)

        # Only inject default config for extensions the user hasn't configured.
        if ext in defaults and ext not in config.mdx_configs:
            config.mdx_configs[ext] = defaults[ext]


def _inject_theme_features(config: MkDocsConfig) -> None:
    """Add default theme features if not already present."""
    existing = set(config.theme.get("features") or [])
    features = list(config.theme.get("features") or [])

    for feature in DEFAULT_FEATURES:
        if feature not in existing:
            features.append(feature)

    config.theme["features"] = features


def _inject_theme_settings(config: MkDocsConfig) -> None:
    """Set Bifrost fonts and admonition icons when the user hasn't customized them."""
    # Fonts: only replace Material's default Roboto fonts.
    font = config.theme.get("font") or {}
    if isinstance(font, dict):
        text_font = font.get("text", MATERIAL_DEFAULT_FONT_TEXT)
        code_font = font.get("code", MATERIAL_DEFAULT_FONT_CODE)

        if text_font == MATERIAL_DEFAULT_FONT_TEXT:
            font["text"] = BIFROST_FONT_TEXT
        if code_font == MATERIAL_DEFAULT_FONT_CODE:
            font["code"] = BIFROST_FONT_CODE

        config.theme["font"] = font

    # Admonition icons: only inject if user hasn't set any.
    icon = config.theme.get("icon") or {}
    if not icon.get("admonition"):
        icon["admonition"] = dict(DEFAULT_ADMONITION_ICONS)
        config.theme["icon"] = icon


def _inject_extra_javascript(config: MkDocsConfig) -> None:
    """Add MathJax JS entries if not already present."""
    existing = {str(entry) for entry in config.extra_javascript}

    for entry in DEFAULT_EXTRA_JS:
        if entry not in existing:
            config.extra_javascript.append(entry)


# ---------------------------------------------------------------------------
# Plugin class
# ---------------------------------------------------------------------------


class IntilityBifrostPlugin(BasePlugin):
    """MkDocs plugin that applies the Intility Bifrost theme to Material for MkDocs.

    Injects Bifrost theme overrides, sensible default markdown extensions, theme
    features, fonts, icons, and MathJax configuration. Users only need to add
    ``intility-bifrost`` to their plugins list for a fully configured Bifrost
    experience.
    """

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        overrides_dir = Path(__file__).parent / "overrides"

        # Insert our overrides as the highest-priority theme directory.
        config.theme.dirs.insert(0, str(overrides_dir.resolve()))

        # Inject extra.css so it gets a <link> tag in every page.
        config["extra_css"] = [
            "assets/stylesheets/extra.css",
        ] + config["extra_css"]

        # Inject sensible defaults (never overwrites user-provided config).
        _inject_markdown_extensions(config)
        _inject_theme_features(config)
        _inject_theme_settings(config)
        _inject_extra_javascript(config)

        return config
