# Snippets

Extension: `pymdownx.snippets`

Snippets pull content from another file into a page at build time, so shared text (a changelog, license, or a reusable section) lives in one place and stays in sync.

## Including a File

This site's [Changelog](../changelog.md) is the repository's root `CHANGELOG.md`, pulled in with a single line:

```markdown
;--8<-- "CHANGELOG.md"
```

The marker must be on its own line. Paths are resolved relative to the directory MkDocs runs from (the project root), so `CHANGELOG.md` refers to the file next to `mkdocs.yml`.

## Including Part of a File Into a Block

Indent the marker to pull a file into another block, such as a message, and append a line range to include only a slice. The example below includes lines 3 through 8 of the changelog:

=== "Result"

    !!! quote "From the changelog"

        --8<-- "CHANGELOG.md:3:8"

=== "Markdown"

    ```markdown
    !!! quote "From the changelog"

        ;--8<-- "CHANGELOG.md:3:8"
    ```

The included content is indented to match the block it lands in. Omit either side of the range (`:3:` or `::8`) to read from the start or to the end of the file.

## Syntax

```markdown
;--8<-- "path/to/file.md"        # whole file
;--8<-- "path/to/file.md:5:10"   # lines 5 through 10
```

Because the marker is processed before the page renders, write a leading semicolon (`;--8<--`) when you want to show the literal syntax instead of triggering an include, as on this page.
