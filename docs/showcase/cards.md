# Cards

Extension: `md_in_html`

## Examples

=== "Result"

    <div class="grid cards" markdown>

    - :material-download:{ .lg .middle } **Installation**

        ---

        Install the plugin with pip and add it to your `mkdocs.yml`.

    - :material-cog:{ .lg .middle } **Configuration**

        ---

        Override any injected default by setting it explicitly in your config.

    - :material-file-document:{ .lg .middle } **Writing Content**

        ---

        Write standard Markdown; the enabled extensions handle the rest.

    - :material-rocket-launch:{ .lg .middle } **Deployment**

        ---

        Build the static site and publish the output anywhere.

    </div>

=== "Markdown"

    ```html
    <div class="grid cards" markdown>

    - :material-download:{ .lg .middle } **Installation**

        ---

        Install the plugin with pip and add it to your `mkdocs.yml`.

    - :material-cog:{ .lg .middle } **Configuration**

        ---

        Override any injected default by setting it
        explicitly in your config.

    - :material-file-document:{ .lg .middle } **Writing Content**

        ---

        Write standard Markdown; the enabled extensions
        handle the rest.

    - :material-rocket-launch:{ .lg .middle } **Deployment**

        ---

        Build the static site and publish the output anywhere.

    </div>
    ```

## Link cards

Make the header a link and the whole card becomes clickable, like a Bifrost
link-section. Add a trailing arrow icon for the affordance: it slides on hover.

=== "Result"

    <div class="grid cards" markdown>

    - [:material-book-open-variant:{ .lg .middle } **Getting Started** :material-arrow-right:](../index.md)

        ---

        Install the theme and configure your first site.

    - [:material-palette:{ .lg .middle } **Theming Guide** :material-arrow-right:](index.md)

        ---

        Browse every component the theme styles.

    </div>

=== "Markdown"

    ```html
    <div class="grid cards" markdown>

    - [:material-book-open-variant:{ .lg .middle } **Getting Started** :material-arrow-right:](../index.md)

        ---

        Install the theme and configure your first site.

    - [:material-palette:{ .lg .middle } **Theming Guide** :material-arrow-right:](index.md)

        ---

        Browse every component the theme styles.

    </div>
    ```

## Syntax

The key parts:

- Wrap in `<div class="grid cards" markdown>` to enable grid layout and Markdown processing
- Each card is a list item (`-`) with an icon, title, divider (`---`), and description
- Use `{ .lg .middle }` on icons to size and align them

For a **link card**, wrap the whole header in a link (`[ ... ](url)`) and add a
trailing `:material-arrow-right:`. The entire card becomes clickable and the
arrow slides on hover. Cards without a header link stay static.
