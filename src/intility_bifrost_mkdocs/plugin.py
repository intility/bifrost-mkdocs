from pathlib import Path

from mkdocs.plugins import BasePlugin


class IntilityBifrostPlugin(BasePlugin):
    """MkDocs plugin that applies the Intility Bifrost theme to Material for MkDocs.

    Injects the Bifrost theme overrides (main.html, bifrost.css, fonts) and
    extra.css into the MkDocs build. Users only need to add ``intility-bifrost``
    to their plugins list -- no ``custom_dir`` or ``extra_css`` required.
    """

    def on_config(self, config):
        overrides_dir = Path(__file__).parent / "overrides"

        # Insert our overrides as the highest-priority theme directory.
        # MkDocs discovers both templates (main.html) and static assets
        # (CSS, fonts) from entries in theme.dirs.
        config.theme.dirs.insert(0, str(overrides_dir.resolve()))

        # Inject extra.css so it gets a <link> tag in every page.
        # Prepend so user-defined extra_css can still override our styles.
        config["extra_css"] = [
            "assets/stylesheets/extra.css",
        ] + config["extra_css"]

        return config
