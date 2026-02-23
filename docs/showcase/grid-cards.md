# Grid Cards

Extension: `md_in_html`

## Examples

=== "Result"

    <div class="grid cards" markdown>

    - :material-clock-fast:{ .lg .middle } **Quick Setup**

        ---

        Get up and running in minutes with sensible defaults and minimal configuration.

    - :material-palette:{ .lg .middle } **Bifrost Theming**

        ---

        Four color schemes (teal, purple, pink, yellow) with automatic light/dark mode switching.

    - :material-format-font:{ .lg .middle } **Custom Typography**

        ---

        Satoshi for headings, Open Sans for body text, JetBrains Mono for code blocks.

    - :material-magnify:{ .lg .middle } **Full-text Search**

        ---

        Built-in search with suggestions, highlighting, and shareable search URLs.

    </div>

=== "Markdown"

    ```html
    <div class="grid cards" markdown>

    - :material-clock-fast:{ .lg .middle } **Quick Setup**

        ---

        Get up and running in minutes with sensible defaults
        and minimal configuration.

    - :material-palette:{ .lg .middle } **Bifrost Theming**

        ---

        Four color schemes with automatic light/dark mode.

    - :material-format-font:{ .lg .middle } **Custom Typography**

        ---

        Satoshi for headings, Open Sans for body text,
        JetBrains Mono for code blocks.

    - :material-magnify:{ .lg .middle } **Full-text Search**

        ---

        Built-in search with suggestions, highlighting,
        and shareable search URLs.

    </div>
    ```

## Syntax

The key parts:

- Wrap in `<div class="grid cards" markdown>` to enable grid layout and Markdown processing
- Each card is a list item (`-`) with an icon, title, divider (`---`), and description
- Use `{ .lg .middle }` on icons to size and align them
