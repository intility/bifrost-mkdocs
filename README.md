# MkDocs Bifrost Template

A template repository for creating beautiful documentation sites using MkDocs with Bifrost-themed Material design.

## Overview

This template provides a ready-to-use setup for MkDocs documentation with:

- **Material for MkDocs theme** with custom Bifrost branding
- **Multiple color schemes** (teal, purple, pink, yellow)
- **Dark mode support** with toggle
- **Enhanced navigation** with tabs, sections, and instant loading
- **Search functionality** with suggestions and highlighting
- **Code syntax highlighting** with copy button
- **Mermaid diagram support**
- **Git revision dates** showing when pages were last updated

## Documentation

Once deployed, your documentation will be available at https://intility.github.io/<your-project>

## Local Development

To build and serve the documentation locally:

### Prerequisites

- Python 3.x
- pip

### Setup

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Serve locally 
mkdocs serve
```

The documentation will be available at http://127.0.0.1:8000

Visit the site and make changes to your documentation - the browser will automatically reload!

**Note:** Remember to activate the virtual environment (`source venv/bin/activate`) each time you work on the documentation.

### Building

```bash
# Build static site
mkdocs build

# Output will be in the site/ directory
```

## Getting Started with This Template

### 1. Use This Template

Click the "Use this template" button on GitHub to create a new repository based on this template.

### 2. Customize Configuration

Edit `mkdocs.yaml` to customize:

- `site_name`: Your project name
- `site_description`: Brief description of your project
- `site_author`: Your name or organization
- `site_url`: Your GitHub Pages URL (https://[username].github.io/[repo-name])
- `repo_name`: Your GitHub repo (username/repo-name)
- `repo_url`: Full GitHub repository URL
- `theme.palette.primary`: Choose from teal, purple, pink, or yellow

### 3. Add Your Content

Add your documentation markdown files in the `docs/` directory and update the `nav` section in `mkdocs.yaml`.

### 4. Deploy

Push to GitHub and enable GitHub Pages in your repository settings (deploy from `gh-pages` branch).

## Project Structure

```
.
├── docs/                          # Documentation source files
│   └── index.md                   # Home page (customize this!)
├── theme/                         # Custom theme overrides
│   ├── overrides/                 # Template overrides
│   └── stylesheets/               # Custom CSS
├── mkdocs.yaml                    # MkDocs configuration
├── requirements.txt               # Python dependencies
├── .github/
│   └── workflows/
│       └── deploy-docs.yml        # Auto-deploy to GitHub Pages
└── README.md                      # This file
```

## Customization

### Changing the Theme Color

In `mkdocs.yaml`, modify the `primary` color (line 17):

```yaml
primary: &bifrost_theme teal  # Options: teal, purple, pink, yellow
```

### Adding Custom Styles

Add custom CSS files to `theme/stylesheets/` and reference them in `mkdocs.yaml`:

```yaml
extra_css:
  - stylesheets/custom.css
```

### Customizing the Navigation

Edit the `nav` section in `mkdocs.yaml` to structure your documentation:

```yaml
nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - Guides:
      - Installation: guides/installation.md
      - Configuration: guides/configuration.md
  - API Reference: api/index.md
```

## Features Included

### Navigation & UX
- **Tabbed navigation** with sections and expansion
- **Instant loading** with progress indicator
- **Back to top** button
- **URL tracking** for navigation state
- **Edit buttons** on each page (links to GitHub)

### Search
- **Full-text search** across all documentation
- **Search suggestions** as you type
- **Search highlighting** in results
- **Search sharing** via URL

### Content Features
- **Code blocks** with syntax highlighting and copy button
- **Annotations** for code explanations
- **Admonitions** (notes, warnings, tips, etc.)
- **Tabbed content** for alternative instructions
- **Tables** with sorting support
- **Mermaid diagrams** for flowcharts and diagrams
- **Emoji support** via Material emoji set

### Metadata
- **Git revision dates** showing last updated time
- **Creation dates** for each page
- **Author information**

### Theming
- **Bifrost color schemes**: teal, purple, pink, yellow
- **Dark/light mode toggle**
- **Responsive design** for mobile and desktop

## Requirements

See `requirements.txt` for all dependencies. Main packages:

- `mkdocs-material` - Material theme for MkDocs
- `mkdocs-git-revision-date-localized-plugin` - Git metadata plugin

## License

This template is provided as-is for creating documentation sites.

## Support

For issues with this template:

- Open an issue on GitHub
- Check the [MkDocs documentation](https://www.mkdocs.org/)
- Check the [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)

## Credits

Built with:

- [MkDocs](https://www.mkdocs.org/) - Static site generator
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Beautiful theme
- [GitHub Pages](https://pages.github.com/) - Free hosting
- Bifrost styling by Intility AS
