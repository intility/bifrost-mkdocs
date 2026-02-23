# Bifrost MkDocs Theme

A custom MkDocs theme that implements Intility's Bifrost design system while extending Material for MkDocs functionality.

## Structure

```
theme/
├── assets/
│   └── stylesheets/
│       └── bifrost.css          # Main Bifrost theme stylesheet
├── partials/                     # Custom template partials (future use)
├── main.html                     # Main theme template (includes inline JS)
└── README.md                     # This file
```

## Features

- **Bifrost Design System**: Full implementation of Intility's design system
- **Light/Dark Mode**: Automatic theme switching with Bifrost color variables
- **Material Features**: All Material for MkDocs features (search, navigation, responsive)
- **Typography**: Satoshi for headings, Open Sans for body text
- **Components**: Styled admonitions, code blocks, tables, buttons, and more

## How It Works

1. **Base Theme**: Extends Material for MkDocs (`name: material`)
2. **Custom Directory**: Uses `custom_dir: theme` to override templates
3. **Bifrost CSS**: Imports Bifrost CSS framework from CDN which provides all color variables
4. **Inline JavaScript**: Observes Material's `data-md-color-scheme` and `data-md-color-primary` attributes and applies corresponding Bifrost classes to `<html>`
5. **Color Variables**: Uses Bifrost's CSS variables (`--bfc-*`) directly - no hardcoded colors!
6. **Configuration-Driven**: Theme colors set via `mkdocs.yaml` palette configuration

## Customization

### Changing Theme Color

Edit `mkdocs.yaml` and set the `primary` color using a YAML anchor (defined once, reused for both light and dark modes):

```yaml
theme:
  palette:
    - scheme: light
      primary: &bifrost_theme teal  # Options: teal, purple, pink, yellow
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: dark
      primary: *bifrost_theme  # Reuses the theme defined above
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

The `primary` value maps directly to Bifrost themes:
- `teal` → `.bf-theme-teal` (default)
- `purple` → `.bf-theme-purple`
- `pink` → `.bf-theme-pink`
- `yellow` → `.bf-theme-yellow`

**Note:** The `&bifrost_theme` creates a YAML anchor, and `*bifrost_theme` references it. This ensures both light and dark modes use the same theme color. Simply change `teal` to another theme name to update the entire site.

### Light/Dark Mode

Use `scheme: light` for light mode and `scheme: dark` for dark mode in your palette configuration. These map to Bifrost's `.bf-lightmode` and `.bf-darkmode` classes.

### Example: Purple Theme

To switch to the purple Bifrost theme, just change the anchor value:

```yaml
theme:
  palette:
    - scheme: light
      primary: &bifrost_theme purple  # Changed from teal to purple
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: dark
      primary: *bifrost_theme
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

### Adding Custom Styles

Add custom CSS to `theme/assets/stylesheets/bifrost.css` at the end of the file.

### Creating Custom Templates

Add custom Jinja2 templates to `theme/partials/` to override Material components.

## Dependencies

- **MkDocs**: >=1.5.0
- **Material for MkDocs**: >=9.5.0
- **Bifrost CSS**: Latest from CDN (https://unpkg.com/@intility/bifrost-css@latest/dist/bifrost-all.css)

## Documentation

- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Bifrost Design System](https://bifrost.intility.com/)

## Maintenance

To update the theme:

1. Edit files in `theme/` directory
2. Run `mkdocs build` to test
3. Commit changes to version control
4. Deploy to GitHub Pages
