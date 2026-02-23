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

## Extension Reference

| Syntax | Result | Extension |
|--------|--------|-----------|
| `**bold**` | **bold** | built-in |
| `*italic*` | *italic* | built-in |
| `~~strikethrough~~` | ~~strikethrough~~ | `tilde` |
| `==highlight==` | ==highlight== | `mark` |
| `^^superscript^^` | ^^superscript^^ | `caret` |
| `~subscript~` | ~subscript~ | `tilde` |
