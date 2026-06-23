# Typography & Text Formatting

Extensions: `pymdownx.caret`, `pymdownx.mark`, `pymdownx.tilde`, `pymdownx.betterem`

## Basic Formatting

=== "Result"

    Regular text with **bold**, *italic*, ***bold italic***, ~~strikethrough~~, ==highlighted text==, ^^superscript^^, and ~subscript~.

=== "Markdown"

    ```markdown
    Regular text with **bold**, *italic*, ***bold italic***,
    ~~strikethrough~~, ==highlighted text==, ^^superscript^^,
    and ~subscript~.
    ```

## Combined Formatting

=== "Result"

    **==bold and highlighted==**, ~~*strikethrough italic*~~, ^^superscript **bold**^^

=== "Markdown"

    ```markdown
    **==bold and highlighted==**, ~~*strikethrough italic*~~,
    ^^superscript **bold**^^
    ```

## Headings

Headings build the page structure and the table of contents. The TOC in the
right sidebar nests one level per heading depth, so a section like this one
shows the connector markers at every level.

### Second-level heading

A `###` heading nests under its `##` parent in the table of contents.

#### Third-level heading

A `####` heading nests one level deeper, demonstrating the third-level marker.

## Extension Reference

| Syntax | Result | Extension |
|--------|--------|-----------|
| `**bold**` | **bold** | built-in |
| `*italic*` | *italic* | built-in |
| `~~strikethrough~~` | ~~strikethrough~~ | `tilde` |
| `==highlight==` | ==highlight== | `mark` |
| `^^superscript^^` | ^^superscript^^ | `caret` |
| `~subscript~` | ~subscript~ | `tilde` |
