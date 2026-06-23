from __future__ import annotations

from pathlib import Path
from typing import Any

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import PluginError
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File, Files

# Path (relative to the docs site root) of the generated cascade-layer
# bootstrap stylesheet. See `_build_layer_bootstrap_css` and `main.html`.
BIFROST_LAYERS_CSS = "assets/stylesheets/bifrost-layers.css"

# ---------------------------------------------------------------------------
# Default markdown extensions the plugin injects.
# ---------------------------------------------------------------------------
DEFAULT_EXTENSIONS: list[str] = [
    "abbr",
    "admonition",
    "github-callouts",
    "attr_list",
    "def_list",
    "footnotes",
    "md_in_html",
    "toc",
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
    # Stamps `.bf-table` onto generated tables so Bifrost's framework CSS
    # styles them. See intility_bifrost_mkdocs/table_ext.py.
    "intility_bifrost_mkdocs.table_ext",
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
    "content.tabs.link",
]

# ---------------------------------------------------------------------------
# Fonts (Bifrost branding).
# ---------------------------------------------------------------------------
# Bifrost ships Satoshi (vendored) for all text and JetBrains Mono (vendored)
# for code, both applied via CSS (see tokens.css). No Google Fonts are needed,
# so we disable them unless the user picked their own font.
#
# Material's defaults, used to detect whether the user customized the font.
MATERIAL_DEFAULT_FONT_TEXT = "Roboto"
MATERIAL_DEFAULT_FONT_CODE = "Roboto Mono"

# ---------------------------------------------------------------------------
# Default admonition icons.
# ---------------------------------------------------------------------------
# Icons mirror Bifrost's Message component, which demonstrates circle-info
# (theme), heart (attn), circle-exclamation (warning) and triangle-exclamation
# (alert). The remaining types reuse that circle/triangle family for a
# consistent look. Each type also maps to a Bifrost state in messages.css.
DEFAULT_ADMONITION_ICONS: dict[str, str] = {
    # theme
    "note": "fontawesome/solid/circle-info",
    "info": "fontawesome/solid/circle-info",
    "todo": "fontawesome/solid/circle-info",
    # chill
    "abstract": "fontawesome/solid/circle-info",
    "example": "fontawesome/solid/circle-info",
    "question": "fontawesome/solid/circle-question",
    # success
    "tip": "fontawesome/solid/circle-check",
    "success": "fontawesome/solid/circle-check",
    # warning
    "warning": "fontawesome/solid/circle-exclamation",
    # attn
    "attention": "fontawesome/solid/heart",
    # alert (caution lives here too: `!!! caution` and GitHub `[!CAUTION]`)
    "failure": "fontawesome/solid/triangle-exclamation",
    "danger": "fontawesome/solid/triangle-exclamation",
    "error": "fontawesome/solid/triangle-exclamation",
    "bug": "fontawesome/solid/triangle-exclamation",
    "caution": "fontawesome/solid/triangle-exclamation",
    # chill (GitHub `[!IMPORTANT]`)
    "important": "fontawesome/solid/circle-exclamation",
    # neutral
    "quote": "fontawesome/solid/quote-left",
}

# Back-to-top button icon. Material defaults to a Material Design arrow; use a
# Font Awesome one to stay consistent with the rest of the theme's icons.
DEFAULT_TOP_ICON = "fontawesome/solid/arrow-up"

# ---------------------------------------------------------------------------
# Default extra JavaScript.
# ---------------------------------------------------------------------------
DEFAULT_EXTRA_JS: list[str] = [
    "javascripts/bifrost-theme.js",
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
    # Fonts: Bifrost styles all text (vendored Satoshi) and code (system
    # monospace) via CSS, so no Google Fonts are needed. Disable them by
    # default. `font: false` (the user's or ours) is respected, and a user who
    # set their own font keeps it.
    font = config.theme.get("font")
    if font is not False:
        font = font or {}
        if isinstance(font, dict):
            text_font = font.get("text", MATERIAL_DEFAULT_FONT_TEXT)
            code_font = font.get("code", MATERIAL_DEFAULT_FONT_CODE)

            customized = (
                text_font != MATERIAL_DEFAULT_FONT_TEXT
                or code_font != MATERIAL_DEFAULT_FONT_CODE
            )
            config.theme["font"] = font if customized else False

    # Icons: only inject defaults the user hasn't set.
    icon = config.theme.get("icon") or {}
    if not icon.get("admonition"):
        icon["admonition"] = dict(DEFAULT_ADMONITION_ICONS)
    if not icon.get("top"):
        icon["top"] = DEFAULT_TOP_ICON
    config.theme["icon"] = icon


def _inject_extra_javascript(config: MkDocsConfig) -> None:
    """Add default extra JavaScript entries if not already present."""
    existing = {str(entry) for entry in config.extra_javascript}

    for entry in DEFAULT_EXTRA_JS:
        if entry not in existing:
            config.extra_javascript.append(entry)


def _discover_material_stylesheets() -> dict[str, str]:
    """Find Material's hashed stylesheet filenames in the installed package.

    Material ships ``main.<hash>.min.css`` and ``palette.<hash>.min.css`` with a
    content hash that changes on every release. Our theme demotes Material into a
    low-priority ``@layer`` by re-importing those stylesheets (see ``main.html``),
    which means we must resolve the hashed names at build time rather than
    hardcoding them. Discovering them here keeps the layering working across
    Material upgrades automatically.

    Returns a mapping with a ``"main"`` key and, when present, a ``"palette"``
    key. Raises ``PluginError`` (failing the build with an actionable message)
    if Material's main stylesheet cannot be located.
    """
    import material

    stylesheets = (
        Path(material.__file__).parent / "templates" / "assets" / "stylesheets"
    )
    main_matches = sorted(stylesheets.glob("main.*.min.css"))
    palette_matches = sorted(stylesheets.glob("palette.*.min.css"))

    if not main_matches:
        raise PluginError(
            "intility-bifrost: could not locate Material's 'main.*.min.css' in "
            f"{stylesheets}. The Bifrost theme re-imports it into a cascade layer, "
            "so this is required. mkdocs-material likely changed its asset layout; "
            "please open an issue at https://github.com/intility/bifrost-mkdocs."
        )

    sheets = {"main": main_matches[0].name}
    if palette_matches:
        sheets["palette"] = palette_matches[0].name
    return sheets


def _build_layer_bootstrap_css(config: MkDocsConfig) -> str:
    """Build the contents of the cascade-layer bootstrap stylesheet.

    This stylesheet declares the layer order and re-imports Material's CSS into
    the low-priority ``material`` layer. It is emitted as a real file (see
    ``on_files``) and loaded via a plain ``<link>`` rather than an inline
    ``<style>``.

    Why a file instead of inline ``<style>`` in ``main.html``: Material's
    ``navigation.instant`` rewrites ``href``/``src`` *attributes* to absolute
    URLs before diffing ``<head>``, so a ``<link>`` stays byte-identical across
    pages and is kept untouched on navigation. It cannot normalise a URL living
    inside inline ``<style>`` text, so a page-relative ``@import`` there makes
    the element differ per page; instant navigation then re-appends it on every
    visit, which breaks the cascade-layer order and flashes unstyled content.

    The ``@import`` paths are written *bare* (filename only) so the browser
    resolves them relative to this stylesheet's own URL, i.e. its siblings in
    ``assets/stylesheets/`` -- making them page-independent.
    """
    sheets = _discover_material_stylesheets()

    lines = ["@layer material, bifrost-framework, bifrost-overrides;"]
    lines.append(f'@import "{sheets["main"]}" layer(material);')
    if config.theme.get("palette") and "palette" in sheets:
        lines.append(f'@import "{sheets["palette"]}" layer(material);')

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Plugin class
# ---------------------------------------------------------------------------


class IntilityBifrostPlugin(BasePlugin):
    """MkDocs plugin that applies the Intility Bifrost theme to Material for MkDocs.

    Injects Bifrost theme overrides, sensible default markdown extensions, theme
    features, fonts, and icons. Users only need to add ``intility-bifrost`` to
    their plugins list for a fully configured Bifrost experience.
    """

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        overrides_dir = str((Path(__file__).parent / "overrides").resolve())

        # Insert our overrides as the highest-priority theme directory.
        # Guard against re-insertion if on_config runs more than once.
        if overrides_dir not in config.theme.dirs:
            config.theme.dirs.insert(0, overrides_dir)

        # Inject sensible defaults (never overwrites user-provided config).
        _inject_markdown_extensions(config)
        _inject_theme_features(config)
        _inject_theme_settings(config)
        _inject_extra_javascript(config)

        # Fail fast at config time with an actionable message if Material's
        # stylesheets can't be located; the bootstrap file generated in
        # `on_files` depends on them.
        _discover_material_stylesheets()

        return config

    def on_files(self, files: Files, *, config: MkDocsConfig) -> Files:
        """Emit the cascade-layer bootstrap stylesheet as a real file.

        Loaded via a stable ``<link>`` in ``main.html`` so Material's instant
        navigation never re-appends it (see ``_build_layer_bootstrap_css``).
        """
        files.append(
            File.generated(
                config,
                BIFROST_LAYERS_CSS,
                content=_build_layer_bootstrap_css(config),
            )
        )
        return files
