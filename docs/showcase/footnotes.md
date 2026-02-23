# Footnotes

Extension: `footnotes`

## Examples

=== "Result"

    MkDocs[^1] is a static site generator built with Python. Combined with Material for MkDocs[^2], it provides a feature-rich documentation platform.

    [^1]: MkDocs was created by Tom Christie and is released under the BSD license. See [mkdocs.org](https://www.mkdocs.org/) for more.
    [^2]: Material for MkDocs is maintained by Martin Donath. It supports over 60 languages and dozens of plugins.

=== "Markdown"

    ```markdown
    MkDocs[^1] is a static site generator built with Python.
    Combined with Material for MkDocs[^2], it provides a
    feature-rich documentation platform.

    [^1]: MkDocs was created by Tom Christie and is released
        under the BSD license.
    [^2]: Material for MkDocs is maintained by Martin Donath.
        It supports over 60 languages and dozens of plugins.
    ```

## Syntax

```markdown
Reference in text: [^label]
Definition:        [^label]: Footnote content here
```

Footnotes are collected and rendered at the bottom of the page, regardless of where the definitions appear in the source.
