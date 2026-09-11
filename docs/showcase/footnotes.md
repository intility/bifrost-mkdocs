# Footnotes

Extension: `footnotes`

## Examples

=== "Result"

    Zensical[^1] is a static site generator from the Material for MkDocs team. It replaces Material for MkDocs[^2], which reaches end of life on 2026-11-05.

    [^1]: Zensical is the successor to Material for MkDocs. See [zensical.org](https://zensical.org/) for more.
    [^2]: Material for MkDocs was maintained by Martin Donath. It supported over 60 languages and dozens of plugins.

=== "Markdown"

    ```markdown
    Zensical[^1] is a static site generator from the Material
    for MkDocs team. It replaces Material for MkDocs[^2], which
    reaches end of life on 2026-11-05.

    [^1]: Zensical is the successor to Material for MkDocs.
    [^2]: Material for MkDocs was maintained by Martin Donath.
        It supported over 60 languages and dozens of plugins.
    ```

## Syntax

```markdown
Reference in text: [^label]
Definition:        [^label]: Footnote content here
```

Footnotes are collected and rendered at the bottom of the page, regardless of where the definitions appear in the source.
